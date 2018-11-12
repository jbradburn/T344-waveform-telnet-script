import sys
import csv
import telnetlib
"""
	Numpy - using reshape, array, and empty
"""
import numpy as np
from time import sleep

#max trials size
MAX_SIZE = 2
#default host
HOST_M = "192.168.253.199"
HOST_S = "192.168.254.183"
#default port
PORT_M = "2000"
PORT_S = "2000"

# Default ch settings
SET_DEFAULT = '1,1000,0,0'

# Default command execute wait
SLEEP_CMD = 0.01

# Default command set wait
SLEEP_SET = 3

#Default device mode 
S_MODE = 0

def main():

	#initialize telnet connections
	try:
		tn1 = telnetlib.Telnet(HOST_M, PORT_M)
		tn2 = telnetlib.Telnet(HOST_S, PORT_S)

		# Move this somewhere else

		###

		# Set 1 as MASTER
		#tn1.write("MS 101")
		# Set 2 as SLAVE
		#tn2.write("MS 201")
		# Sync all M/S Channels
		# GLobal 3
		#tn1.write("GL 3")

		###

		response = "Telnet connection success\n"
		tFlag=1

		# Test
		data = getCSVData()
		tn1.write(b'QA 1\r')
		tn1.write(b'QF 1000\r')
		tn1.write(b'QP 0\r')
		tn1.write(b'QD 0\r')
		tn1.write(b'QL SI\r')
		print(data)

"""
	getCSVData

"""

def getCSVData():

	# Local vars to track index of channel and command in 'entries'
	ch = 0
	i = 0

	# Open source .csv file
	with open('dummy_data.csv', 'rt', encoding="utf8") as csvfile:
		csvreader = csv.reader(csvfile)	#reader instance from csv.py
		entries = list(csvreader)		#split csv file into 2D array by line with internal elements split by ',' chars

	# Iterate over channel configs (lines)
	for elem in entries:
		# Iterate over commands in each channel config with index i
		for command in elem:
			elem[i] = str(ch) + switcher(i) + ' ' + elem[i] # command = target channel number + command char + space + value
			i += 1											# Increment command index
		ch += 1 											# Increment config (line, channel) index
		# Reset target channel or command index to 0 if over 3
		if ch > 3 and ch = 0 or pass
		if i > 3 and i = 0 or pass
 
	entries = np.reshape(entries, (-1,4)) # Reshape entries array to an array with subarrays containing sets of 4 commands

	return entries

"""
	sendSingle
	Sends sets of four data points to each of four channels

"""
def sendSingle(data, tM, millis):
	# try/except/finally
	# Iterate over sets of channels
	try:
		for x in range(0, MAX_SIZE):
			print('Set ', x+1, '\n')					# Print set number to console
			# Iterate over channels in a set
			for y in range(0, 4):
				y += (x*4)
				print('Channel ', y)					# Print channel number to console
				# Iterate over commands for a channel
				for z in range(0, 4):
					s = bytes(data[y][z], 'utf-8') 		# Convert string command to byte string
					print("\n", data[y][z])				# Print current command to console
					tM.write(s + b'\r')					# Send bstr command to device (must terminate with a carriage return char)
					sleep(SLEEP_CMD)					# Wait buffer to load command to device
				print('\n')
		response = "Data load success\n"

		sleep(SLEEP_SET)								# Wait time for data set
	except:
		response = "Data load failed\n"
		tFlag=0
	finally:
		print(response, '\n')

"""
"""
def sendDouble(data, tM, tS, millis):
	try:
		# Iterate over sets of channels
		for x in range(0, MAX_SIZE):
			print('Set ', x+1, '\n')					# Print set number to console

			"""
			Master Device
			"""
			print('Master Device (0)')

			# Iterate over channels in a set
			for y in range(0, 4):
				y += (x*8)
				print('Channel ', y)					# Print channel number to console
				# Iterate over commands for a channel
				for z in range(0, 4):
					s = bytes(data[y][z], 'utf-8') 		# Convert string command to byte string
					print("\n", data[y][z])				# Print current command to console
					tM.write(s + b'\r')					# Send bstr command to device (must terminate with a carriage return char)
					sleep(SLEEP_CMD)					# Wait buffer to load command to device
				print('\n')

			"""
			Slave Device
			"""
			print('Slave Device (1)')

			# Iterate over channels in a set
			for y in range(4, 8):
				y += (x*8)
				print('Channel ', y)					# Print channel number to console
				# Iterate over commands for a channel
				for z in range(0, 4):
					s = bytes(data[y][z], 'utf-8') 		# Convert string command to byte string
					print("\n", data[y][z])				# Print current command to console
					tS.write(s + b'\r')					# Send bstr command to device (must terminate with a carriage return char)
					sleep(SLEEP_CMD)					# Wait buffer to load command to device
				print('\n')
		response = "Data load success\n"
		
		sleep(SLEEP_SET)								# Wait time for data set

	except:
		response = "Data load failed\n"
		tFlag = 0
	finally:
		print(response, "\n")

"""
	switcher
		Switch case to assist parsing parameter types to T344 commands
"""
def switcher(arg):
	switcher = {
	0: "A",
	1: "F",
	2: "P",
	3: "D"
	}
	return switcher.get(arg)

if __name__ == '__main__':
	main()

