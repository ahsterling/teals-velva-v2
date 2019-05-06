from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/adam')
def adam():
    return render_template('students/adam.html', name="Adam", grad_year="?")

@app.route('/wyatt')
def wyatt():
    return render_template('students/wyatt.html', name="Wyatt", grad_year="?")

@app.route('/paul')
def paul():
    return render_template('students/paul.html', name="Paul", grad_year="?")

@app.route('/grace')
def grace():
    return render_template('students/grace.html', name="Grace", grad_year="?")

@app.route('/isabella')
def isabella():
    return render_template('students/isabella.html', name="Isabella", grad_year="?")

@app.route('/daniel')
def daniel():
    return render_template('students/daniel.html', name="Daniel", grad_year="2021")

@app.route('/morgan')
def morgan():
    return render_template('students/morgan.html', name="Morgan", grad_year="2021")

@app.route('/gunnar')
def gunnar():
    return render_template('students/gunnar.html', name="Gunnar", grad_year="2021")

@app.route('/bryson')
def bryson():
    return render_template('students/bryson.html', name="Bryson", grad_year="?")

@app.route('/jerry')
def jerry():
    return render_template('students/jerry.html', name="Jerry", grad_year="2021")

@app.route('/michael')
def michael():
    return render_template('students/michael.html', name="Michael", grad_year="2020")

@app.route('/skyler')
def skyler():
    return render_template('students/skyler.html', name="Skyler", grad_year="2020")

if __name__ == '__main__':
    app.run()
