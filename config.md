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
ignore = [
    "Project.toml", "Manifest.toml",
    "node_modules/", "package-lock.json", "package.json",
    "pyproject.toml", "poetry.lock", ".venv/",
    "__pycache__/", "_assets/__pycache__/",
    "bin/",
]

# RSS (the website_{title, descr, url} must be defined to get RSS)
generate_rss = true
website_title = "anime"
website_descr = "Miscellaneous thoughts on anime"
website_url   = "https://anime.cgdct.moe/"
# prepath = "anime"

# doesn't seem to have a default value for tag pages
div_content = "franklin-content"

# header structure (url, display name)
headers = [
    ("/", "index"),
    ("/blog/", "blog"),
    ("/profile/", "profile"),
    ("/animelist/", "animelist"),
]

# git repo for page source
git_repo = "https://github.com/stephen-huan/anime/blob/master"

# footer exclude
footer_exclude = Set(
    ["/404/", "/blog/"]
)
+++

<!--
Add here global LaTeX commands to use throughout your pages.
-->
<!-- text formatting -->
\newcommand{\bold}[1]{
  \begin{wrap}{span class="font-weight-bold"}#1\end{wrap}
}
\newcommand{\emph}[1]{_!#1_}
\newcommand{\newline}{~~~<br>~~~} <!-- avoid self-closing tag <br/> -->
\newcommand{\href}[2]{\begin{wrap}{a href="!#1"}#2\end{wrap}}
\newcommand{\url }[1]{\href{!#1}{~~~#1~~~}}
\newcommand{\chapter      }[1]{\begin{wrap}{h1}#1\end{wrap}}
\newcommand{\section      }[1]{\begin{wrap}{h2}#1\end{wrap}}
\newcommand{\circle}[1]{~~~<span class="circle #1"></span>~~~}
\newcommand{\space    }{~~~<span id="space">0</span>~~~}
<!-- images -->
\newenvironment{figure}{\begin{wrap}{figure}}{\end{wrap}}
\newcommand{\includegraphics}[4]{
  ~~~<img alt="!#1" src="!#2" width="!#3" height="!#4">~~~
}
\newcommand{\caption}[1]{\begin{wrap}{figcaption}#1\end{wrap}}
\newcommand{\figpreview}[5]{
  \begin{wrap}{a href="!#5"}
    \includegraphics{!#1}{{{assets}}/!#2}{!#3}{!#4}
  \end{wrap}
}
\newcommand{\figanime}[3]{
  \begin{wrap}{a href="!#3"}
    \begin{wrap}{span class="anime-title"}#1\end{wrap}
    \includegraphics{#1}{/assets/favorites/!#2}{100}{150}
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

