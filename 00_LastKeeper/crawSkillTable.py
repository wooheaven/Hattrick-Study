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
	moveX = screenX / 100 * 3
	if isDualMonitor:
		moveX += 1920
	moveY = screenY / 100 * 3

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
	moveX = screenX / 100 * 18
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
	# find locateOnScreen
	moveX, moveY = 484, 405
	if isDualMonitor:
		moveX += 1920
	pyautogui.moveTo(moveX, moveY, duration=0.15)

	faceBookLogin = pyautogui.locateOnScreen('screen-FacebookLogin.png', region=(moveX, moveY, 77, 33), grayscale=True)
	print('1st faceBookLogin location with region =', faceBookLogin)
	if None == faceBookLogin:
		faceBookLogin = pyautogui.locateOnScreen('screen-FacebookLogin.png')
		print('2nd faceBookLogin location =', faceBookLogin)
		faceBookLogin = pyautogui.locateCenterOnScreen('screen-FacebookLogin.png')
		print('2nd faceBookLogin location of Center =', faceBookLogin)
	else:
		faceBookLogin = pyautogui.locateCenterOnScreen('screen-FacebookLogin.png', region=(moveX, moveY, 77, 33), grayscale=True)
		print('1st faceBookLogin location of Center with region =', faceBookLogin)

	moveX = faceBookLogin[0]
	moveY = faceBookLogin[1]
	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(12)

def clickMyClub(y):
	# define position
	moveX = screenX / 100 * 29
	if isDualMonitor:
		moveX += 1920
	moveY = screenY * y

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(2.2)

def clickPlayer(y):
	# define position
	moveX = screenX / 100 * 22
	if isDualMonitor:
		moveX += 1920
	moveY = screenY * y

	# wait
	time.sleep(0.4)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(2.5)

def clickSkillTable(y):
	# define position
	moveX = screenX / 100 * 32
	if isDualMonitor:
		moveX += 1920
	moveY = screenY * y

	# wait
	time.sleep(2)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(1)

def clickSince(y):
	# define position
	moveX = screenX / 100 * 32
	if isDualMonitor:
		moveX += 1920
	moveY = screenY * y

	# wait
	time.sleep(1.1)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(8.5)

def clickCopy(y):
	# define position
	moveX = screenX / 100 * 57
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

	pyautogui.moveTo(moveX, moveY, duration=0.15)
	
	faceBookLogout = pyautogui.locateOnScreen('screen-FacebookLogout.png', region=(moveX, moveY, 69, 51), grayscale=True)
	print('1st faceBookLogout location with region =', faceBookLogout)
	if None == faceBookLogout:
		faceBookLogout = pyautogui.locateOnScreen('screen-FacebookLogout.png')
		print('2nd faceBookLogout location =', faceBookLogout)
		faceBookLogout = pyautogui.locateCenterOnScreen('screen-FacebookLogout.png')
		print('2nd faceBookLogout location of Center =', faceBookLogout)
	else:
		faceBookLogout = pyautogui.locateCenterOnScreen('screen-FacebookLogout.png', region=(moveX, moveY, 69, 51), grayscale=True)
		print('1st faceBookLogout location of Center with region =', faceBookLogout)

	# define position
	moveX = faceBookLogout[0]
	moveY = faceBookLogout[1]

	# wait
	time.sleep(0.5)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(3)

def clickURL(y):
	# define position
	moveX = screenX / 100 * 25
	if isDualMonitor:
		moveX += 1920
	moveY = screenY * y

	# wait
	time.sleep(0.35)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(0.3)

	for _ in range(13):
		pyautogui.press('left')
	
	pyautogui.typewrite('74', interval=0.05)
	time.sleep(0.7)
	
	pyautogui.press('enter')
	time.sleep(1.7)

def moveAndClick(moveX, moveY):
	pyautogui.moveTo(moveX, moveY, duration=0.2)
	pyautogui.click()

def moveScroll(y):
	# wait
	time.sleep(0.5)

	# move scroll
	pyautogui.scroll(y)
