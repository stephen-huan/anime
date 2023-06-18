using Franklin: GLOBAL_LXDEFS, lxd, lxe, subs

const mal_commands = [
    lxd("circle", 1, raw"""~~~<span class="circle #1"></span>~~~"""),
    lxd("space", 0, raw"""~~~<span id="space">0</span>~~~"""),
    lxd(
        "figanime",
        3,
        raw"""
\begin{wrap}{a href="!#3"}
    \begin{wrap}{span class="anime-title"}#1\end{wrap}
    \includegraphics{#1}{/assets/favorites/!#2}{100}{150}
\end{wrap}""",
    ),
]

const mal_environments = []

for store in (mal_commands, mal_environments), (name, def) in store
    GLOBAL_LXDEFS[name] = def
end
