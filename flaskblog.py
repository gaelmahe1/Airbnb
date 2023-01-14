from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Gael Mahe',
        'title': 'My first blog post',
        'content': 'First post content',
        'date_posted': '26 Mars, 2022'
    },
    {
        'author': 'Kevin Mahe',
        'title': 'My slay blog post',
        'content': 'slay post content',
        'date_posted': '16 Mars, 2022'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', tittle='About')


@app.route("/404")
def error():
    return "<h1>Page is under construction</h1>"
