import numpy as np
from PIL import Image

img = Image.open('train.jpg')
img = img.convert('RGB')
img = np.asarray(img)

new_size = 256

for i in range(10000):
    x = np.random.randint(img.shape[0]-new_size)
    y = np.random.randint(img.shape[1]-new_size)
    crop = img[x:x+new_size, y:y+new_size]
    im = Image.fromarray(crop)
    im.save('mix/{:04d}.png'.format(i))

img = Image.open('second.png')
img = img.convert('RGB')
img = np.asarray(img)

new_size = 256

for i in range(10000, 20000):
    x = np.random.randint(img.shape[0]-new_size)
    y = np.random.randint(img.shape[1]-new_size)
    crop = img[x:x+new_size, y:y+new_size]
    im = Image.fromarray(crop)
    im.save('mix/{:04d}.png'.format(i))
