# Programmējamais kods
## parastā bilde un kods
import  cv2
import matplotlib.pyplot as plt
image=cv2.imread('planet.png')#importets attels
img_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
resized_img=cv2.resize(img_rgb,(500,500))#pieskir izmeru attelam
resized_img[20,2]=(0,0,0) #melna krasa pozicija

plt.figure(figsize=(10,10))
plt.imshow(resized_img)
