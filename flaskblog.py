from flask import Flask, render_template, url_for
from forms import ResgistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ccd05cf35eafd2881ba52b6b7ba4e052'


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


@app.route("/register")
def register():
    form = ResgistrationForm()
    return render_template('register.html', tittle='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', tittle='Login', form=form)
