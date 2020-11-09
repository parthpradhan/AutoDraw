import numpy
import pyautogui
import time	  
class AutoDraw(object):
	pyautogui.PAUSE = 0.00
	pyautogui.FAILSAFE = True

	@staticmethod
	def imgLines(image_array: numpy.array, offset:int, rowsleep:int, lowsleep:int) -> None:
		positionx,positiony = pyautogui.position()
		for row in image_array:
			xoffset = 0
			drawing = False
			for value in row:
				if not value.all():
					if drawing == True:
						xoffset += offset
					else:
						start = positionx + xoffset
						drawing = True
						xoffset += offset
				if value.all():
					if drawing == False:
						xoffset += offset
					else:
						pyautogui.moveTo(start,positiony)
						pyautogui.dragTo(positionx + xoffset, positiony, duration=lowsleep, button='left')
						time.sleep(lowsleep)
						drawing = False
						xoffset += offset
			if not value.all():
				if drawing == True:
					pyautogui.moveTo(start,positiony)
					pyautogui.dragTo(positionx + xoffset, positiony, duration=lowsleep, button='left')
					time.sleep(lowsleep)
					xoffset += offset
			positiony += offset
			time.sleep(rowsleep)
			