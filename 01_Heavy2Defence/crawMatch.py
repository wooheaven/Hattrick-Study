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
	moveY = screenY / 100 * 3

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
	moveX = 360
	if isDualMonitor:
		moveX += 1920
	moveY = screenY * y

	# wait
	time.sleep(0.3)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(0.4)

def clickHattrickLogin(y):
	# define position
	moveX = 500
	if isDualMonitor:
		moveX += 1920
	moveY = screenY * y

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

	# define position
	moveY = screenY * (y+(11/200))

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(11.9)

def clickMyClub(y):
	# define position
	moveX = screenX / 140 * 90
	moveY = screenY * y

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(2.5)

def clickMatch(y):
	# define position
	moveX = screenX / 110 * 67
	moveY = screenY * y

	# wait
	time.sleep(0.4)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(2)

def clickLastMatch(y):
	# define position
	moveX, moveY = 779, y
	if isDualMonitor:
		moveX += 1920

	# wait
	time.sleep(0.8)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(5.8)

def clickFirefoxFile():
	# define position
	moveX = screenX / 50 * 26
	moveY = screenY / 70 * 1

	# wait
	time.sleep(0.3)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(0.3)

def clickSavePageAs():
	# define position
	moveX = screenX / 50 * 26
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
	moveX = screenX * x
	moveY = screenY * y

	# wait
	time.sleep(0.2)

	# move and click
	moveAndClick(moveX, moveY)
	pyautogui.click(clicks=2, interval=0.10)

	# wait
	time.sleep(0.3)

def click02_workspace(x,y):
	# define position
	moveX = screenX * x
	moveY = screenY * y

	# wait
	time.sleep(0.3)

	# move and click
	moveAndClick(moveX, moveY)
	pyautogui.click(clicks=2, interval=0.10)

	# wait
	time.sleep(0.3)

def click02_Hattrick(x,y):
	# define position
	moveX = screenX * x
	moveY = screenY * y

	# wait
	time.sleep(0.3)

	# move and click
	moveAndClick(moveX, moveY)
	pyautogui.click(clicks=2, interval=0.10)

	# wait
	time.sleep(0.3)

def clickHattrickStudy(x,y):
	# define position
	moveX = screenX * x
	moveY = screenY * y

	# wait
	time.sleep(0.3)

	# move and click
	moveAndClick(moveX, moveY)
	pyautogui.click(clicks=2, interval=0.10)

	# wait
	time.sleep(0.3)

def click01_Heavy2Defence(x,y):
	# define position
	moveX = screenX * x
	moveY = screenY * y

	# wait
	time.sleep(0.2)

	# move and click
	moveAndClick(moveX, moveY)
	pyautogui.click(clicks=2, interval=0.10)

	# wait
	time.sleep(0.2)

def click2017(x,y):
	# define position
	moveX = screenX * x
	moveY = screenY * y

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
	moveX = screenX * x
	moveY = screenY * y
	
	# wait
	time.sleep(0.3)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(0.2)

def clickLogout(x,y):
	# define position
	moveX = screenX * x
	moveY = screenY * y

	# wait
	time.sleep(0.8)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(3.7)

def clickURL(y):
	# define position
	moveX = screenX / 110 * 73
	moveY = screenY * y

	# wait
	time.sleep(0.3)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(0.3)

	for _ in range(13):
		pyautogui.press('left')
	
	pyautogui.typewrite('92', interval=0.05)
	time.sleep(0.7)
	
	pyautogui.press('enter')
	time.sleep(1.7)

def moveAndClick(moveX, moveY):
	pyautogui.moveTo(moveX, moveY, duration=0.15)
	pyautogui.click()

def moveScroll(y):
	# wait
	time.sleep(0.3)

	# move scroll
	pyautogui.scroll(y)
