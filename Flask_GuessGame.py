import random
from flask import Flask
app = Flask(__name__)
n = random.randint(0,9)

def whattodo(fun):
    def wrap(**args):
        if args['num'] > n:
            return "<h1>Too High!</h1><img src='https://media0.giphy.com/media/3oz8xLd9DJq2l2VFtu/giphy.gif'>"
        elif args['num']<n:
            return "<h1>Too Low!</h1><img src='https://media0.giphy.com/media/3oz8xLd9DJq2l2VFtu/giphy.gif'>"
        else:
            return "<h1>You are right</h1><img src='https://media.giphy.com/media/l1J9wXoC8W4JFmREY/giphy.gif'>"
    return wrap
@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1><img src="https://media.giphy.com/media/307aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<int:num>')
@whattodo
def f(num):
    pass

if __name__=='__main__':
    app.run()