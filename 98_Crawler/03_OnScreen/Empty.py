import pyautogui, time

def clickEmpty(y, isDualMonitor):
	# define position
	x = 300
	if isDualMonitor:
		x += 1920

	# wait
	time.sleep(0.4)

	# move and click
	pyautogui.moveTo(x, y, duration=0.2)
	pyautogui.click()

	# wait
	time.sleep(0.4)