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
	moveX = 170
	if isDualMonitor:
		moveX += 1920
	moveY = screenY / 200 * 7

	# wait
	time.sleep(0.5)

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

def clickFacebookLogin():
	# initial region
	moveX, moveY = 484, 405
	if isDualMonitor:
		moveX += 1920

	# move
	pyautogui.moveTo(moveX, moveY, duration=0.15)

	# find faceBookLogin
	faceBookLogin = pyautogui.locateOnScreen('screen-FacebookLogin.png', region=(moveX, moveY, 77, 33), grayscale=True)
	if None == faceBookLogin:
		faceBookLogin = pyautogui.locateOnScreen('screen-FacebookLogin.png')
		if None == faceBookLogin:
			print('1st 2nd faceBookLogin is None')
		else:
			print('2nd faceBookLogin location =', faceBookLogin)
			moveX = faceBookLogin[0] + faceBookLogin[2]/2
			moveY = faceBookLogin[1] + faceBookLogin[3]/2
	else:
		print('1st faceBookLogin location with region =', faceBookLogin)
		moveX = faceBookLogin[0] + faceBookLogin[2]/2
		moveY = faceBookLogin[1] + faceBookLogin[3]/2

	# move and click
	moveAndClick(moveX, moveY)

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
	print('find myClub =', myClub)

	# define position
	moveX = myClub[0] + myClub[2]/2
	moveY = myClub[1] + myClub[3]/2

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(5)

def clickPlayer(y):
	# define position
	moveX = 418
	if isDualMonitor:
		moveX += 1920
	moveY = screenY * y

	# wait
	time.sleep(0.4)

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

def clickFacebookLogout(y):
	# find locateOnScreen
	moveX, moveY = 1258, 338
	if isDualMonitor:
		moveX += 1920

	# move
	pyautogui.moveTo(moveX, moveY, duration=0.15)

	# find faceBookLogin
	faceBookLogout = pyautogui.locateOnScreen('screen-FacebookLogout.png', region=(moveX, moveY, 69, 51), grayscale=True)
	if None == faceBookLogout:
		faceBookLogout = pyautogui.locateOnScreen('screen-FacebookLogout.png')
		if None == faceBookLogout:
			print('1st 2nd faceBookLogin is None')
		else:
			print('2nd faceBookLogout location =', faceBookLogout)
			moveX = faceBookLogout[0] + faceBookLogout[2]/2
			moveY = faceBookLogout[1] + faceBookLogout[3]/2
	else:
		print('1st faceBookLogout location with region =', faceBookLogout)
		moveX = faceBookLogout[0] + faceBookLogout[2]/2
		moveY = faceBookLogout[1] + faceBookLogout[3]/2

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(3)

def moveAndClick(moveX, moveY):
	pyautogui.moveTo(moveX, moveY, duration=0.2)
	pyautogui.click()

def moveScroll(y):
	# wait
	time.sleep(0.5)

	# move scroll
	pyautogui.scroll(y)
