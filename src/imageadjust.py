from PIL import Image, ImageFilter, ImageOps
import numpy as np
from easygui import fileopenbox

class ImageAdjust(object):
	def __init__(self,image):
		self.im = Image.open(image)

	@staticmethod
	def get_image() -> str:
		path = fileopenbox()
		return path

	def convert_image(self) -> None:
		self.im = self.im.convert(mode='1',dither=None)

	def invert(self,image) -> None:
		self.im = ImageOps.invert(Image.open(image))

	def resize(self,value:int) -> None:
		hsize, vsize = self.im.size
		if hsize > vsize:
			cfactor = hsize / value
			self.im = self.im.resize((int(hsize / cfactor), int(vsize / cfactor)))
		else:
			cfactor = vsize / value
			self.im = self.im.resize((int(hsize / cfactor), int(vsize / cfactor)))

	def update_array(self) -> np.array:
		array = np.array(self.im)
		return array




