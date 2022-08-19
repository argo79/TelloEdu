# Questo codice fa muovere Tello Edu alla ricerca di un PAD bersaglio

from djitellopy import Tello
import time
# create and connect
# 创建Tello对象并连接


lunghezzaO = 400
larghezzaO = 400
altVolo=100
distanzaP = 75
padTarget = 3
stato=0  

tello = Tello()
tello.connect()

batt = tello.get_battery()
print("La batteria è al ",batt,"%.")

tello.set_mission_pad_detection_direction(0) 
tello.set_speed(100)
tello.takeoff()
time.sleep(1)

tello.enable_mission_pads()

originPad=tello.get_mission_pad_id()

print("Il pad di partenza è il numero: ", originPad,".")
print("Il pad da ricercare è il numero: ", padTarget,".")

tello.move_right(25)
#tello.rotate_counter_clockwise(90)
alt=tello.get_height()
diff=altVolo-alt
tello.move_up(diff)
alt=tello.get_height()
lunghezza=lunghezzaO
larghezza=larghezzaO-25
larghezzaO=larghezza


while stato==0 & (larghezza>distanzaP & lunghezza>distanzaP):

	# Primo passaggio in lunghezza

	while lunghezza>distanzaP:
		tello.move_forward(distanzaP)
		xPad=tello.get_mission_pad_distance_x()
		yPad=tello.get_mission_pad_distance_y()
		zPad=tello.get_mission_pad_distance_z()
		padId=tello.get_mission_pad_id()
		print("Il pad trovato è il numero: ", padId,".")
		lunghezza=lunghezza-distanzaP

		if padId==padTarget:
			stato=1
			lunghezza=0
			larghezza=0
	
	if lunghezza==distanzaP:
		tello.move_forward(50)
		xPad=tello.get_mission_pad_distance_x()
		yPad=tello.get_mission_pad_distance_y()
		zPad=tello.get_mission_pad_distance_z()
		padId=tello.get_mission_pad_id()
		print("Il pad trovato è il numero: ", padId,".")
		lunghezza=lunghezza-50

		if padId==padTarget:
			stato=1	
			larghezza=0
			larghezza=0

	lunghezza=lunghezzaO-lunghezza
	lunghezzaO=lunghezza
	print(lunghezzaO)
	print(lunghezza)
	tello.rotate_clockwise(90)

	# Primo passaggio in larghezza

	while larghezza>distanzaP:
		
		tello.move_forward(distanzaP)
		xPad=tello.get_mission_pad_distance_x()
		yPad=tello.get_mission_pad_distance_y()
		zPad=tello.get_mission_pad_distance_z()
		padId=tello.get_mission_pad_id()
		print("Il pad trovato è il numero: ", padId,".")
		larghezza=larghezza-distanzaP
		
		if padId==padTarget:
			stato=1
			larghezza=0
			lunghezza=0

	if larghezza==distanzaP:
		xPad=tello.get_mission_pad_distance_x()
		yPad=tello.get_mission_pad_distance_y()
		zPad=tello.get_mission_pad_distance_z()
		padId=tello.get_mission_pad_id()	
		print("Il pad trovato è il numero: ", padId,".")
		larghezza=larghezza-50

		if padId==padTarget:
			stato=1
			lunghezza=0
			larghezza=0

	larghezza=larghezzaO-larghezza
	larghezzaO=larghezza
	print(larghezzaO)
	print(larghezza)
	tello.rotate_clockwise(90)

if stato==1:
	tello.go_xyz_speed_mid(0,0,100,50,padTarget)
	print("Il pad è stato trovato!")
	print("Le coordinate del Mission Pad numero ", padTarget," sono: x=",xPad,", y=",yPad," z=",zPad,".")
	tello.land()
	time.sleep(5)
	tello.takeoff()
	time.sleep(1)
	tello.go_xyz_speed_mid(-xPad,-yPad,50,100,padTarget)
	
else:
	print("Il pad NON è stato trovato!")
	tello.rotate_clockwise(360)
	tello.land()

tello.end()