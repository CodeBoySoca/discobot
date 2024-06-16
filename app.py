from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)


@app.route('/')
def signin():
    return render_template('signin.html')

@app.route('/signout')
def signout():
    pass

@app.route('/discobot')
def discobot():
    return render_template('discobot.html')

@app.route('/your-music')
def your_music():
    pass

@app.route('/playlist/<id>')
def playlist():
    pass

@app.route('/add/music')
def add_music():
    pass

if __name__ == '__main__':
    app.run(port=5555)