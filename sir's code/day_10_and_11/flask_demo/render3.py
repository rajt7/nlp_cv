from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    temp = {}
    if request.method == 'POST':
        data = request.form
        m1 = int(request.form['phy'])
        m2 = int(request.form['chem'])
        m3 = int(request.form['maths'])
        avg = (m1 + m2 + m3) / 3
        temp['name'] = request.form['name']
        temp['average'] = avg
    return render_template('render2.html', result=temp)


if __name__ == '__main__':
    app.run(debug=True)