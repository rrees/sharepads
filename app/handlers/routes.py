from . import pages

routes = [
    ("/", "index", pages.front_page, ["GET"]),
    ("/sharepad/<slug>", "sharepad", pages.sharepad, ["GET"]),
]
