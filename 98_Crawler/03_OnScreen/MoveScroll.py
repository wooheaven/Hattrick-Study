import pyautogui, time

def moveScroll(y):
	# wait
	time.sleep(0.2)

	# move scroll
	pyautogui.scroll(y)