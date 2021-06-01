# coding=utf-8
from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import random
import copy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fflask.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100))
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/test')
def test():
    return render_template("test.html")


@app.route('/create-article', methods=['POST', 'GET'])
def create_article():
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Article(title=title, intro=intro, text=text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/')
        except:
            return "Произошла ошибка"
    else:
        return render_template("create-article.html")


@app.route('/ttest1')
def ttest1():
    return render_template("ttest1.html")


@app.route('/ttest2')
def ttest2():
    return render_template("ttest2.html")


@app.route('/ttest3')
def ttest3():
    return render_template("ttest3.html")


@app.route('/ttest4')
def ttest4():
    return render_template("ttest4.html")


@app.route('/ttest5')
def ttest5():
    return render_template("ttest5.html")


@app.route('/test1')
def test1():
    return render_template("test1.html")


@app.route('/test2')
def test2():
    return render_template("test2.html")


@app.route('/test3')
def test3():
    return render_template("test3.html")


@app.route('/test4')
def test4():
    return render_template("test4.html")


@app.route('/test5')
def test5():
    return render_template("test5.html")


@app.route('/profile')
def profile():
    return render_template("profile.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/signup')
def signup():
    return render_template("signup.html")


@app.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user:
        return redirect(url_for('app.signup'))

    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('app.login'))


@app.route('/logout')
def logout():
    return render_template("logout.html")


@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('app.login'))

    return redirect(url_for('app.profile'))


original_questions = {
 'Soft Self-Portrait with Grilled Bacon': ['Dali', 'Malevich', 'Picasso', 'Chagall', 'Kandinsky'],
 'Absinthe Drinker': ['Picasso', 'Dali', 'Kandinsky', 'Chagall', 'Malevich'],
 'Blue Lovers': ['Chagall', 'Kandinsky', 'Malevich', 'Dali', 'Picasso'],
 'First Abstract Watercolor': ['Kandinsky', 'Picasso', 'Dali', 'Chagall', 'Malevich'],
 'Black Square': ['Malevich', 'Dali', 'Chagall', 'Kandinsky', 'Picasso'],
 'Violinist': ['Chagall', 'Malevich', 'Kandinsky', 'Dali', 'Picasso'],
 'Ghost Carriage': ['Dali', 'Kandinsky', 'Picasso', 'Chagall', 'Malevich']
}
questions = copy.deepcopy(original_questions)

original_questions1 = {
 'Garden of Earthly Delights': ['Bosch', 'da Vinci', 'Durer', 'Bruegel', 'Tiziano'],
 'Tabletop of the Seven Deadly Sins and the Four Last Things': ['Bosch', 'da Vinci', 'Durer', 'Bruegel', 'Tiziano'],
 'Mona Lisa': ['da Vinci', 'Bosch', 'Durer', 'Bruegel', 'Tiziano'],
 'Madonna of the Pear': ['Durer', 'Bosch', 'da Vinci', 'Bruegel', 'Tiziano'],
 'Tower of Babel': ['Bruegel', 'Bosch', 'da Vinci', 'Durer', 'Tiziano'],
 'The hunters in the Snow': ['Bruegel', 'Bosch', 'da Vinci', 'Durer', 'Tiziano'],
 'Venus Blindfolding Cupid': ['Tiziano', 'Bosch', 'da Vinci', 'Durer', 'Bruegel']
}
questions1 = copy.deepcopy(original_questions1)


def shuffle(q):
    selected_keys = []
    i = 0
    while i < len(q):
        current_selection = random.choice(q.keys())
        if current_selection not in selected_keys:
            selected_keys.append(current_selection)
            i = i+1
    return selected_keys


@app.route('/quiz1')
def quiz():
    questions_shuffled = shuffle(questions)
    for i in questions.keys():
        random.shuffle(questions[i])
    return render_template('quiz1.html', q=questions_shuffled, o=questions)


@app.route('/quiz', methods=['POST'])
def quiz_answers():
    correct = 0
    for i in questions.keys():
        answered = request.form[i]
        if original_questions[i][0] == answered:
            correct = correct+1
    return render_template("quiz.html", f=correct)


@app.route('/quizz1')
def quizz():
    questions_shuffled1 = shuffle(questions1)
    for i in questions1.keys():
        random.shuffle(questions1[i])
    return render_template('quizz1.html', q=questions_shuffled1, o=questions1)


@app.route('/quizz', methods=['POST'])
def quizz_answers():
    correct1 = 0
    for i in questions1.keys():
        answered = request.form[i]
        if original_questions1[i][0] == answered:
            correct1 = correct1+1
    return render_template("quizz.html", f=correct1)


if __name__ == "__main__":
    app.run(debug=True)