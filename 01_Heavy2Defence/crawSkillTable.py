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
	moveX = 430
	if isDualMonitor:
		moveX += 1920
	moveY = screenY * y

	# wait
	time.sleep(0.4)

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
	moveX = screenX / 100 * 29
	if isDualMonitor:
		moveX += 1920
	moveY = screenY * y

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(2.5)

def clickPlayer(y):
	# define position
	moveX = screenX / 100 * 22
	if isDualMonitor:
		moveX += 1920
	moveY = screenY * y

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(2)

def clickSkillTable(y):
	# define position
	moveX = screenX / 100 * 32
	if isDualMonitor:
		moveX += 1920
	moveY = screenY * y

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(0.4)

def clickSince(y):
	# define position
	moveX = screenX / 100 * 32
	if isDualMonitor:
		moveX += 1920
	moveY = screenY * y

	# wait
	time.sleep(3.5)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(7.5)

def clickCopy(y):
	# define position
	moveX = screenX / 100 * 57
	if isDualMonitor:
		moveX += 1920
	moveY = screenY * y

	# wait
	time.sleep(1)

	# move and click
	moveAndClick(moveX, moveY)

def clickHattrickLogout(y):
	# define position
	moveX, moveY = 1258, screenY * y
	if isDualMonitor:
		moveX += 1920

	# wait
	time.sleep(0.5)

	# move and click
	moveAndClick(moveX, moveY)

	# wait
	time.sleep(8.4)

def clickURL(y):
	# define position
	moveX = screenX / 100 * 25
	if isDualMonitor:
		moveX += 1920
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
