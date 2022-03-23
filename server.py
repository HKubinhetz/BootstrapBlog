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


@app.route("/post/<int:postid>")
def post_page(postid):
    print(postid)
    img_path = "../static/assets/img/post-bg.jpg"
    posts = getposts.get_posts()
    my_post = posts[postid-1]
    return render_template('post.html', path=img_path, post=my_post)


if __name__ == "__main__":
    app.run(debug=True)
