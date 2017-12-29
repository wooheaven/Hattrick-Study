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
	if isDualMonitor:
		x += 1920

	# move
	pyautogui.moveTo(x, y, duration=0.15)

	# find faceBookLogin
	faceBookLogin = pyautogui.locateOnScreen('screen-FacebookLogin.png', region=(x, y, 77, 33), grayscale=True)
	if None == faceBookLogin:
		faceBookLogin = pyautogui.locateOnScreen('screen-FacebookLogin.png')
		if None == faceBookLogin:
			print('1st 2nd faceBookLogin is None')
		else:
			print('2nd faceBookLogin location =', faceBookLogin)
			x = faceBookLogin[0] + faceBookLogin[2]/2
			y = faceBookLogin[1] + faceBookLogin[3]/2
	else:
		print('1st faceBookLogin location with region =', faceBookLogin)
		x = faceBookLogin[0] + faceBookLogin[2]/2
		y = faceBookLogin[1] + faceBookLogin[3]/2

	# move and click
	pyautogui.moveTo(x, y, duration=0.2)
	pyautogui.click()

	# wait
	time.sleep(12)

def clickHattrickLogin(x, y):
	# define position
	if isDualMonitor:
		x += 1920

	# move and click
	pyautogui.moveTo(x, y, duration=0.2)
	pyautogui.click()

	# wait
	time.sleep(0.7)

	# delete previous id
	pyautogui.click(clicks=2)
	pyautogui.press('delete')
	pyautogui.press('blackspace')

	# type id
	pyautogui.typewrite('heavy2defence', interval=0.07)

	# wait
	time.sleep(0.7)

	# next cell
	pyautogui.press('tab')

	# wait
	time.sleep(0.7)

	# type password
	pyautogui.typewrite('h1324d3546', interval=0.07)

	# wait
	time.sleep(0.7)

	# Login
	y += 55
	pyautogui.moveTo(x, y, duration=0.25)
	pyautogui.click()
	
	# wait
	time.sleep(5)

def clickFacebookLogout(x, y):
	# find locateOnScreen
	if isDualMonitor:
		x += 1920

	# move
	pyautogui.moveTo(x, y, duration=0.15)

	# find faceBookLogin
	faceBookLogout = pyautogui.locateOnScreen('screen-FacebookLogout.png', region=(x, y, 69, 51), grayscale=True)
	if None == faceBookLogout:
		faceBookLogout = pyautogui.locateOnScreen('screen-FacebookLogout.png')
		if None == faceBookLogout:
			print('1st 2nd faceBookLogin is None')
		else:
			print('2nd faceBookLogout location =', faceBookLogout)
			x = faceBookLogout[0] + faceBookLogout[2]/2
			y = faceBookLogout[1] + faceBookLogout[3]/2
	else:
		print('1st faceBookLogout location with region =', faceBookLogout)
		x = faceBookLogout[0] + faceBookLogout[2]/2
		y = faceBookLogout[1] + faceBookLogout[3]/2

	# move and click
	pyautogui.moveTo(x, y, duration=0.2)
	pyautogui.click()

	# wait
	time.sleep(3)

def clickHattrickLogout(x, y):
	# define position
	if isDualMonitor:
		x += 1920

	# wait
	time.sleep(0.5)

	# move and click
	pyautogui.moveTo(x, y, duration=0.2)
	pyautogui.click()

	# wait
	time.sleep(8.4)
