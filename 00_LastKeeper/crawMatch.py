import pyautogui, time

def clickEmpty(y):
	# define position
	moveX = 356
	if isDualMonitor:
		moveX += 1920
	moveY = screenY * y

	# wait
	time.sleep(0.4)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(0.5)

def clickMyClub(y):
	# define position
	moveX = 550
	if isDualMonitor:
		moveX += 1920
	moveY = screenY * y

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(2.2)

def clickMatch(y):
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
	time.sleep(6)

def clickLastMatch(y):
	# define position
	moveX = 795
	if isDualMonitor:
		moveX += 1920
	moveY = screenY * y

	# wait
	time.sleep(0.8)

	# move and click
	moveAndClick(moveX, moveY)

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
