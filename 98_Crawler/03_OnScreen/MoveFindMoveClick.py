import pyautogui, time

def moveByImage(x, y, rowSize, colSize, isDualMonitor, fileName):
	moveByImageWithModify(x, y, 0, 0, rowSize, colSize, isDualMonitor, fileName)

def moveByImageWithModify(x, y, modifyX, modifyY, rowSize, colSize, isDualMonitor, fileName):
	# modify isDual
	if isDualMonitor:
		x += 1920

	# move
	pyautogui.moveTo(x, y, duration=0.15)

	# find myTarget
	myTarget = None
	while(None == myTarget):
		myTarget = pyautogui.locateOnScreen(fileName, region=(x, y, rowSize, colSize), grayscale=True)
		time.sleep(2.5)
		if(None == myTarget):
			print('re find')
			myTarget = pyautogui.locateOnScreen(fileName)
		time.sleep(2.5)

	# define position
	x = myTarget[0] + myTarget[2]/2 + modifyX
	y = myTarget[1] + myTarget[3]/2 + modifyY

	# myTarget
	if isDualMonitor:
		print(fileName, 'location on Screen (', myTarget[0] - 1920, myTarget[1], myTarget[2], myTarget[3], ')')
	else:
		print(fileName, 'location on Screen', myTarget)

	# move and click
	pyautogui.moveTo(x, y, duration=0.2)
	pyautogui.click()

	# wait
	time.sleep(5)
