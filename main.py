import matplotlib.pyplot as plt
import numpy as np
from calculations import transform
from grab_tmatrix_from_user import getTmatrix

plt.rcParams["figure.autolayout"] = True
plt.figure(figsize=(8,8),dpi=120)

plt.xlim(-20,20)
plt.ylim(-20,20)

plt.xticks(np.arange(-20,20,step=1))
plt.yticks(np.arange(-20,20,step=1))
plt.grid()
plt.axvline(x=0, c="black", label="x=0")
plt.axhline(y=0, c="black", label="y=0")


tMatrix,MINX,MAXX,MINY,MAXY = getTmatrix()

mappings = transform(tMatrix,MINX,MAXX,MINY,MAXY)

for key in mappings:
    x1 = key[0]
    y1=key[1]
    plt.plot(x1,y1,marker ="x", markersize=10, markeredgecolor ="red")


    newCoord = mappings[key]
    x2=newCoord[0]
    y2=newCoord[1]
    plt.plot(x2, y2, marker="x", markersize=10, markeredgecolor="blue")

    x=[x1,x2]
    y=[y1,y2]
    plt.plot(x,y,color="green",linewidth = 0.5)




plt.show()