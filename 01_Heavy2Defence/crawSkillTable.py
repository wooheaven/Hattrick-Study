import pyautogui, time

def clickEmpty(y, isDualMonitor):
	# define position
	x = 300
	if isDualMonitor:
		x += 1920

	# wait
	time.sleep(0.4)

	# move and click
	moveAndClick(x, y)

	# wait
	time.sleep(0.4)

def clickMyClub(x, y, isDualMonitor):
	# initial region
	moveX, moveY = x, y
	if isDualMonitor:
		moveX += 1920

	# move
	pyautogui.moveTo(moveX, moveY, duration=0.15)

	# find myClub
	myClub = None
	while(None == myClub):
		myClub = pyautogui.locateOnScreen('screen-MyClub.png', region=(moveX, moveY, 77, 42), grayscale=True)
		time.sleep(2.5)
		if(None == myClub):
			myClub = pyautogui.locateOnScreen('screen-MyClub.png')
		time.sleep(2.5)
	print('clickMyClub =', myClub)

	# define position
	moveX = myClub[0] + myClub[2]/2
	moveY = myClub[1] + myClub[3]/2

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(5)

def clickPlayer(x, y, isDualMonitor):
	# initial region
	moveX, moveY = x, y
	if isDualMonitor:
		moveX += 1920

	# move
	pyautogui.moveTo(moveX, moveY, duration=0.15)

	# find Player
	player = None
	while(None == player):
		player = pyautogui.locateOnScreen('screen-Player.png', region=(moveX, moveY, 72, 59), grayscale=True)
		time.sleep(2.5)
		if(None == player):
			player = pyautogui.locateOnScreen('screen-Player.png')
		time.sleep(2.5)
	print('Player =', player)

	# define position
	moveX = player[0] + player[2]/2
	moveY = player[1] + player[3]/2

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(5)

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

def moveScroll(y):
	# wait
	time.sleep(0.09)

	# move scroll
	pyautogui.scroll(y)