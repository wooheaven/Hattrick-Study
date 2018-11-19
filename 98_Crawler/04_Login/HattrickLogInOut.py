import pyautogui, time


def clickHattrickLogin2(x, y, isDualMonitor):
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
	pyautogui.typewrite('woosky', interval=0.07)

	# wait
	time.sleep(0.7)

	# next cell
	pyautogui.press('tab')

	# wait
	time.sleep(0.7)

	# type password
	pyautogui.typewrite('12qwaszx', interval=0.07)

	# wait
	time.sleep(0.7)

	# Login
	pyautogui.press('tab')
	pyautogui.press('enter')

	time.sleep(6)

def clickHattrickLogin(x, y, isDualMonitor):
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
	pyautogui.press('tab')
	pyautogui.press('enter')

	# wait
	time.sleep(6)

def clickFacebookLogout(x, y, isDualMonitor):
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
			print('1st 2nd faceBookLogout is None')
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

def clickHattrickLogout(x, y, isDualMonitor):
	# define position
	if isDualMonitor:
		x += 1920

	# wait
	time.sleep(0.5)

	# move and click
	pyautogui.moveTo(x, y, duration=0.2)
	pyautogui.click()

	# wait
	time.sleep(3)
