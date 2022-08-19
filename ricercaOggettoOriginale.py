#Tello
import time


lunghezzaO = 400
larghezzaO = 400

distanzaP = 75
padTarget = 1

takeoff()
time.sleep(1)
enable_mission_pads()

originPad=get_mission_pad_id()

print("Il pad di partenza è il numero: ", originPad,".")
print("Il pad da ricercare è il numero: ", padTarget,".")

tello.move_right(25)
lunghezza=lunghezzaO
larghezza=larghezzaO-25
larghezzaO=larghezza

# Primo passaggio in lunghezza




while lunghezza>distanzaP:
	tello.move_forward(distanzaP)
	xPad=tello.get_mission_pad_distance_x()
	yPad=tello.get_mission_pad_distance_y()
	zPad=tello.get_mission_pad_distance_z()
	padId=tello.get_mission_pad_id()
	lunghezza=lunghezza-distanzaP

	if padId==padTarget:
		stato=1
		lunghezza=0
	
if lunghezza==distanzaP:
	tello.move_forward(50)
	xPad=tello.get_mission_pad_distance_x()
	yPad=tello.get_mission_pad_distance_y()
	zPad=tello.get_mission_pad_distance_z()
	padId=tello.get_mission_pad_id()
	lunghezza=lunghezza-50

	if padId==padTarget:
		stato=1
	
if stato==1:
	tello.go_xyz_speed_mid(0,0,0,75,padTarget)
	print("Il pad è stato trovato!")
	print("Le coordinate del Mission Pad numero ", padTarget," sono: x=",xPad,", y=",yPad," z=",zPad,".")
	time.sleep(5)
	tello.go_xyz_speed_mid(-xPad,-yPad,80,100,padTarget)
	land()

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
	larghezza=larghezza-distanzaP
	
	if padId==padTarget:
		stato=1
		larghezza=0

if larghezza==distanzaP:
	xPad=tello.get_mission_pad_distance_x()
	yPad=tello.get_mission_pad_distance_y()
	zPad=tello.get_mission_pad_distance_z()
	padId=tello.get_mission_pad_id()	
	larghezza=larghezza-50

	if padId==padTarget:
		stato=1

if stato==1:
	tello.go_xyz_speed_mid(0,0,0,75,padTarget)
	print("Il pad è stato trovato!")
	print("Le coordinate del Mission Pad numero ", padTarget," sono: x=",xPad,", y=",yPad," z=",zPad,".")
	time.sleep(5)
	tello.go_xyz_speed_mid(-xPad,-yPad,80,100,padTarget)
	land()

larghezza=larghezzaO-larghezza
larghezzaO=larghezza
print(larghezzaO)
print(larghezza)

tello.rotate_clockwise(90)

# SECONDO PASSAGGIO ! ! !