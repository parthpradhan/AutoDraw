import time
import sys
import os
from easygui import multenterbox

cwd = os.getcwd()
sys.path.append(cwd+'/src')

from imageadjust import ImageAdjust
from autodraw import AutoDraw

app = "paint"

os.chdir("art")

imgname = ImageAdjust.get_image()
adjust = ImageAdjust(imgname)
message = "Resizevalue: Image Size(in pixels)\nOffset: Choose 1 for original size"
value, offset = multenterbox(message,"Autodraw", ["Resizevalue","Offset"])
value = int(value) if value else 100
offset = int(offset) if offset else 1
value = value / offset
adjust.convert_image()
adjust.resize(value)
adjust.im.show()
lowsleep = 0.005
rowsleep = 0.025
option = None
while option == None:
	print("Press >enter< to begin 5 second countdown,\nPress >p< to close the program.")
	option = input()
	if option == 'p':
		exit()
	if option == 'i':
		adjust.invert(imgname)
		adjust.convert_image()
		value = value / offset
		adjust.resize(value)
		adjust.im.show()
		option = None

time.sleep(5)
array = adjust.update_array()
AutoDraw.imgLines(array, offset, rowsleep, lowsleep)

end = input("Press any key to exit")
exit()

