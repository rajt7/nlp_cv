from flask import Flask, render_template
app = Flask(__name__)


@app.route('/result')
def result():
    data = {'phy': 67, 'chem': 72, 'maths': 80}
    return render_template('render2.html', result=data)


if __name__ == '__main__':
    app.run(debug=True)