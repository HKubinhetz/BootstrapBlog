from flask import Flask
from flask import render_template
import getposts

app = Flask(__name__)


@app.route("/")
def homepage():
    img_path = "../static/assets/img/home-bg.jpg"
    posts = getposts.get_posts()
    return render_template('index.html', path=img_path, posts=posts)


@app.route("/about/")
def about_page():
    img_path = "../static/assets/img/about-bg.jpg"
    return render_template('about.html', path=img_path)


@app.route("/contact/")
def contact_page():
    img_path = "../static/assets/img/contact-bg.jpg"
    return render_template('contact.html', path=img_path)


if __name__ == "__main__":
    app.run(debug=True)
