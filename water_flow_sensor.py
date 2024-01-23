import RPi.GPIO as GPIO
import time


class WaterFlowSensor:
    def __init__(self, pin):
        self.pin = pin
        self.flow_rate_count = 0
        self.flow_rate = 0
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.pin, GPIO.RISING,
                              callback=self.pulse_callback)

    def pulse_callback(self, pin):
        self.flow_rate_count += 1

    def calculate_flow(self, pulses_per_liter):
        # Convertir pulsos a litros por minuto
        self.flow_rate = (self.flow_rate_count / pulses_per_liter) / 60
        self.flow_rate_count = 0

    def read_flow(self):
        pulses_per_liter = 450
        time.sleep(1)
        self.calculate_flow(pulses_per_liter)
        return self.flow_rate
