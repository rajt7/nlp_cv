from flask import Flask
app = Flask(__name__)

@app.route('/<num>')
def hello_world(num):
    sq = int(num) ** 2
    return f'<p style="color:red">Square of {num} is {sq}.</p>'


@app.route('/well')
def welcome():
    return f'<p style="color:green">Welcome</p>'


@app.route('/good')
def good():
    return f'Good bye all!'


@app.route('/')
def home():
    return f'ou are at home page!'


if __name__ == '__main__':
    app.run(debug=True)