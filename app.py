from flask import Flask, request, render_template
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TXT_FILE = os.path.join(BASE_DIR, "whosaidhi.txt")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/sayhi", methods=["GET", "POST"])
def sayhi() -> render_template:

    if request.method == "POST":

        name = request.form.get("username")

        print(name)

        with open(TXT_FILE, "a") as f:
            f.write(f"{name} said hi!\n")

        return render_template("hireturn.html")

    return render_template("name.html")
@app.route("/projects")
def projects():
    
    return render_template("projects.html")



if __name__ == "__main__":
    app.run(debug=True)