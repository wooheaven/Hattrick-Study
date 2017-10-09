import pyautogui, time
screenX, screenY = pyautogui.size()

def clickTabOfFireFox(n):
	# define position
	moveX = screenX / 100 * 51
	moveY = screenY / 30 * 1

	# wait
	time.sleep(0.5)

	# move and click
	moveAndClick(moveX, moveY)

	# CTRL + TAB * n
	pyautogui.keyDown('ctrl')
	for i in range(n-1):
		time.sleep(0.2)
		pyautogui.press('tab')
	pyautogui.keyUp('ctrl')

def clickEmpty(y):
	# define position
	moveX = screenX / 110 * 66
	moveY = screenY * y

	# wait
	time.sleep(0.3)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(0.3)

def clickFacebookLogin():
	# define position
	moveX = screenX / 110 * 70
	moveY = screenY / 300 * 135

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(12)

def clickMyClub():
	# define position
	moveX = screenX / 140 * 90
	moveY = screenY / 300 * 90

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(3)

def clickMatch():
	# define position
	moveX = screenX / 18 * 11
	moveY = screenY / 3600 * 2285

	# wait
	time.sleep(0.4)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(2)

def clickLastMatch():
	# define position
	moveX = screenX / 180 * 127
	moveY = screenY / 410 * 290

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

def clickHome():
	# define position
	moveX = screenX / 50 * 32
	moveY = screenY / 200 * 53

	# wait
	time.sleep(0.2)

	# move and click
	moveAndClick(moveX, moveY)
	pyautogui.click(clicks=2, interval=0.10)

	# wait
	time.sleep(0.3)

def click02_workspace():
	# define position
	moveX = screenX / 50 * 34
	moveY = screenY / 1000 * 331

	# wait
	time.sleep(0.3)

	# move and click
	moveAndClick(moveX, moveY)
	pyautogui.click(clicks=2, interval=0.10)

	# wait
	time.sleep(0.3)

def click02_Hattrick():
	# define position
	moveX = screenX / 50 * 34
	moveY = screenY / 1000 * 331

	# wait
	time.sleep(0.3)

	# move and click
	moveAndClick(moveX, moveY)
	pyautogui.click(clicks=2, interval=0.10)

	# wait
	time.sleep(0.3)

def clickHattrickStudy():
	# define position
	moveX = screenX / 100 * 68
	moveY = screenY / 200 * 62

	# wait
	time.sleep(0.3)

	# move and click
	moveAndClick(moveX, moveY)
	pyautogui.click(clicks=2, interval=0.10)

	# wait
	time.sleep(0.3)

def click01_LastKeeper():
	# define position
	moveX = screenX / 100 * 68
	moveY = screenY / 200 * 62

	# wait
	time.sleep(0.2)

	# move and click
	moveAndClick(moveX, moveY)
	pyautogui.click(clicks=2, interval=0.10)

	# wait
	time.sleep(0.2)

def click2017():
	# define position
	moveX = screenX / 100 * 68
	moveY = screenY / 200 * 62

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

def clickSave():
	# define position
	moveX = screenX / 1000 * 852
	moveY = screenY / 2000 * 1485
	
	# wait
	time.sleep(0.3)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(0.2)

def clickFacebookLogout():
	# define position
	moveX = screenX / 110 * 92
	moveY = screenY / 300 * 93

	# wait
	time.sleep(0.8)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(3.7)

def clickURL():
	# define position
	moveX = screenX / 110 * 83
	moveY = screenY / 300 * 19

	# wait
	time.sleep(0.3)

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
	pyautogui.moveTo(moveX, moveY, duration=0.15)
	pyautogui.click()

def moveScroll(y):
	# wait
	time.sleep(0.3)

	# move scroll
	pyautogui.scroll(y)
