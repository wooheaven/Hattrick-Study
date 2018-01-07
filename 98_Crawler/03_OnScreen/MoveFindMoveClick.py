import pyautogui, time

def moveByImage(x, y, rowSize, colSize, isDualMonitor, fileName):
	# initial region
	if isDualMonitor:
		x += 1920

	# move
	pyautogui.moveTo(x, y, duration=0.15)

	# find myClub
	myClub = None
	while(None == myClub):
		myClub = pyautogui.locateOnScreen(fileName, region=(x, y, rowSize, colSize), grayscale=True)
		time.sleep(2.5)
		if(None == myClub):
			myClub = pyautogui.locateOnScreen(fileName)
		time.sleep(2.5)
	print(fileName, myClub)

	# define position
	x = myClub[0] + myClub[2]/2
	y = myClub[1] + myClub[3]/2

	# move and click
	pyautogui.moveTo(x, y, duration=0.2)
	pyautogui.click()

	# wait
	time.sleep(5)
