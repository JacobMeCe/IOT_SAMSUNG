# Sistema de Monitoreo y Alerta de Nivel de Agua

Este proyecto es un sistema de monitoreo y alerta de nivel de agua diseñado para la Raspberry Pi. Utiliza un sensor de flujo de agua y un sensor de nivel de agua para monitorear el consumo de agua y el nivel del agua en un tanque, respectivamente. Alerta al usuario a través de LEDs en diferentes situaciones como: bajo flujo de agua, tanque llenándose y ausencia de agua.

## Componentes de Hardware

- Raspberry Pi (Modelo B o superior recomendado)
- Sensor de flujo de agua (con salida de pulso digital)
- Sensor de nivel de agua (digital que detecta presencia/ausencia de agua)
- LEDs (rojo, amarillo, verde)
- Resistencias de 220 ohmios para cada LED
- Cables y protoboard para las conexiones

## Configuración del Software

### Requisitos

Este proyecto requiere la siguiente configuración en su Raspberry Pi:

- Python 3.6 o superior
- RPi.GPIO (generalmente viene instalado en Raspberry Pi OS)
