import pyautogui, time

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

def clickMatch(x, y, isDualMonitor):
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
	moveY = player[1] + player[3]/2 + 23

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(5)

def clickLastMatch(x, y, isDualMonitor):
	# define position
	if isDualMonitor:
		x += 1920

	# wait
	time.sleep(0.8)

	# move and click
	moveAndClick(x, y)

	# wait
	time.sleep(7)

def clickFirefoxFile():
	# define position
	moveX = 91
	if isDualMonitor:
		moveX += 1920
	moveY = 15

	# wait
	time.sleep(1)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(0.3)

def clickSavePageAs():
	# define position
	moveX = 91
	if isDualMonitor:
		moveX += 1920
	moveY = screenY / 100 * 12

	# wait
	time.sleep(0.3)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(0.3)

def typeFileName():
	# wait
	time.sleep(0.4)

	pyautogui.typewrite('match', interval=0.05)

	# wait
	time.sleep(0.3)

def clickRwoo(x,y):
	# define position
	moveX = x
	if isDualMonitor:
		moveX += 1920
	moveY = y

	# wait
	time.sleep(0.2)

	# move and click
	moveAndClick(moveX, moveY)
	pyautogui.click(clicks=2, interval=0.10)

	# wait
	time.sleep(0.3)

def click02_workspace(x,y):
	# define position
	moveX = x
	if isDualMonitor:
		moveX += 1920
	moveY = y

	# wait
	time.sleep(0.3)

	# move and click
	moveAndClick(moveX, moveY)
	pyautogui.click(clicks=2, interval=0.10)

	# wait
	time.sleep(0.3)

def click02_Hattrick(x,y):
	# define position
	moveX = x
	if isDualMonitor:
		moveX += 1920
	moveY = y

	# wait
	time.sleep(0.3)

	# move and click
	moveAndClick(moveX, moveY)
	pyautogui.click(clicks=2, interval=0.10)

	# wait
	time.sleep(0.3)

def clickHattrickStudy(x,y):
	# define position
	moveX = x
	if isDualMonitor:
		moveX += 1920
	moveY = y

	# wait
	time.sleep(0.3)

	# move and click
	moveAndClick(moveX, moveY)
	pyautogui.click(clicks=2, interval=0.10)

	# wait
	time.sleep(0.3)

def click00_LastKeeper(x,y):
	# define position
	moveX = x
	if isDualMonitor:
		moveX += 1920
	moveY = y

	# wait
	time.sleep(0.2)

	# move and click
	moveAndClick(moveX, moveY)
	pyautogui.click(clicks=2, interval=0.10)

	# wait
	time.sleep(0.2)

def click2017(x,y):
	# define position
	moveX = x
	if isDualMonitor:
		moveX += 1920
	moveY = y

	# wait
	time.sleep(0.2)

	# move and click
	moveAndClick(moveX, moveY)
	pyautogui.click(clicks=2, interval=0.10)

	# wait
	time.sleep(0.2)

def clickLastMonth():
	# wait
	time.sleep(0.3)

	# move to last month
	for i in range(10):
		pyautogui.press('down')
	time.sleep(0.2)
	pyautogui.press('enter')

	# wait
	time.sleep(0.2)

def clickLastDay():
	# wait
	time.sleep(0.3)

	# move to last day
	for i in range(10):
		pyautogui.press('down')
	time.sleep(0.2)
	pyautogui.press('enter')
	
	# wait
	time.sleep(0.2)

def clickSave(x,y):
	# define position
	moveX = x
	if isDualMonitor:
		moveX += 1920
	moveY = y
	
	# wait
	time.sleep(0.3)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(1)

def moveAndClick(moveX, moveY):
	pyautogui.moveTo(moveX, moveY, duration=0.15)
	pyautogui.click()

def moveScroll(y):
	# wait
	time.sleep(0.3)

	# move scroll
	pyautogui.scroll(y)
