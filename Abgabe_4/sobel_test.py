import sobel_demo as nd
import numpy as np
from skimage import io
import matplotlib.pyplot as plt
import time


def rgb_2_gray(img, mode='lut'):
    if mode == 'lut':
        return np.round(img[:,:,0] * 0.2126 + img[:,:,1] * 0.7152 + img[:,:,2] * 0.0722)
    else:
        return np.round(img[:,:,0] * 0.2126 + img[:,:,1] * 0.587 + img[:,:,2] * 0.114)


img = io.imread("lena.jpg")
gray = rgb_2_gray(img).astype("float64")

# TODO: define filters in x in y direction

filter_x = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]], dtype=float)

filter_y = np.array([[-1, -2, -1],
                    [0, 0, 0],
                    [1, 2, 1]], dtype=float)

start = time.time()
# TODO: filter image in x direction (nd.sobel(gray, filter_x))
gx = nd.sobel(gray, filter_x)
end = time.time()
duration = end-start
print("Duration in milliseconds: ", duration*1000)


start = time.time()
# TODO: filter image in y direction (nd.sobel(gray, filter_y))
gy = nd.sobel(gray, filter_y)
end = time.time()
duration = end-start
print("Duration in milliseconds: ", duration*1000)

# TODO compute Gradient magnitude
magnitude = np.sqrt(gx**2 + gy**2)


plt.figure(figsize=(12,4))
plt.subplot(1,3,1)
plt.title("1. Ableitung in x-Richtung (horizontal)")
plt.imshow(gx, cmap='gray')
plt.axis('off')

plt.subplot(1,3,2)
plt.title("1. Ableitung in y-Richtung (vertikal)")
plt.imshow(gy, cmap='gray')
plt.axis('off')

plt.subplot(1,3,3)
plt.title("Kantenstärke")
plt.imshow(magnitude, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()