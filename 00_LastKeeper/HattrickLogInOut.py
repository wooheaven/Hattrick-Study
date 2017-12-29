import pyautogui, time
screenX, screenY = pyautogui.size()
if 1920 == screenX and 1080 == screenY:
	isDualMonitor = False
	print('use 1 monitor =', screenX, 'x', screenY, 'isDualMonitor=', isDualMonitor)
else:
	isDualMonitor = True
	print('use 2 monitor =', screenX, 'x', screenY, 'isDualMonitor=', isDualMonitor)

def clickFacebookLogin(x, y):
	# initial region
	moveX, moveY = x, y
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
	pyautogui.moveTo(moveX, moveY, duration=0.2)
	pyautogui.click()

	# wait
	time.sleep(12)

def clickFacebookLogout(x, y):
	# find locateOnScreen
	moveX, moveY = x, y
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
	pyautogui.moveTo(moveX, moveY, duration=0.2)
	pyautogui.click()

	# wait
	time.sleep(3)