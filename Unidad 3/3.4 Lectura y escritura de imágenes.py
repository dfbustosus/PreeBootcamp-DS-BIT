# !pip install -q scikit-image
from skimage import io 
import matplotlib.pyplot as plt
photo = io.imread('dogormuffin.jpg')
print(type(photo))
print(photo.shape)

print(photo[:,:,0])

#plt.imshow(photo[:,:,0],cmap='jet')
plt.imshow(photo[:,:,0])
plt.show()

plt.imshow(photo)
plt.show()

plt.imshow(photo[::-1,::-1]) # ::-1 significa "toma todo en esta dimension pero alreves
plt.show()

plt.imshow(photo[:, ::-1]) # Efecto espejo 
plt.show()

plt.imshow(photo[:, :,::-1]) # Cambiar de RGB a BGR
plt.show()

plt.imshow(photo[0:534, 0:500]) # Recortar
plt.show()

plt.imshow(photo[::2, ::2]) # Reducir a la mitad
print(photo[::2, ::2].shape)
plt.show()
