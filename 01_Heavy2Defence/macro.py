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

def clickHattrickLogin():
	# define position of Hattrick's Login
	moveX = screenX / 1100 * 693
	moveY = screenY / 300 * 119

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(12)


def moveAndClick(moveX, moveY):
	pyautogui.moveTo(moveX, moveY, duration=0.2)
	pyautogui.click()

def moveScroll(y):
	pyautogui.scroll(y)
