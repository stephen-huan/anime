<!--
Add here global page variables to use throughout your website.
-->
+++
author = "Stephen Huan"
date_format= "yyyy-mm-dd"
mintoclevel = 2

# Add here files or directories that should be ignored by Franklin, otherwise
# these files might be copied and, if markdown, processed by Franklin which
# you might not want. Indicate directories by ending the name with a `/`.
# Base files such as LICENSE.md and README.md are ignored by default.
ignore = ["Project.toml", "Manifest.toml",
          "node_modules/", "package-lock.json", "package.json",
          "pyproject.toml", "poetry.lock", ".venv/", "__pycache__/",
          "bin/",
         ]

generate_sitemap = false
generate_robots = false
generate_rss = false

# RSS (the website_{title, descr, url} must be defined to get RSS)
# website_title = "anime"
# website_descr = "animelist"
website_url   = "https://stephen-huan.github.io/"
# prepath = "anime"

# header structure (url, display name)
headers = [("/", "index"),
           ("/profile/", "profile"),
           ("/animelist/", "animelist"),
          ]

# git repo for page source
git_repo = "https://github.com/stephen-huan/anime/blob/master"

# footer exclude
footer_exclude = Set(
  []
)
+++

<!--
Add here global LaTeX commands to use throughout your pages.
-->
\newcommand{\newline}{~~~<br>~~~} <!-- avoid self-closing tag <br/> -->
\newcommand{\circle}[1]{~~~<span class="circle #1"></span>~~~}
\newcommand{\figanime}[3]{
  \begin{wrap}{a href="!#3"}
    \begin{wrap}{span class="anime-title"}#1\end{wrap}
    \figalt{#1}{/assets/favorites/!#2}
  \end{wrap}
}
<!-- images -->
\newenvironment{figure}{\begin{wrap}{figure}}{\end{wrap}}
\newcommand{\caption}[1]{\begin{wrap}{figcaption}#1\end{wrap}}
\newcommand{\figpreview}[3]{
  \begin{wrap}{a href="!#3"}
    \figalt{#1}{#2}
  \end{wrap}
}
<!-- columns -->
\newenvironment{columns}{
  \begin{wrap}{div class="row"}
}{
  ~~~<div style="clear: both"></div>~~~\end{wrap}
}
\newenvironment{column}[2]{
  \begin{wrap}{div class="#1" style="width: #2;"}
}{
  \end{wrap}
}

