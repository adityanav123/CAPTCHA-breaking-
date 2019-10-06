""""from captcha.image import ImageCaptcha 
img = ImageCaptcha()
image = img.generate_image('ae34bv')
image.show()
image.save('D:/Captcha/new_Captcha.png')"""
# OLD CODE - NEW CAPTCHAs TAKEN FROM SITE Recc.
# THIS CAPTCHA is full of noise.
import sys
import os 
import random 
import string
from captcha.image import ImageCaptcha
def random_string(length = 4):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(length))
args = sys.argv 
directory = args[1] # where to save the generated captcha's 
count = 1000 
for _ in range(count):
	img = ImageCaptcha()
	str_to_save = random_string(4)
	image = img.generate_image(str_to_save)
	image.save(directory + '/' + str(str_to_save) + '.png')
