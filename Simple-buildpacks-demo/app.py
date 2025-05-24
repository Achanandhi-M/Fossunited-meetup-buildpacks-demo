from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h1>Please register for the <a href="https://fossunited.org/indiafoss/2025">India FOSS 2025</a></h1>
        <h2>Submit your CFP before <strong>June 7</strong> <a href="https://fossunited.org/dashboard/cfp/apply/indiafoss/2025">here</a></h2>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
