from flask import Flask, render_template, request

app = Flask(__name__)
app.TEMPLATES_AUTO_RELOAD = True
app.DEBUG = True


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/oops')
def oops():
    return render_template('oops.html', search_results=request.args.get('q'))

@app.route('/secret')
def secret():
    return "my secret"
