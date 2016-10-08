from flask import *
import things

app = Flask(__name__)
pi_things = things.PiThings()

@app.route("/")
def hello():
      button = pi_things.read_button()
      return render_template('index.html', button=button)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
