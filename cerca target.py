from djitellopy import Tello
import time
# create and connect
# 创建Tello对象并连接
tello = Tello()
tello.connect()

target = 2
distanza = 50
massimo = 1
totale = 50
# configure drone
# 设置无人机

tello.enable_mission_pads()
tello.set_mission_pad_detection_direction(0)  # forward detection only  只识别前方

tello.takeoff()
time.sleep(1)

pad = tello.get_mission_pad_id()
print("Il pad numerato è il: ", tello.get_mission_pad_id())

while pad != target:
    
for i in range(1, 50):

    for i in range(1,massimo):
    	tello.move_forward(distanza)
	    tello.rotate_counter_clockwise(90)
	    pad = tello.get_mission_pad_id()
	    print("Il pad è:", pad)
    
	    if pad == target:
	    	tello.land()
	    	tello.end()
	    tello.move_forward(distanza)
	    tello.rotate_counter_clockwise(90)
	    pad = tello.get_mission_pad_id()
	    print("Il pad è:", pad)
    

    if pad == target:
    	tello.land()
    	tello.end()
    
    totale=totale+50

    if totale>400:
    	tello.land()
    	tello.end()

print("Il pad numerato è il: ", tello.get_mission_pad_id())

tello.disable_mission_pads()
tello.land()
tello.end()
