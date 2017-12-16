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

def clickHattrickLogin(x, y):
	# define position
	moveX, moveY = x, y
	if isDualMonitor:
		moveX += 1920

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(0.7)

	# delete previous id
	for _ in range(30):
		pyautogui.press('delete')
		pyautogui.press('blackspace')

	# type id
	pyautogui.typewrite('heavy2defence', interval=0.05)

	# wait
	time.sleep(0.7)

	# next cell
	pyautogui.press('tab')

	# wait
	time.sleep(0.7)

	# type password
	pyautogui.typewrite('h1324d3546', interval=0.05)

	# wait
	time.sleep(0.7)

	# Login
	pyautogui.press('tab')
	pyautogui.press('enter')

	# wait
	time.sleep(11.9)

def clickMyClub(y):
	# define position
	moveX, moveY = 550, y
	if isDualMonitor:
		moveX += 1920

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(2.5)

def clickPlayer(x, y):
	# initial position
	moveX,moveY  = x, y
	if isDualMonitor:
		moveX += 1920

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

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(0.4)

def clickSince(y):
	# define position
	moveX = screenX / 100 * 32
	if isDualMonitor:
		moveX += 1920
	moveY = screenY * y

	# wait
	time.sleep(3.5)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(7.5)

def clickCopy(y):
	# define position
	moveX = screenX / 100 * 57
	if isDualMonitor:
		moveX += 1920
	moveY = screenY * y

	# wait
	time.sleep(1)

	# move and click
	moveAndClick(moveX, moveY)

def clickHattrickLogout(y):
	# define position
	moveX, moveY = 1258, screenY * y
	if isDualMonitor:
		moveX += 1920

	# wait
	time.sleep(0.5)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(8.4)

def clickFacebookLogout(y):
	# find locateOnScreen
	moveX, moveY = 1260, 338
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
	time.sleep(0.09)
	
	# move scroll
	pyautogui.scroll(y)

	# wait
	time.sleep(0.09)
