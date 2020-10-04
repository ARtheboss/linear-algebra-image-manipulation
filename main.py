import numpy as np
from PIL import Image, ImageDraw

loc = 'asdf.jpg' #raw_input("Image location/url: ")
im1 = Image.open(loc)
pix1 = im1.load()
loc = 'asdf2.jpg'  #raw_input("Image 2 location/url: ")
im2 = Image.open(loc)
pix2 = im2.load()


width = im1.size[0]
height = im1.size[1]

images = [Image.new('RGB', (width, height)) for i in range(10)]
pixels = [i.load() for i in images]


reds1 = np.zeros((width, height))
greens1 = np.zeros((width, height))
blues1 = np.zeros((width, height))
reds2 = np.zeros((width, height))
greens2 = np.zeros((width, height))
blues2 = np.zeros((width, height))

for x in range(width):
	for y in range(height):
		reds1[x, y] = pix1[x, y][0]
		greens1[x, y] = pix1[x, y][1]
		blues1[x, y] = pix1[x, y][2]
		reds2[x, y] = pix2[x, y][0]
		greens2[x, y] = pix2[x, y][1]
		blues2[x, y] = pix2[x, y][2]

for i in range(10):
	for x in range(width):
		for y in range(height):
			i = float(i)
			pixels[int(i)][x, y] = (int(i/10 * reds1[x, y] + (10-i)/10 * reds2[x,y]), 
									int(i/10 * greens1[x, y] + (10-i)/10 * greens2[x,y]), 
									int(i/10 * blues1[x, y] + (10-i)/10 * blues2[x,y]))

images[0].save('test.gif',
               save_all=True,
               append_images=images[1:],
               duration=200,
               loop=0)



