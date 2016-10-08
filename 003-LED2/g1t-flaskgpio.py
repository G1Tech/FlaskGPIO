from flask import *
import things

app = Flask(__name__)
pi_things = things.PiThings()

@app.route("/")
def hello():
      button = pi_things.read_button()
      return render_template('index.html', button=button)

@app.route("/led/<int:state>", methods=['POST'])
def led(state):
    if state == 0:
        pi_things.set_led(False)
    elif state == 1:
        pi_things.set_led(True)
    else:
        return ('Unknown LED state', 400)
    return ('', 204)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
