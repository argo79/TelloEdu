from djitellopy import Tello
import time
# create and connect
# 创建Tello对象并连接

tello = Tello()
tello.connect()

tello.set_mission_pad_detection_direction(0) 
tello.set_speed(100)
batt = tello.get_battery()
print("La batteria è al ",batt,"%.")
tello.takeoff()
time.sleep(1)

padTarget = 5

tello.enable_mission_pads()

originPad=tello.get_mission_pad_id()
time.sleep(1)


print("Il pad di partenza è il numero: ", originPad,".")
print("Il pad da ricercare è il numero: ", padTarget,".")

xPad=tello.get_mission_pad_distance_x()
yPad=tello.get_mission_pad_distance_y()
zPad=tello.get_mission_pad_distance_z()

tello.go_xyz_speed_mid(-100,-125,150,100,originPad)

tello.land()
tello.end()