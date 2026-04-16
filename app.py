from flask import Flask, render_template, request, session, redirect, url_for, jsonify

app = Flask(__name__)
app.secret_key = "birthday_magic_2024"

# ✏️  Change this to whatever password you want to give your sister
PASSWORD = "taniii bada bhai hai"

# ✏️  Change this to your sister's name
SISTER_NAME = "Mansi"


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


if __name__ == "__main__":
    app.run(debug=True)
