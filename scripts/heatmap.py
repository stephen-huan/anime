from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import calmap
import history
from mal import ROOT
"""
Heatmap of episodes watched with calmap.
"""

OUT = "_assets/heatmap.png"

if __name__ == "__main__":
    entries = history.parse_entries()
    all_episodes = {}
    for entry in entries.values():
        for _, episode_date in entry["ordered"]:
            # day level resampling precision
            fmt = "%Y-%m-%d"
            episode_date = datetime.strptime(episode_date.strftime(fmt), fmt)
            all_episodes[episode_date] = all_episodes.get(episode_date, 0) + 1
    dates, weights = zip(*((day, all_episodes[day])
                           for day in sorted(all_episodes)))
    days, weights = pd.DatetimeIndex(dates), np.array(weights, dtype=np.int64)
    # outliers from importing a series without marking each individual episode
    # as well as natural viewing variance, use log to de-emphasize large values
    weights = np.log(weights)
    events = pd.Series(weights, index=days)
    # strong outliers so take the top 1% instead of actual max
    vmax = np.sort(weights)[round(0.99*(weights.shape[0] - 1))]
    # https://www.statology.org/matplotlib-change-font/
    import matplotlib
    matplotlib.rcParams["font.family"] = "Noto Sans Mono"
    calmap.calendarplot(
        # 0 is hard to read with colormap "YlGn" so bump it up a bit
        events, vmin=-1, vmax=vmax,
        # set to mean: https://github.com/martijnvermaat/calmap/issues/27
        how=None,
        # monthticks=False,
        daylabels=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        # daylabels="MTWTFSS",
        dayticks=[0, 2, 4, 6],
        # https://matplotlib.org/stable/tutorials/colors/colormaps.html
        cmap="YlGn",
        fillcolor="whitesmoke",
        linewidth=1,
        yearlabel_kws=dict(
            fontname="DejaVu Sans",
            # color="0.95",
        ),
        fig_kws=dict(
            figsize=(8, 6),
        ),
    )
    # or use calplot: https://github.com/tomkwok/calplot
    # import calplot
    # calplot.calplot(events)

    plt.savefig(OUT, bbox_inches="tight") # , pad_inches=0)

