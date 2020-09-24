import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

w = 500
h = 500
fig = plt.figure(figsize=(9, 13))
columns = 5
rows = 2

# prep (x,y) for extra plotting
xs = np.linspace(0, 2*np.pi, 60)  # from 0 to 2pi
ys = np.abs(np.sin(xs))           # absolute of sine

# ax enables access to manipulate each of subplots
ax = []
i=0
for imgs in os.listdir('./generated_images'):
    img_path = os.path.join('./generated_images',imgs)
    name = os.path.basename(img_path)
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
    # create subplot and append to ax
    ax.append( fig.add_subplot(rows, columns, i+1) )
    ax[-1].set_title(name)  # set title
    plt.axis('off')
    plt.imshow(img)
    i += 1

# do extra plots on selected axes/subplots
# note: index starts with 0
ax[2].plot(xs, 3*ys)
ax[9].plot(ys**2, xs)

plt.show()