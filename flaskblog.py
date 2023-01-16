from flask import Flask, render_template, url_for, flash, redirect
from forms import ResgistrationForm, LoginForm
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ccd05cf35eafd2881ba52b6b7ba4e052'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


posts = [
    {
        'author': 'Gael Mahe',
        'title': 'My first blog post',
        'content': 'First post content',
        'date_posted': '26 Mars, 2022'
    },

    {
        'author': 'Emily Johnson',
        'title': 'The Importance of Self-Care',
        'content': 'In a world that can be fast-paced and stressful, it is crucial to make time for self-care. This can include anything from taking a relaxing bath to going for a walk in nature. Practicing self-care can help to improve your mental and physical well-being, and can also increase your ability to handle stress. This is my personal journey about self-care.',
        'date_posted': '22 january, 2022'
    },

    {
        'author': 'John Smith',
        'title': 'The Benefits of Yoga',
        'content': 'Yoga is a form of exercise that has been around for thousands of years. It is a great way to improve flexibility, strength, and balance. It can also help to reduce stress and improve overall mental well-being. In this post, I will discuss some of the benefits of yoga and how it can help you to improve your overall health and well-being.',
        'date_posted': '12 february, 2022'
    },

    {
        'author': 'Lana Del Rey',
        'title': 'The Beauty of Nature',
        'content': 'Nature has a way of bringing peace and tranquility to our lives. Whether it is the sight of a beautiful sunset or the sound of a babbling brook, nature has the ability to calm our minds and soothe our souls. In this post, I will share some of my personal experiences with nature and the beauty it holds.',
        'date_posted': '15 mars, 2022'
    }
]


@ app.route("/")
@ app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@ app.route("/about")
def about():
    return render_template('about.html', tittle='About')


@ app.route("/register", methods=['GET', 'POST'])
def register():
    form = ResgistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', tittle='Register', form=form)


@ app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@admin.com' and form.password.data == 'password':
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Failed to log in, please check email and password', 'danger')
    return render_template('login.html', tittle='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
