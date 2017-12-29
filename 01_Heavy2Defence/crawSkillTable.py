import pyautogui, time
screenX, screenY = pyautogui.size()
if 1920 == screenX and 1080 == screenY:
	isDualMonitor = False
	print('use 1 monitor =', screenX, 'x', screenY, 'isDualMonitor=', isDualMonitor)
else:
	isDualMonitor = True
	print('use 2 monitor =', screenX, 'x', screenY, 'isDualMonitor=', isDualMonitor)

def clickTabOfFireFox(n):
	# define position
	moveX = 150
	if isDualMonitor:
		moveX += 1920
	moveY = screenY / 200 * 7

	# wait
	time.sleep(0.2)

	# move and click
	moveAndClick(moveX, moveY)

	# CTRL + TAB * n
	pyautogui.keyDown('ctrl')
	for i in range(n-1):
		time.sleep(0.25)
		pyautogui.press('tab')
	pyautogui.keyUp('ctrl')

def clickEmpty(y):
	# define position
	moveX = 350
	if isDualMonitor:
		moveX += 1920
	moveY = y

	# wait
	time.sleep(0.4)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(0.4)

def clickMyClub(x, y):
	# wait
	time.sleep(10)

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
		time.sleep(2)
		if(None == myClub):
			myClub = pyautogui.locateOnScreen('screen-MyClub.png')
		time.sleep(2)
	print('clickMyClub =', myClub)

	# define position
	moveX = myClub[0] + myClub[2]/2
	moveY = myClub[1] + myClub[3]/2

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(5)

def clickPlayer(x, y):
	# initial position
	moveX,moveY  = x, y
	if isDualMonitor:
		moveX += 1920
	print('clickPlayer =', moveX, moveY)

	# move
	pyautogui.moveTo(moveX, moveY, duration=0.15)

	# wait
	time.sleep(1)

	# find player
	player = pyautogui.locateOnScreen('screen-player.png', region=(moveX, moveY, 105, 66), grayscale=True)
	if None == player:
		player = pyautogui.locateOnScreen('screen-player.png')
		if None == player:
			print('1st 2nd player is None')
		else:
			print('2nd player location =', player)
			moveX = player[0] + player[2]/2
			moveY = player[1] + player[3]/2
	else:
		print('1st player location with region=', player)
		moveX = player[0] + player[2]/2
		moveY = player[1] + player[3]/2

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(3)

def clickSkillTable(x, y):
	# define position
	moveX, moveY = x, y
	if isDualMonitor:
		moveX += 1920
	print('clickSkillTable =', moveX, moveY)

	# move and click
	moveAndClick(moveX, moveY)

def clickSince(x, y):
	# initial position
	moveX,moveY  = x, y
	if isDualMonitor:
		moveX += 1920

	# move
	pyautogui.moveTo(moveX, moveY, duration=0.15)

	# wait
	time.sleep(2)

	# find Since
	since = None
	while(None == since):
		since = pyautogui.locateOnScreen('screen-Since.png', region=(moveX, moveY, 168, 25), grayscale=True)
		time.sleep(1.5)
		if(None == since):
			since = pyautogui.locateOnScreen('screen-Since.png')
		time.sleep(1.5)
	moveX = since[0] + since[2]/2
	moveY = since[1] + since[3]/2
	print('clickSince =', since)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(3)

def clickCopy(x, y):
	# define position
	moveX = x
	if isDualMonitor:
		moveX += 1920
	moveY = y
	print('clickCopy =', moveX, moveY)

	# wait
	time.sleep(1)

	# move and click
	moveAndClick(moveX, moveY)

def moveAndClick(moveX, moveY):
	pyautogui.moveTo(moveX, moveY, duration=0.2)
	pyautogui.click()

def moveScroll(y):
	# wait
	time.sleep(0.09)
	
	# move scroll
	pyautogui.scroll(y)

	# wait
	time.sleep(0.09)
