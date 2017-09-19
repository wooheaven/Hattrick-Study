import pyautogui, time
screenX, screenY = pyautogui.size()

def whereIsMouse():
	currentMouseX, currentMouseY = pyautogui.position()
	print("(" + str(currentMouseX) + "," + str(currentMouseY) + ") / (" + str(screenX) + "," + str(screenY) + ")")

def clickTabOfFireFox(n):
	# define position of FireFox's 1st tab
	moveX = screenX / 100 * 51
	moveY = screenY / 30 * 1

	# move and click
	moveAndClick(moveX, moveY)

	# CTRL + TAB * n
	pyautogui.keyDown('ctrl')
	for i in range(n-1):
		time.sleep(0.1)
		pyautogui.press('tab')
	pyautogui.keyUp('ctrl')

def clickEmpty(y):
	# define position of empty
	moveX = screenX / 110 * 65
	moveY = screenY * y

	# move and click
	moveAndClick(moveX, moveY)

def clickFacebookLogin():
	# define position of Hattrick's Login
	moveX = screenX / 110 * 70
	moveY = screenY / 300 * 135

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(12)

def clickMyClub():
	# define position of Hattrick's Login
	moveX = screenX / 140 * 90
	moveY = screenY / 300 * 90

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(2.5)

def clickPlayer():
	# define position of Hattrick's Login
	moveX = screenX / 110 * 67
	moveY = screenY / 300 * 183

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(2.5)

def clickSkillTable():
	# define position of Hattrick's Login
	moveX = screenX / 1400 * 1102
	moveY = screenY / 300 * 155

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(3.8)

def clickSince(y):
	# define position of Hattrick's Login
	moveX = screenX / 1200 * 831
	moveY = screenY * y

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(4)
	

def moveAndClick(moveX, moveY):
	pyautogui.moveTo(moveX, moveY, duration=0.2)
	pyautogui.click()

def moveScroll(y):
	pyautogui.scroll(y)
