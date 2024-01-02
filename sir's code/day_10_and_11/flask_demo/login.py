from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('sample.html')


@app.route('/success/<name>')
def success(name):
    return f'Welcome {name}'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        password = request.form['password']
        if user == 'admin' and password == 'admin@123':
            return redirect(url_for('success', name=user))
        elif user == 'admin' and password != 'admin@123':
            return '<p> Enter correct password'
        elif user != 'admin' and password == 'admin@123':
            return '<p> Enter correct user name'
        else:
            return redirect(url_for('success', name=user))


if __name__ == "__main__":
    app.run(debug=True)