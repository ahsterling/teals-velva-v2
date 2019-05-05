from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/adam')
def adam():
    return render_template('students/adam.html', name="Adam")

@app.route('/wyatt')
def wyatt():
    return render_template('students/wyatt.html', name="Wyatt")

@app.route('/paul')
def paul():
    return render_template('students/paul.html', name="Paul")

@app.route('/grace')
def grace():
    return render_template('students/grace.html', name="Grace")

@app.route('/isabella')
def isabella():
    return render_template('students/isabella.html', name="Isabella")

@app.route('/daniel')
def daniel():
    return render_template('students/daniel.html', name="Daniel")

@app.route('/morgan')
def morgan():
    return render_template('students/morgan.html', name="Morgan")

@app.route('/gunnar')
def gunnar():
    return render_template('students/gunnar.html', name="Gunnar")

@app.route('/bryson')
def bryson():
    return render_template('students/bryson.html', name="Bryson")

@app.route('/jerry')
def jerry():
    return render_template('students/jerry.html', name="Jerry")

@app.route('/michael')
def michael():
    return render_template('students/michael.html', name="Michael")

@app.route('/skyler')
def skyler():
    return render_template('students/skyler.html', name="Skyler")

if __name__ == '__main__':
    app.run()
