# coding=utf-8
from flask import Flask, render_template, url_for, request, redirect, flash
from datetime import datetime
import sqlite3
import random
import copy

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
@app.route('/home')
def indexa():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/create-article', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('posts'))

    return render_template("create-article.html")


@app.route('/posts')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template("posts.html", posts=posts)


@app.route('/test')
def test():
    return render_template("test.html")


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