from flask import render_template, Blueprint
import markdown
import os

personal = Blueprint("personal", __name__)


@personal.route("/")
def portfolio():
    return render_template("portfolio.html")


@personal.route("/settings")
def settings():
    md_file = os.path.join(os.path.dirname(__file__), "../templates/homepage.md")
    with open(md_file, "r") as f:
        content = f.read()
        md = markdown.markdown(content)
    return render_template("index.html", content=md)
