import mal
import history
"""
Various sanity checks on the consistency of a list.
- if marked as completed, watched every episode
- scored every completed entry
"""

if __name__ == "__main__":
    list_type = mal.ListType.ANIME
    anime_list = mal.get_last_export(list_type)
    for anime in anime_list[list_type]:
        if anime["my_status"] is mal.Status.COMPLETED:
            title, total = anime["series_title"], anime["series_episodes"]
            seen = anime["my_watched_episodes"]
            if seen != total:
                print(f"Marked {title} as completed but "
                      f"only watched {seen}/{total} episodes.")
            if anime["my_score"] is mal.Score.UNSCORED:
                print(f"Have not scored anime {title}.")

    anime_view = mal.dict_view(anime_list)
    total = sum(
        anime["series_episodes"]
        for anime in anime_list[list_type]
        if anime["my_status"] is mal.Status.COMPLETED
    )
    print(f"Sum of compeleted episodes: {total}")
    entries = history.parse_entries()
    total_eps = sum(
        len(entry["ordered"])
        for entry in entries.values()
    )
    print(f"Sum of   recorded episodes: {total_eps}")
    for title, entry in entries.items():
        eps = anime_view[title]["series_episodes"]
        recorded = len(entry["ordered"])
        if recorded != eps:
            print(f"{title} has {eps} episodes but {recorded} recorded.")


