+++
title = "anime profile"
+++

# Profile

## Statistics

\begin{columns}
\begin{column}{outer left}{50%}

### Anime stats

@@bottom-margin
Score $ \mu \pm \sigma $: {{score_mean 3}} $ \pm $ {{score_std 3}}
@@

@@stats-graph
<!-- one line to remove spaces: https://stackoverflow.com/questions/441279/ -->
~~~
 <span class="watching"      style="width: {{width_watching}}%"></span
><span class="completed"     style="width: {{width_completed}}%"></span
><span class="on_hold"       style="width: {{width_onhold}}%"></span
><span class="dropped"       style="width: {{width_dropped}}%"></span
><span class="plan_to_watch" style="width: {{width_plantowatch}}%"></span>
~~~
@@

\begin{columns}
\begin{column}{inner left}{52%}

@@clean-table,no-header,left
| legend                 | status        | number                |
|:-----------------------|--------------:|-----------------------|
| \circle{watching}      | Watching      | {{total_watching}}    |
| \circle{completed}     | Completed     | {{total_completed}}   |
| \circle{on_hold}       | On-hold       | {{total_onhold}}      |
| \circle{dropped}       | Dropped       | {{total_dropped}}     |
| \circle{plan_to_watch} | Plan to watch | {{total_plantowatch}} |
@@

\end{column}

\begin{column}{inner right no-margin}{44%}

@@clean-table,no-header,right
| status        | number              |
|:--------------|--------------------:|
| Total entries | {{total_anime}}     |
| Rewatched     | {{total_rewatched}} |
| Episodes      | {{total_episodes}}  |
@@

\end{column}

\end{columns}
\end{column}

\begin{column}{outer right no-margin}{45%}
@@img-full,nonumber,centering,bottom-margin
\begin{figure}
\includegraphics{Anime score distribution}{/assets/scores.png}{583}{492}
\caption{
  $ \mu $: {{score_mean 3}},
  $ \sigma^2 $: {{score_var 3}},
  $ \mathbb{H}[X] $: {{score_entropy 3}} bits
}
\end{figure}
@@
\end{column}

\end{columns}

\includegraphics{Anime viewing frequency heatmap}{
  /assets/heatmap.png
}{790}{553}

## Favorites

\begin{columns}
\begin{column}{grid left bottom-margin}{45%}

### Anime

<!-- manually break newlines to hint to css what the width is -->
@@favorites
\figanime{K-On!!}{anime/76121.webp}{
  https://myanimelist.net/anime/7791/K-On
}
\figanime{Shoujo \newline Shuumatsu \newline Ryokou}{anime/88321.webp}{
  https://myanimelist.net/anime/35838/Shoujo_Shuumatsu_Ryokou/
}
\figanime{Non Non Biyori}{anime/51581.webp}{
  https://myanimelist.net/anime/17549/Non_Non_Biyori
}
\figanime{Gochuumon wa \newline Usagi desu ka?}{anime/79600.webp}{
  https://myanimelist.net/anime/21273/Gochuumon_wa_Usagi_desu_ka
}
\figanime{Yojouhan Shinwa \newline Taikei}{anime/123689.webp}{
  https://myanimelist.net/anime/7785/Yojouhan_Shinwa_Taikei
}
\figanime{
  Monogatari \newline Series: Second \newline Season
}{anime/121534.webp}{
  https://myanimelist.net/anime/17074/Monogatari_Series__Second_Season
}
\figanime{
  Kono Subarashii \newline Sekai ni \newline Shukufuku wo!
}{anime/77831.webp}{
  https://myanimelist.net/anime/30831/Kono_Subarashii_Sekai_ni_Shukufuku_wo
}
\figanime{Steins;Gate}{anime/127974.webp}{
  https://myanimelist.net/anime/9253/Steins_Gate
}
\figanime{Mahou Shoujo \newline Madoka★Magica}{anime/55225.webp}{
  https://myanimelist.net/anime/9756/Mahou_Shoujo_Madoka%E2%98%85Magica
}
@@
\end{column}
\begin{column}{grid right no-margin}{45%}

### Characters

@@favorites
\figanime{Oikura Sodachi}{character/293644.webp}{
  https://myanimelist.net/character/130739/Sodachi_Oikura
}
\figanime{Akashi}{character/311918.webp}{
  https://myanimelist.net/character/31522/Akashi
}
\figanime{Makise Kurisu}{character/492885.webp}{
  https://myanimelist.net/character/34470/Kurisu_Makise
}
\figanime{Hiyajou Maho}{character/345914.webp}{
  https://myanimelist.net/character/83419/Maho_Hiyajou
}
\figanime{Haibara Ai}{character/308577.webp}{
  https://myanimelist.net/character/1743/Ai_Haibara
}
\figanime{Futaba Rio}{character/361763.webp}{
  https://myanimelist.net/character/163452/Rio_Futaba
}
\figanime{Shinonome Nano}{character/119458.webp}{
  https://myanimelist.net/character/10422/Nano_Shinonome
}
\figanime{Kafuu Chino}{character/244251.webp}{
  https://myanimelist.net/character/94941/Chino_Kafuu
}
\figanime{Akemi Homura}{character/219771.webp}{
  https://myanimelist.net/character/38005/Homura_Akemi
}
@@
\end{column}
\end{columns}

