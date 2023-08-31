import cyberpi
import time

sensor = "R2"
conectado = 1

@cyberpi.event.is_press("up")
def repetimos ():
    cyberpi.mbot2.cyberpi.quad_rgb_sensor.is_line(sensor, conectado)
    
    