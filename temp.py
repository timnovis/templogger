#!/usr/bin/env python
import os, json, re, time

def writeTemp():

	temp = os.popen("/opt/vc/bin/vcgencmd measure_temp").read()
	rawtemp = re.sub(r'[^0-9.]', "", temp)
	timestamp = time.time()


	with open('data.json', 'a') as outfile: 
		json.dump({'temp' : rawtemp, 'time' : timestamp}, outfile)

		time.sleep(300)

while True: 
	writeTemp()
