# Questo codice fa muovere Tello Edu alla ricerca di un PAD bersaglio

from djitellopy import Tello
import time
# create and connect
# 创建Tello对象并连接

speed=20
padTarget=5
x=35
y=35
altezza=80


tello = Tello()
tello.connect()

batt = tello.get_battery()
print("La batteria è al ",batt,"%.")

tello.set_mission_pad_detection_direction(0) 
tello.set_speed(speed)
tello.takeoff()
time.sleep(1)

tello.enable_mission_pads()

originPad=tello.get_mission_pad_id()


print("Il pad di partenza è il numero: ", originPad,".")
print("Il pad da ricercare è il numero: ", padTarget,".")






tello.go_xyz_speed_mid(x,-y,altezza,speed,originPad)
padId=tello.get_mission_pad_id()
print("Il pad di partenza è il numero: ", padId,".")
tello.go_xyz_speed_mid(x,y,altezza,speed,originPad)
padId=tello.get_mission_pad_id()
print("Il pad di partenza è il numero: ", padId,".")
tello.go_xyz_speed_mid(-x,y,altezza,speed,originPad)
padId=tello.get_mission_pad_id()
print("Il pad di partenza è il numero: ", padId,".")
tello.go_xyz_speed_mid(-x,-y,altezza+20,speed,originPad)
time.sleep(3)
padId=tello.get_mission_pad_id()
print("Il pad di partenza è il numero: ", padId,".")
tello.go_xyz_speed_mid(35,35,altezza,speed,padId)
padId=tello.get_mission_pad_id()
tello.go_xyz_speed_mid(0,0,altezza,speed,padId)

tello.land()
tello.end()
