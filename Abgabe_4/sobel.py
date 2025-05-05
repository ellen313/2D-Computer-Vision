import numpy as np
import matplotlib.pyplot as plt
from matplotlib.mlab import magnitude_spectrum
from skimage import io
import time

def rgb_2_gray(img, mode='lut'):
    if mode == 'lut':
        return np.round(img[:,:,0] * 0.2126 + img[:,:,1] * 0.7152 + img[:,:,2] * 0.0722)
    else:
        return np.round(img[:,:,0] * 0.2126 + img[:,:,1] * 0.587 + img[:,:,2] * 0.114)
    

def sobel(img, filter):
    # TODO: implement sobel filtering e.g. with 4 foor loops
    height, width = img.shape
    filter_h, filter_w = filter.shape

    s = 1.0 if np.sum(filter) == 0 else 1.0 / np.sum(filter)

    # filter matrix (2K+1)×(2L+1) (radius)
    K = filter_w // 2
    L = filter_h // 2

    filtered_img = np.zeros((height - 2 * K, width - 2 * L))

    for v in range(L, height - L):  #über Zeilen
        for u in range(K, width - K):  #über Spalten
            value = 0.0
            for j in range(-L, L + 1):  #über Filterzeilen
                for i in range(-K, K + 1):  #über Filterspalten
                    value += img[v + j, u + i] * filter[j + L , i + K]
            filtered_img[v - L , u - K] = s * value

    filtered_img = np.clip(filtered_img, 0, 255).astype(np.uint8)

    return filtered_img

def grad_magnitude(x_result, y_result):
    gx = x_result.astype(np.float32)
    gy = y_result.astype(np.float32)

    magnitude = np.sqrt(gx ** 2 + gy ** 2)
    magnitude = np.clip(magnitude, 0, 255).astype(np.uint8)
    return magnitude


img = io.imread("lena.jpg")
gray = rgb_2_gray(img)

height, width = gray.shape

# TODO: define filter in x in y direction

filter_x = np.array([[ -1,  0,  1],
                     [ -2,  0,  2],
                     [ -1,  0, 1]])

filter_y = np.array([[ -1, -2, -1],
                     [  0,  0, 0],
                     [  1,  2, 1]])


start = time.time()
# TODO: filter image in x direction (sobel(gray, filter_x))
sobelx_grad = sobel(gray, filter_x)
end = time.time()
duration = end-start
print("Duration in milliseconds: ", duration*1000)

start = time.time()
# TODO: filter image in y direction (sobel(gray, filter_y))
sobely_grad = sobel(gray, filter_y)
end = time.time()
duration = end-start
print("Duration in milliseconds: ", duration*1000)

# TODO compute Gradient magnitude
magnitude = grad_magnitude(sobelx_grad, sobely_grad)

plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.title("∂I/∂x(u,v) (horizontal)")
plt.imshow(sobelx_grad, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("∂I/∂y(u,v) (vertikal)")
plt.imshow(sobely_grad, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Kantenstärke (|∇f|)")
plt.imshow(magnitude, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()