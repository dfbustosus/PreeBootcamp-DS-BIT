import numpy as np
# python -m pip install scikit-image
from skimage import io 
import matplotlib.pyplot as plt

photo = io.imread('dogormuffin.jpg')
print(type(photo))
print(photo.shape)

plt.imshow(photo)
plt.show()

plt.imshow(photo[::-1]) # ::-1 significa "toma todo en esta dimension pero alreves
plt.show()

plt.imshow(photo[:, ::-1]) # Efecto espejo 
plt.show()

plt.imshow(photo[:, :,::-1]) # Cambiar de RGB a BGR
plt.show()

plt.imshow(photo[0:534, 0:500]) # Recortar
plt.show()

plt.imshow(photo[::2, ::2]) # Reducir a la mitas
print(photo[::2, ::2].shape)
plt.show()

photo_sin = np.round(np.abs(np.sin(photo) ),0)*260
print(photo_sin)

photo_msk = np.where(photo> 100, 255, 0)
plt.imshow(photo_msk)
plt.show()

plt.imshow(photo[:,:,2].T,cmap='jet')
plt.show()