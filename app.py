import os
from flask import Flask, render_template, request, session, redirect, url_for, jsonify, send_from_directory

app = Flask(__name__)
app.secret_key = "birthday_magic_2026"
app.config["PHOTO_DIR"] = os.path.join(app.root_path, "photos")

# ✏️  Change this to whatever password you want to give your sister
PASSWORD = "myBaji"

# ✏️  Change this to your sister's name
SISTER_NAME = "Fouziya Baji"



@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        pwd = request.form.get("password", "")
        if pwd == PASSWORD:
            session["authenticated"] = True
            return redirect(url_for("special"))
        else:
            error = "Wrong password, try again! 💫"
    return render_template("login.html", error=error)


@app.route("/special")
def special():
    if not session.get("authenticated"):
        return redirect(url_for("login"))
    return render_template("special.html", name=SISTER_NAME)


@app.route("/cake")
def cake():
    if not session.get("authenticated"):
        return redirect(url_for("login"))
    return render_template("cake.html", name=SISTER_NAME)


@app.route("/fireworks")
def fireworks():
    if not session.get("authenticated"):
        return redirect(url_for("login"))
    return render_template("fireworks.html", name=SISTER_NAME)


@app.route("/letter")
def letter():
    if not session.get("authenticated"):
        return redirect(url_for("login"))
    return render_template("letter.html", name=SISTER_NAME)

@app.route("/photos")
def photos():
    if not session.get("authenticated"):
        return redirect(url_for("login"))

    images = sorted(
        [f for f in os.listdir(app.config["PHOTO_DIR"]) if os.path.isfile(os.path.join(app.config["PHOTO_DIR"], f))]
    )
    return render_template("photos.html", images=images, name=SISTER_NAME)


@app.route("/photos/<path:filename>")
def serve_photo(filename):
    return send_from_directory(app.config["PHOTO_DIR"], filename)


if __name__ == "__main__":
    app.run(debug=False)