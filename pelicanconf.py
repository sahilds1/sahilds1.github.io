THEME = "."
AUTHOR = "Sahil Shah"
SITENAME = "Sahil Shah"
SITEURL = "http://localhost:8000"
PATH = "content"
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_SOURCES = True
TYPOGRIFY = True
TYPOGRIFY_DASHES = "oldschool"
TIMEZONE = "America/New_York"
DEFAULT_LANG = "en"
DEFAULT_PAGINATION = 10
CATEGORIES_SAVE_AS = "categories/index.html"
CATEGORIES_URL = "categories/"
TAGS_SAVE_AS = "tags/index.html"
TAGS_URL = "tags/"
AUTHORS_SAVE_AS = "authors/index.html"
AUTHORS_URL = "authors/"
ARCHIVES_SAVE_AS = "archives/index.html"
ARCHIVES_URL = "archives/"


FEED_DOMAIN = SITEURL

# Make the URLs of article permalink pages nicer.
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SOURCE_URL = "{article.url}index{OUTPUT_SOURCES_EXTENSION}"

# Make the URLs of period archive pages nicer.
YEAR_ARCHIVE_SAVE_AS = "{date:%Y}/index.html"
YEAR_ARCHIVE_URL = "{date:%Y}/"
MONTH_ARCHIVE_SAVE_AS = "{date:%Y}/{date:%m}/index.html"
MONTH_ARCHIVE_URL = "{date:%Y}/{date:%m}/"
DAY_ARCHIVE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/index.html"
DAY_ARCHIVE_URL = "{date:%Y}/{date:%m}/{date:%d}/"

# Make the URLs of static pages nicer.
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SOURCE_URL = "{page.url}index{OUTPUT_SOURCES_EXTENSION}"

# Links (renamed from LINKS to MENUITEMS for Sidecar compatibility)
MENUITEMS = (
    ("Atom Feed", "https://sahilds1.github.io/feeds/all.atom.xml"),
    ("GitHub", "https://github.com/sahilds1"),
    ("LinkedIn", "https://www.linkedin.com/in/sahildshah1/"),
)

# GitHub URL for navbar
GITHUB_URL = "https://github.com/sahilds1"

# Sidecar navbar configuration (corrected from SIDECAR_MENU)
SIDECAR_NAVBAR = [
    "HOME",
    "MENUITEMS",
    "PAGES",
    "CATEGORIES",
    "TAGS",
    "ARCHIVES",
    "GITHUB",  # Added since GITHUB_URL is set
]

# Sidecar article tagline configuration (corrected from SIDECAR_TAGLINE)
SIDECAR_ARTICLE_TAGLINE_ITEMS = [
    "TIME",
    "AUTHORS",
    "TAGS",
]

# Optional: Configure article footer items
# SIDECAR_ARTICLE_FOOTER_ITEMS = ["AUTHORS"]

# Optional: Configure page tagline and footer items
# SIDECAR_PAGE_TAGLINE_ITEMS = []
# SIDECAR_PAGE_FOOTER_ITEMS = ["TIME"]

# Optional: Set date format for better appearance
# DEFAULT_DATE_FORMAT = "%b %d, %Y"

# Optional: Configure GitHub URL for navbar GitHub icon
# GITHUB_URL = "https://github.com/sahilds1"

# Optional: Configure site bio for homepage
# AVATAR_URL = "https://gravatar.com/avatar/..."
# SITESUBTITLE = "Your site subtitle"
# SITEBIO = "Your bio text"

# Optional: Configure syntax highlighting theme
# SIDECAR_PYGMENTS_THEME = "monokai"
# SIDECAR_PYGMENTS_BORDERLESS = True

# Optional: Configure custom CSS
# STYLESHEET = """
#     :root {
#       --ok-color-bg: #ff851b;
#       --ok-color-fg: #85144b;
#     }
# """