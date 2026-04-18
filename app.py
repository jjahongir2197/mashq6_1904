from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    error = ""
    success = ""

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        if len(name) < 3:
            error = "Name 3 ta harfdan kam bo'lmasin"

        elif "@" not in email:
            error = "Email ichida @ bo'lishi kerak"

        elif len(password) <= 6:
            error = "Password 6 dan katta bo'lishi kerak"

        else:
            success = "Registration successful!"

    return render_template(
        "index.html",
        error=error,
        success=success
    )

if __name__ == "__main__":
    app.run(debug=True)
