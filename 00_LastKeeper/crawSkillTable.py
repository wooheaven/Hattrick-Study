import pyautogui, time
screenX, screenY = pyautogui.size()

def whereIsMouse():
	currentMouseX, currentMouseY = pyautogui.position()
	print("(" + str(currentMouseX) + "," + str(currentMouseY) + ") / (" + str(screenX) + "," + str(screenY) + ")")

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
	time.sleep(0.4)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(0.4)

def clickFacebookLogin():
	# define position
	moveX = screenX / 110 * 70
	moveY = screenY / 300 * 117

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
	time.sleep(2.2)

def clickPlayer():
	# define position
	moveX = screenX / 110 * 67
	moveY = screenY / 300 * 183

	# wait
	time.sleep(0.4)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(2.5)

def clickSkillTable():
	# define position
	moveX = screenX / 1400 * 1102
	moveY = screenY / 300 * 155

	# wait
	time.sleep(2)
	
	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(1)

def clickSince(y):
	# define position
	moveX = screenX / 1200 * 831
	moveY = screenY * y

	# wait
	time.sleep(1.1)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(8.5)

def clickCopy():
	# define position
	moveX = screenX / 1400 * 1100
	moveY = screenY / 310 * 80

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(0.5)

def clickFacebookLogout():
	# define position
	moveX = screenX / 110 * 92
	moveY = screenY / 300 * 93

	# wait
	time.sleep(0.5)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(3)

def clickURL():
	# define position
	moveX = screenX / 110 * 77
	moveY = screenY / 300 * 19

	# wait
	time.sleep(0.35)

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
	pyautogui.moveTo(moveX, moveY, duration=0.2)
	pyautogui.click()

def moveScroll(y):
	# wait
	time.sleep(0.5)

	# move scroll
	pyautogui.scroll(y)
