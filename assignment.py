from __future__ import print_function

import time
from sr.robot import *

"""
Assignment 1: Write a python node that controls the robot to put all the golden boxes together.

Some hints:
- you can use the code (token.info.code) associated to each marker to know what are the boxes that have been already paired;
- you can reuse, maybe modiyfing them a little bit, the functions that you have developed during the exercises.

Solution:
	- 1) find and grab the closest golden token
	- 2) move the token to the center
	- 3) find another golden token that hasn't been moved yet
	- 4) move the token to the center by locating the first token 
	- 5) start again from task 3 until all tokens are moved to the center

"""

# Class Robot
R = Robot()

# Array for collecting the token codes
collected_tokens = []

# Max number of tokens
all_tokens = 6

# Starting status
m = 0
n = 0

# Case 1 and 2
case1 = 1
case2 = 2

"""
FUNCTIONS

"""
# Function for setting linear velocity
def drive(speed, seconds):
	# Speeds for both motors (wheels)
	R.motors[0].m0.power = speed
	R.motors[0].m1.power = speed
	# For how long the robot is moving
	time.sleep(seconds)
	# Stopping motors
	R.motors[0].m0.power = 0
	R.motors[0].m1.power = 0
	
# Function for setting angular velocity
def turn(speed, seconds):
	# Speeds for both motors (wheels)
	R.motors[0].m0.power = speed
	R.motors[0].m1.power = -speed
	# For how long the robot is moving
	time.sleep(seconds)
	# Stopping motors
	R.motors[0].m0.power = 0
	R.motors[0].m1.power = 0
	
# Function to find the closest token
def find_token(collected_tokens):
	"""
	Returns:
		dist (float): distance of the closest token (returns -1 if no token is detected)
		rot_y (float): angle between the robot and the token (returns -1 if no token is detected)
		code (int): the numeric code of the token (returns -1 if no token is detected)
	"""
	# maximum distance where robot can see a token
	dist = 100
	
	for token in R.see(): # R.see() returns list of all the markers the robot can see
		# If token is in distance
		if token.dist < dist and token.info.code not in collected_tokens:
			dist = token.dist
			rot_y = token.rot_y
			code = token.info.code
						
	if dist == 100:
		return -1, -1, -1
	else:
		return dist, rot_y, code
		
# Function to locate the center token
def find_token_center(center_code):
	"""
	Returns:
		dist (float): distance of the center token (returns -1 if center token is not detected)
		rot_y (float): angle between the robot and the center token (returns -1 if center token is not detected)
	"""
	# maximum distance where robot can see a token
	dist = 100
	
	for token in R.see(): # R.see() returns list of all the markers the robot can see
		# If token with center code was detected
		if token.info.code == center_code:
			print("Found the center token!")
			dist = token.dist
			rot_y = token.rot_y		
	if dist == 100:
		return -1, -1
	else:
		return dist, rot_y		
		
def move_token(case, dist, rot_y):

	"""
	Case 1: finding the closest token that has not been moved yet
	Case 2: finding the center token

	"""
	# Thresholds for orentation and distance of the token for robot to grab it
	angle_th = 2.0
	distance_th = 0.4
	# Threshold of the token for robot to release it
	center_dist = 0.6
	
	# Token is too far or already moved it
	if dist == -1:
		# Search for another token	
		print("I don't see token! Locating...")
		turn(-15, 1)
		
	# If token is in the distance threshold and robot can grab or release it
	elif dist < distance_th and case == 1:	
		return 1
	
	elif dist < center_dist and case == 2:	
		return 1			
							
	# If the robot is aligned with the token, angle is in the threshold
	elif -angle_th <= rot_y <= angle_th:
		print("Here we are!")
		drive(30, 0.5)
			
	# If token is found but not well aligned
	# Move left	
	elif rot_y < -angle_th:
		print("Left a bit...")
		turn(-2, 0.5)
	# Move right
	elif rot_y > angle_th:
		print("Right a bit...")
		turn(2, 0.5)					
	
	
while 1:

	#Finding the token parameters
	dist, rot_y, code = find_token(collected_tokens)
	
	# Token is too far or already moved it
	if dist == -1 or code in collected_tokens:
	
		# All tokens are already moved
		if len(collected_tokens) == all_tokens:
			# Exit while loop
			print("Found all tokens!")
			exit()	
		
		# Search for another token	
		print("I don't see any or already moved that token! Locating...")
		turn(-15, 1)
	else:
		print("Found a token not moved before")
		while m != 1:
			dist, rot_y, code = find_token(collected_tokens)
			m = move_token(case1, dist, rot_y)
			
		print("Found it!")
		R.grab()
		m = 0 # reset status
		print("Got it!")
	
		# Assign found token code to the collected tokens
		collected_tokens.append(code)
		print("Codes found so far: " + str(collected_tokens))
			
		# Moving the first token to the center
		if len(collected_tokens) == 1:
			center_code = collected_tokens[0]
			print("Moving the first token to the center")
			turn(-10, 1.2)
			drive(19, 10)
			print("Arrived in the center!")
			R.release()
			print("Released it!")
			print("Backing up..")
			drive(-25, 1) 
			turn(20, 1)
		# Moving the other tokens to the center by locating the first token 	
		else:
			print("Now locating the center token")
			while n != 1:
				dist, rot_y = find_token_center(center_code)
				n = move_token(case2, dist, rot_y)
			
			print("Arrived in the center!")		
			R.release()
			n = 0 # reset status 
			print("Released it!")
			print("Backing up..")
			drive(-25, 1) 
			turn(-20, 1)
			
	
				
