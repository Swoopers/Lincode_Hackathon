import json
import time
import datetime

file_name_comm = "comm.json"
file_name_lidar = "lidar.json"
file_name_result = "results.json"
fmt = '%Y%m%d%H%M%S'

def readLidar():#for internal purpose only
	with open(file_name_lidar) as f:
		return json.load(f)

def updateResultInst():#for internal purpose only
	with open(file_name_result) as f:
		temp = json.load(f)
	temp['instruction count'] += 1
	with open(file_name_result, "w") as write_file:
		json.dump(temp, write_file)

def update(x):#for internal purpose only
	with open(file_name_comm, "w") as write_file:
		json.dump(x, write_file)
	updateResultInst()

def readF():#for internal purpose only
	with open(file_name_comm) as f:
		return json.load(f)

def updateEndMapping():
	with open(file_name_result) as f:
		temp = json.load(f)
	temp['end_mapping'] = datetime.datetime.now().strftime(fmt)
	with open(file_name_result, "w") as write_file:
		json.dump(temp, write_file)

def updateStartPlanning():
	with open(file_name_result) as f:
		temp = json.load(f)
	temp['start_planning'] = datetime.datetime.now().strftime(fmt)
	with open(file_name_result, "w") as write_file:
		json.dump(temp, write_file)

def updateEndPlanning():
	with open(file_name_result) as f:
		temp = json.load(f)
	temp['end_planning'] = datetime.datetime.now().strftime(fmt)
	with open(file_name_result, "w") as write_file:
		json.dump(temp, write_file)

def moveForward():
	temp = readF()
	temp['motion']['move'] = 1
	update(temp)

def moveBackward():
	temp = readF()
	temp['motion']['move'] = -1
	update(temp)

def rotateLeft():
	temp = readF()
	temp['motion']['rotate'] = -1
	update(temp)

def rotateRight():
	temp = readF()
	temp['motion']['rotate'] = 1
	update(temp)

def fetchLocation():
	temp = readF()
	temp['fetch_current_location'] = 1
	update(temp)
	for i in range(10):
		time.sleep(0.1)
		temp = readF()
		if temp['fetch_current_location'] == 0:
			return temp['current_location']
	return 'Location couldnt be fetched'

def getLidar():
	temp = readF()
	temp['fetch_lidar'] = 1
	update(temp)
	for i in range(10):
		time.sleep(0.1)
		temp = readF()
		if temp['fetch_lidar'] == 0:
			return readLidar()
	return 'LIDAR couldnt be fetched'