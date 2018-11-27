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
