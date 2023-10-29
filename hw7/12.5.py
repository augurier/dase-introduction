from matplotlib import pyplot as plt
import numpy as np
from PIL import Image

path = '12.5.jpg'
x = plt.imread(path).astype('float32')
Y = x[:,:,0] * 0.299 + x[:,:,1] * 0.587 + x[:,:,2] * 0.114
gray = np.zeros((Y.shape[0],Y.shape[1],3))
gray[:,:,0] = gray[:,:,1] = gray[:,:,2] = Y
plt.imshow(gray.astype('int'))
plt.savefig('1.jpg')
plt.show()

image = Image.open(path)
resized_image = image.resize((300, 400)) 
plt.imshow(resized_image)
plt.savefig('2.jpg')
plt.show()
