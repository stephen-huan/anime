import argparse
from datetime import datetime
import os, shutil
import mal
"""
Maintain a text "database" of history, manually copied from MAL:
edit -> Episodes Watched history -> {anime title} Episode Details
"""

# path to history file
HISTORY_FILE = "_assets/history.txt"
# temp file to avoid overwriting
TEMP_FILE = "_assets/history.txt.tmp"
DATE_FORMAT = "%m/%d/%Y at %H:%M"

def parse_num(line: str) -> int:
    """ Parse a line's episode number (0-indexed). """
    return int(line.split()[1][:-1]) - 1

def parse_date(line: str) -> datetime:
    """ Parse a line into a datetime object. """
    # Ep {num}, watched on {DATE_FORMAT} Remove
    return datetime.strptime(" ".join(line.split()[4:-1]), DATE_FORMAT)

def parse_blocks(path: str) -> list[str]:
    """ Parse the raw input into a group of blocks. """
    blocks = [] # list of blocks
    block = []  # current block
    with open(path) as f:
        for line in map(str.strip, f.readlines()):
            if len(line) > 0:
                block.append(line)
            # assume blocks seperated by at least one blank line, new block
            elif len(block) > 0:
                blocks.append(block)
                block = []
    if len(block) > 0:
        blocks.append(block)
        block = []
    return blocks

def parse_entries(path: str=HISTORY_FILE) -> dict[str, dict[str,
    int | datetime | list[tuple[int, datetime]] | list[list[datetime]]]]:
    """ Parse the entries into the main data structure.

    The title of the anime is mapped to
    title: {
        "series_episodes": number of episodes in the anime,
        "start_date": when the anime was started,
        "finish_date": when the anime was finished,
        "ordered": [
            (episode number, date of first episode seen),
            (episode number, date of second episode seen),
            ...
            (eposide number, date of most recent episode seen),
        ],
        "episodes": [
            [first time seeing episode 1, second time, ...],
            [first time seeing episode 2, second time, ...],
            ...
            [first time seeing episode {series_episodes}, ...]
        ],
    }
    """
    # TODO: handle rewatches effectively
    list_type = mal.ListType.ANIME
    anime_list = mal.dict_view(mal.get_last_export(list_type))

    entries = {}
    for block in parse_blocks(path):
        # first line of the form "{series_title} Episode Details"
        title = " ".join(block[0].split(" ")[:-2])
        if title not in anime_list:
            print(f"{title} not found in the export.")
            continue
        # duplicate, take first entry in the file or not completed
        if title in entries or \
                anime_list[title]["my_status"] is not mal.Status.COMPLETED:
            continue
        num_episodes = anime_list[title]["series_episodes"]
        episodes = [[] for _ in range(num_episodes)]
        for line in block[1:]:
            episodes[parse_num(line)].append(parse_date(line))
        # define the "finish date" as the *first* time seeing the last episode
        # multiple re-watches of the show therefore does not affect it
        # reverse sorted by date
        finish_date = episodes[-1][-1] if len(episodes[-1]) > 0 else \
            anime_list[title]["my_finish_date"]
        # fill in implied missing values backwards from the known finish
        last_date = finish_date
        for num in range(num_episodes - 1, -1, -1):
            # haven't seen it but must have
            if len(episodes[num]) == 0:
                episodes[num].append(last_date)
            # use this date as closest reference
            else:
                last_date = episodes[num][-1]
        # made it all the way to the beginning
        start_date = last_date
        entries[title] = {
            "series_episodes": num_episodes,
            "start_date": start_date,
            "finish_date": finish_date,
            "ordered": sorted([
                (num + 1, date)
                for num, episode_list in enumerate(episodes)
                for date in episode_list
            ], key=lambda x: (x[1], x[0])),
            "episodes": episodes,
        }
    return entries

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="parse history")
    parser.add_argument("-p", "--path", default=HISTORY_FILE,
                        help="path to history file")
    parser.add_argument("-u", "--update", action="store_true",
                        help="update and reformat")
    parser.add_argument("-s", "--show", action="store_true",
                        help="show statistics")

    args = parser.parse_args()

    if args.update:
        blocks = parse_blocks(args.path)
        # remove duplicates
        headers = set()
        new_blocks = []
        for block in blocks:
            # first line is title
            key = block[0]
            if key not in headers:
                new_blocks.append(block)
                headers.add(key)
        # avoid losing history if interrupted in the middle
        shutil.copy(HISTORY_FILE, TEMP_FILE)
        with open(HISTORY_FILE, "w") as f:
            f.write("\n\n".join(
                "\n".join(block)
                for block in sorted(blocks, key=lambda block: block[0])))
        os.remove(TEMP_FILE)
    elif args.show:
        list_type = mal.ListType.ANIME
        anime_list = mal.get_last_export(list_type)
        entries = parse_entries(args.path)
        print(f"{len(entries)} entries in history.")
        for anime in anime_list[list_type]:
            title = anime["series_title"]
            if anime["my_status"] is mal.Status.COMPLETED and \
                    title not in entries:
                print(f"Missing {title} from history.")

