import RPi.GPIO as GPIO

LED_PIN     = 17
BUTTON_PIN  = 4

class PiThings(object):

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED_PIN, GPIO.OUT)
        GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def read_button(self):
        return GPIO.input(BUTTON_PIN)

    def set_led(self, value):
        GPIO.output(LED_PIN, value)
