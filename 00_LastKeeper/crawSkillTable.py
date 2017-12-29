import pyautogui, time
screenX, screenY = pyautogui.size()
if 1920 == screenX and 1080 == screenY:
	isDualMonitor = False
	print('use 1 monitor =', screenX, 'x', screenY, 'isDualMonitor=', isDualMonitor)
else:
	isDualMonitor = True
	print('use 2 monitor =', screenX, 'x', screenY, 'isDualMonitor=', isDualMonitor)

def clickEmpty(y):
	# define position
	moveX = 351
	if isDualMonitor:
		moveX += 1920
	moveY = screenY * y

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
		time.sleep(5)
	print('clickMyClub =', myClub)

	# define position
	moveX = myClub[0] + myClub[2]/2
	moveY = myClub[1] + myClub[3]/2

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(5)

def clickPlayer(x, y):
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
		time.sleep(3)
	print('Player =', player)

	# define position
	moveX = player[0] + player[2]/2
	moveY = player[1] + player[3]/2

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(5)

def clickSkillTable(y):
	# define position
	moveX = 600
	if isDualMonitor:
		moveX += 1920
	moveY = screenY * y

	# wait
	time.sleep(4)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(1)

def clickSince(y):
	# define position
	moveX = 600
	if isDualMonitor:
		moveX += 1920
	moveY = screenY * y

	# wait
	time.sleep(1.1)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(9)

def clickCopy(y):
	# define position
	moveX = 1095
	if isDualMonitor:
		moveX += 1920
	moveY = screenY * y

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(0.5)

def moveAndClick(moveX, moveY):
	pyautogui.moveTo(moveX, moveY, duration=0.2)
	pyautogui.click()

def moveScroll(y):
	# wait
	time.sleep(0.5)

	# move scroll
	pyautogui.scroll(y)