### Aizkrāsot noteiktu secību ar pikseļiem
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

image=Image.open('planet1.png') #nolasām attēlu
resized_img=image.resize((500,500)) #mērogošana
pixels = resized_img.load()
n = 6
m = 9
for x in range (500):
    for y in range (500):
        if (x % n) == (y % m):
            pixels[x,y] = (0,255,0)
            
plt.figure(figsize=(10,10))
plt.imshow(resized_img)
