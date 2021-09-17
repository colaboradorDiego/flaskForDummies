from flask import render_template
from flask import Flask


app = Flask(__name__)


@app.route('/basico')
def basico():
    data = {'Boca': 24, 'Platence': 20, 'Velez': 18}
    return render_template('basico.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
