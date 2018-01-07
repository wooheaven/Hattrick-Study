import pyautogui, time

def clickSkillTable(y, isDualMonitor):
	# define position
	x = 600
	if isDualMonitor:
		x += 1920

	# wait
	time.sleep(4)

	# move and click
	moveAndClick(x, y)
	print('SkilTable =', x, y)

	# wait
	time.sleep(1)

def clickSince(x, y, isDualMonitor):
	# initial position
	if isDualMonitor:
		x += 1920

	# move
	pyautogui.moveTo(x, y, duration=0.15)

	# wait
	time.sleep(2)

	# find Since
	since = None
	while(None == since):
		since = pyautogui.locateOnScreen('screen-Since.png', region=(x, y, 168, 25), grayscale=True)
		time.sleep(1.5)
		if(None == since):
			since = pyautogui.locateOnScreen('screen-Since.png')
		time.sleep(1.5)
	x = since[0] + since[2]/2
	y = since[1] + since[3]/2
	print('clickSince =', since)

	# move and click
	moveAndClick(x, y)

	# wait
	time.sleep(3)

def clickCopy(x, y, isDualMonitor):
	# define position
	if isDualMonitor:
		x += 1920
	print('clickCopy =', x, y)

	# wait
	time.sleep(1)

	# move and click
	moveAndClick(x, y)

def moveAndClick(moveX, moveY):
	pyautogui.moveTo(moveX, moveY, duration=0.2)
	pyautogui.click()