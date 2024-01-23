import RPi.GPIO as GPIO


class WaterLevelSensor:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)

    def read_level(self):

        if GPIO.input(self.pin) == GPIO.LOW:
            return "Agua detectada"
        else:
            return "No hay agua"
