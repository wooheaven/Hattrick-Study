import pyautogui, time
screenX, screenY = pyautogui.size()

def clickTabOfFireFox(n):
	# define position
	moveX = screenX / 100 * 53
	moveY = screenY / 30 * 1

	# wait
	time.sleep(0.2)

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
	moveX = screenX / 110 * 65
	moveY = screenY * y

	# wait
	time.sleep(0.3)

	# move and click
	moveAndClick(moveX, moveY)

def clickHattrickLogin(y):
	# define position
	moveX = screenX / 1100 * 693
	moveY = screenY * y

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(0.7)
	
	# type id
	pyautogui.typewrite('heavy2defence', interval=0.05)
	
	# wait
	time.sleep(0.7)
	
	# define position
	moveY = screenY * (y+(11/300))
	
	# move and click
	moveAndClick(moveX, moveY)
	
	# wait
	time.sleep(0.7)
	
	# type password
	pyautogui.typewrite('h1324d3546', interval=0.05)
	
	# wait
	time.sleep(0.7)
	
	# define position
	moveY = screenY * (y+(14/300))

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

def clickPlayer(y):
	# define position
	moveX = screenX / 110 * 67
	moveY = screenY * y

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(2)

def clickSkillTable(y):
	# define position
	moveX = screenX / 1400 * 932
	moveY = screenY * y

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(0.4)

def clickSince(y):
	# define position
	moveX = screenX / 1200 * 821
	moveY = screenY * y
	
	# wait
	time.sleep(3.5)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(7.5)

def clickCopy(y):
	# define position
	moveX = screenX / 1400 * 1099
	moveY = screenY * y

	# wait
	time.sleep(1)
	
	# move and click
	moveAndClick(moveX, moveY)

def clickHattrickLogout(y):
	# define position
	moveX = screenX / 1100 * 915
	moveY = screenY * y

	# wait
	time.sleep(0.5)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(8.4)

def clickURL(y):
	# define position
	moveX = screenX / 110 * 66
	moveY = screenY * y

	# wait
	time.sleep(0.1)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(0.1)

	for _ in range(13):
		pyautogui.press('left')
	
	pyautogui.typewrite('91', interval=0.05)
	time.sleep(0.6)
	
	pyautogui.press('enter')
	time.sleep(1.6)

def moveAndClick(moveX, moveY):
	pyautogui.moveTo(moveX, moveY, duration=0.2)
	pyautogui.click()

def moveScroll(y):
	# wait
	time.sleep(0.09)
	
	# move scroll
	pyautogui.scroll(y)

	# wait
	time.sleep(0.09)
