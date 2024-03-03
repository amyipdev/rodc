#!/usr/bin/env python3

import os
import hashlib

from flask import Flask, render_template, abort, send_from_directory, request

app = Flask(__name__)
key = os.environ["RODC_API_KEY"]


@app.errorhandler(404)
def nf(_e):
    return render_template("404.html"), 404


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/f/<fil>")
def fil(fil: str):
    return send_from_directory("files", fil)


# Randomized file name
@app.route("/s/<ext>", methods=["PUT"])
def s(ext: str):
    if request.headers.get("X-RODC-Authentication") != key:
        abort(401)
    v = request.data
    c = hashlib.sha256(v).hexdigest()[:12]
    w = f"files/{c}.{ext}"
    open(w, "wb").write(v)
    return w, 200


# Keep file name
@app.route("/sf/<fil>", methods=["PUT"])
def sf(fil: str):
    if request.headers.get("X-RODC-Authentication") != key:
        abort(401)
    v = request.data
    open(f"files/{fil}", "wb").write(v)
    return "OK", 200


if __name__ == "__main__":
    app.run(host="::", port=8081)
