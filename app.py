from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/adam')
def adam():
    return render_template('students/adam.html')

@app.route('/wyatt')
def wyatt():
    return render_template('students/wyatt.html')

@app.route('/paul')
def paul():
    return render_template('students/paul.html')

@app.route('/grace')
def grace():
    return render_template('students/grace.html')

@app.route('/isabella')
def isabella():
    return render_template('students/isabella.html')

@app.route('/daniel')
def daniel():
    return render_template('students/daniel.html')

@app.route('/morgan')
def morgan():
    return render_template('students/morgan.html')

@app.route('/gunnar')
def gunnar():
    return render_template('students/gunnar.html')

@app.route('/bryson')
def bryson():
    return render_template('students/bryson.html')

@app.route('/jerry')
def jerry():
    return render_template('students/jerry.html')

@app.route('/michael')
def michael():
    return render_template('students/michael.html')

@app.route('/skyler')
def skyler():
    return render_template('students/skyler.html')

if __name__ == '__main__':
    app.run()
