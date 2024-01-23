import RPi.GPIO as GPIO


class LEDController:
    def __init__(self, pinAguaBaja, pinTinacoLlenandose, pinSinAgua):
        self.pinAguaBaja = pinAguaBaja
        self.pinTinacoLlenandose = pinTinacoLlenandose
        self.pinSinAgua = pinSinAgua
        GPIO.setup(self.pinAguaBaja, GPIO.OUT)
        GPIO.setup(self.pinTinacoLlenandose, GPIO.OUT)
        GPIO.setup(self.pinSinAgua, GPIO.OUT)

    def update_leds(self, flujo, nivel, NIVEL_MINIMO, NIVEL_MAXIMO, FLUJO_MINIMO):
        # Apagar los LEDs
        GPIO.output(self.pinAguaBaja, GPIO.LOW)
        GPIO.output(self.pinTinacoLlenandose, GPIO.LOW)
        GPIO.output(self.pinSinAgua, GPIO.LOW)

        # Encender los LEDs correspondientes
        if nivel < NIVEL_MINIMO:
            GPIO.output(self.pinSinAgua, GPIO.HIGH)
        elif nivel > NIVEL_MAXIMO:
            GPIO.output(self.pinTinacoLlenandose, GPIO.HIGH)
        elif flujo < FLUJO_MINIMO:
            GPIO.output(self.pinAguaBaja, GPIO.HIGH)

    def cleanup(self):
        GPIO.output(self.pinAguaBaja, GPIO.LOW)
        GPIO.output(self.pinTinacoLlenandose, GPIO.LOW)
        GPIO.output(self.pinSinAgua, GPIO.LOW)
        GPIO.cleanup()
