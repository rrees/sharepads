from . import pages

routes = [
    ("/", "index", pages.front_page, ["GET"]),
]
