from water_flow_sensor import WaterFlowSensor
from water_level_sensor import WaterLevelSensor
from led_controller import LEDController

import time
import RPi.GPIO as GPIO

pin_sensor_flujo = 17
pin_sensor_nivel = 27
pin_led_agua_baja = 22
pin_led_tinaco_llenandose = 10
pin_led_sin_agua = 9

pulses_per_liter = 450
nivel_minimo = 10
nivel_maximo = 90

flow_sensor = WaterFlowSensor(pin_sensor_flujo)
level_sensor = WaterLevelSensor(pin_sensor_nivel)
led_controller = LEDController(
    pin_led_agua_baja, pin_led_tinaco_llenandose, pin_led_sin_agua)

try:
    while True:
        flow = flow_sensor.read_flow()
        level = level_sensor.read_level()

        led_controller.set_led('sin_agua', not level)
        led_controller.set_led('agua_baja', flow < 1)
        led_controller.set_led('tinaco_llenandose', flow > 10)

        time.sleep(1)

except KeyboardInterrupt:
    print("Deteniendo el programa...")

finally:
    led_controller.cleanup()
