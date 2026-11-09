from flask import Flask, render_template, request

app = Flask(__name__, template_folder=".")


@app.route("/", methods=["GET"])
def index():
    return render_template("registrationform.html")


@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username", "").strip()
    if not username:
        return "Username is required.", 400

    return render_template("successful.html", name=username)


if __name__ == "__main__":
    app.run()
