import flask
import werkzeug

from app.repositories import sharepads as sharepad_repository


def front_page():
    return flask.render_template("index.html")


def sharepad(slug):
    sharepad = sharepad_repository.get_by_slug(slug)

    if not sharepad:
        raise werkzeug.exceptions.NotFound("Sharepad is unknown")

    return flask.render_template("sharepad.html", sharepad=sharepad)
