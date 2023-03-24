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
    "Project.toml",
    "Manifest.toml",
    "node_modules/",
    "package-lock.json",
    "package.json",
    ".prettierrc.json",
    ".prettierignore",
    "pyproject.toml",
    "poetry.lock",
    ".venv/",
    "__pycache__/",
    "bin/",
    "src/",
    "utils/",
    "_assets/blog/mal-style/.sass-cache/"
]

# RSS (the website_{title, descr, url} must be defined to get RSS)
generate_rss = true
website_title = "anime"
website_descr = "Miscellaneous thoughts on life, anime, and more."
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
