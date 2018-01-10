import pyautogui, time

def typeFileName():
	# wait
	time.sleep(0.5)

	pyautogui.typewrite('match', interval=0.05)

	# wait
	time.sleep(0.3)

def clickRwoo(x,y, isDualMonitor):
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

def click02_workspace(x,y, isDualMonitor):
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

def click02_Hattrick(x,y, isDualMonitor):
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

def clickHattrickStudy(x,y, isDualMonitor):
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

def click00_LastKeeper(x,y, isDualMonitor):
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

def moveAndClick(x, y, isDualMonitor):
	if isDualMonitor:
		x += 1920

	pyautogui.moveTo(x, y, duration=0.15)
	pyautogui.click()

def moveScroll(y):
	# wait
	time.sleep(0.3)

	# move scroll
	pyautogui.scroll(y)
