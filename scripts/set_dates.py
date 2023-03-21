from datetime import datetime
import mal
import history
"""
Set the start and end dates to be the first and last episodes watched.
To update, load the resulting XML into:
https://myanimelist.net/import.php
"""

# file to store processed output
OUT = "animelist.xml"

def date_equal(date1: datetime, date2: datetime) -> bool:
    """ Whether two dates are equal to some precision. """
    fmt = "%Y-%m-%d"
    return date1.strftime(fmt) == date2.strftime(fmt)

if __name__ == "__main__":
    list_type = mal.ListType.ANIME
    anime_list = mal.get_last_export(list_type)
    entries = history.parse_entries()
    count = 0
    for anime in anime_list[list_type]:
        if anime["my_status"] is mal.Status.COMPLETED and \
                (anime["my_start_date"]  is None or \
                 anime["my_finish_date"] is None):
            title = anime["series_title"]
            start_date = entries[title]["start_date"]
            if anime["my_start_date"] is None:
                anime["my_start_date"] = start_date
            else:
                if not date_equal(anime["my_start_date"], start_date):
                    print(title, anime["my_start_date"], finish_date)
            finish_date = entries[title]["finish_date"]
            if anime["my_finish_date"] is None:
                anime["my_finish_date"] = finish_date
            else:
                if not date_equal(anime["my_finish_date"], finish_date):
                    print(title, anime["my_finish_date"], finish_date)
            # You MUST set this to value to 1 on all entries
            # you wish the database to update. Otherwise,
            # the import script will ignore those entries.
            anime["update_on_import"] = True
            count += 1

    mal.check_valid(anime_list)
    print(f"Updating {count} entries...")
    mal.write(OUT, mal.data_to_xml(anime_list))

