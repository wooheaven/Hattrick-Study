import pyautogui

def getIsDualMonitor():
	screenX, screenY = pyautogui.size()
	if 1920 == screenX and 1080 == screenY:
		isDualMonitor = False
		print('use 1 monitor =', screenX, 'x', screenY, 'isDualMonitor=', isDualMonitor)
	else:
		isDualMonitor = True
		print('use 2 monitor =', screenX, 'x', screenY, 'isDualMonitor=', isDualMonitor)
	return isDualMonitor