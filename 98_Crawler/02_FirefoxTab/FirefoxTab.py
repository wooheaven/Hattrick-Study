import pyautogui, time

def clickTabOfFireFox(n, isDualMonitor):
	# define position
	x = 130
	if isDualMonitor:
		x += 1920
	y = 37

	# wait
	time.sleep(0.5)

	# move and click
	pyautogui.moveTo(x, y, duration=0.2)
	pyautogui.click()

	# CTRL + TAB * n
	pyautogui.keyDown('ctrl')
	for i in range(n-1):
		time.sleep(0.3)
		pyautogui.press('tab')
	pyautogui.keyUp('ctrl')