import pyautogui, time

def typeFileName():
	# wait
	time.sleep(0.5)

	pyautogui.typewrite('match', interval=0.05)

	# wait
	time.sleep(0.3)

def clickLastMonthOrDay():
	# wait
	time.sleep(0.3)

	# move to last month
	for i in range(10):
		pyautogui.press('down')
		time.sleep(0.2)
	pyautogui.press('enter')

	# wait
	time.sleep(0.2)

def clickSave(x,y):
	# define position
	if isDualMonitor:
		x += 1920

	# wait
	time.sleep(0.3)

	# move and click
	moveAndClick(x, y)

	# wait
	time.sleep(1)

def moveAndClick(x, y, isDualMonitor):
	moveAndClicks(x, y, isDualMonitor, 1)

def moveAndClicks(x, y, isDualMonitor, clicks):
	if isDualMonitor:
		x += 1920

	pyautogui.moveTo(x, y, duration=0.10)
	pyautogui.click(clicks=clicks, interval=0.10)
