import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

import mal

"""
Compute summary statistics for the profile page.
"""

# file to store statistics
DATAJL = "utils/data.jl"
# file to store score distribution
OUT = "_assets/scores.png"


def function(f, name: str, value, docstring: str = "", roundto: bool = False):
    f.write(
        f"""
\"\"\"
    {f"function hfun_{name}()" if not roundto else
     f"function hfun_{name}(digits=3)"}

{docstring}
\"\"\"
{f"hfun_{name}() = {value}" if not roundto else
 f"hfun_{name}(digits=3) = parseround({value}, digits)"}
"""
    )


if __name__ == "__main__":
    list_type = mal.ListType.ANIME
    anime_list = mal.get_last_export(list_type)
    animelist = anime_list[list_type]

    with open(DATAJL, "w") as f:
        f.write(
            f"# this file is automatically generated by {mal.ROOT}/stats.py.\n"
            "# editing it directly is not advised.\n"
        )
        f.write(
            """
\"\"\"
    function get_digits(digits)

Parse `digits` as an argument to a hfun function.
\"\"\"
get_digits(digits::Int) = digits
get_digits(args::Vector{String}) = parse(Int, args[1])

\"\"\"
    function parseround(value, digits)

Round `value` to `digits` digits, parsing `digits` if necessary.
\"\"\"
parseround(value, digits) = round(value; digits=get_digits(digits))

\"\"\"
    function width(count)

Get the percentage a category takes up out of total anime.
\"\"\"
width(count) = convert(Float64, 100 * (count / hfun_total_anime()))
"""
        )

        info = anime_list["info"]
        for key in info:
            if "total" in key:
                name = key.split("_")[1]
                docstring = (
                    f"Get the total "
                    f"{f'{name} ' if key != 'total_anime' else ''}anime."
                )
                function(f, key, info[key], docstring)
                if key != "total_anime":
                    f.write(
                        f"""
\"\"\"
    function hfun_width_{key}()

Get the percentage {name} anime takes up out of total anime.
\"\"\"
hfun_width_{name} = width(hfun_{key}())
"""
                    )

        total_episodes = 0
        # TODO: this is untested since I haven't rewatched anything yet
        total_rewatched = 0
        for anime in animelist:
            total_episodes += anime["my_watched_episodes"]
            total_rewatched += (
                anime["my_times_watched"] * anime["series_episodes"]
                + anime["my_rewatching_ep"]
            )

        function(
            f,
            "total_episodes",
            total_episodes,
            "Get the total number of episodes watched.",
        )
        function(
            f,
            "total_rewatched",
            total_rewatched,
            "Get the total number of episodes rewatched.",
        )

        scores = np.array(
            [
                anime["my_score"].value
                for anime in animelist
                if anime["my_score"] != mal.Score.UNSCORED
            ]
        )
        probs = np.array([np.sum(scores == i) for i in range(1, 11)])
        # probs = probs.astype(np.float64)/np.sum(probs)

        function(
            f,
            "score_mean",
            np.mean(scores),
            "Get the mean score.",
            roundto=True,
        )

        function(
            f,
            "score_var",
            np.var(scores),
            "Get the (uncorrected) variance of scores.",
            roundto=True,
        )

        function(
            f,
            "score_std",
            np.std(scores),
            "Get the (uncorrected) standard deviation of scores.",
            roundto=True,
        )

        function(
            f,
            "score_entropy",
            stats.entropy(probs, base=2),
            "Get the entropy of scores in bits",
            roundto=True,
        )

        plt.style.use("seaborn-v0_8-whitegrid")
        plt.rc("axes", titlesize=30)  # fontsize of the x and y labels
        plt.rc("axes", labelsize=20)  # fontsize of the x and y labels
        plt.rc("xtick", labelsize=20)  # fontsize of the x tick labels
        plt.rc("ytick", labelsize=20)  # fontsize of the y tick labels

        plt.hist(scores, bins=range(1, 12), rwidth=0.6, color="#26448f")

        plt.xticks(np.arange(1, 11) + 0.5, range(1, 11))
        plt.title("Score distribution")
        plt.xlabel("Score")
        plt.ylabel("Number of entries")

        plt.savefig(OUT, bbox_inches="tight")
