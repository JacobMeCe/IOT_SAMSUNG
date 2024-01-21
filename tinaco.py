# Importar las bibliotecas necesarias
import RPi.GPIO as GPIO
import time

# Configurar el modo de GPIO
GPIO.setmode(GPIO.BCM)

# Definir el pin del sensor de nivel de agua y el pin de la válvula de llenado
pin_sensor_agua = 17
pin_valvula_llenado = 18

# Configurar el pin del sensor como entrada
GPIO.setup(pin_sensor_agua, GPIO.IN)

# Configurar el pin de la válvula de llenado como salida
GPIO.setup(pin_valvula_llenado, GPIO.OUT)


def leer_nivel_agua():
    # Leer el estado del sensor (0 = agua presente, 1 = sin agua)
    return GPIO.input(pin_sensor_agua)


def activar_valvula_llenado():
    print("Iniciando el llenado del tinaco...")
    GPIO.output(pin_valvula_llenado, GPIO.HIGH)


def desactivar_valvula_llenado():
    print("Deteniendo el llenado del tinaco.")
    GPIO.output(pin_valvula_llenado, GPIO.LOW)


try:
    while True:
        nivel_agua = leer_nivel_agua()

        if nivel_agua == 0:
            print("¡Agua detectada!")
            desactivar_valvula_llenado()
        else:
            print("Sin agua")
            activar_valvula_llenado()

        # Esperar un tiempo antes de la siguiente lectura
        time.sleep(2)

except KeyboardInterrupt:
    # Manejar la interrupción del teclado (Ctrl+C)
    pass

finally:
    # Limpiar los pines GPIO al finalizar
    GPIO.cleanup()
