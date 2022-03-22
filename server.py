from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template('index.html')


@app.route("/about/")
def about_page():
    return render_template('about.html')


@app.route("/contact/")
def contact_page():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
