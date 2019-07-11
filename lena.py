import numpy
import matplotlib.pyplot as plt
from PIL import Image

lena_path = r'D:\python\works\lena.png'
lena = Image.open(lena_path)
arr = numpy.array(lena.getdata(), numpy.uint8).reshape(lena.size[1], lena.size[0], 3)

plt.gray()

plt.imshow(arr)
plt.colorbar()
plt.show()