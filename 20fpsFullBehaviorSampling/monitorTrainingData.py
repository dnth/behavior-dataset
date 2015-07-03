import numpy as np
import matplotlib.pyplot as plt
import time

BallLift = np.loadtxt('Ropeway/ImageDataRGB.txt').astype(np.float32)
def setup_backend(backend='TkAgg'):
    import sys
    del sys.modules['matplotlib.backends']
    del sys.modules['matplotlib.pyplot']
    import matplotlib as mpl
    mpl.use(backend)  # do this before importing pyplot
    import matplotlib.pyplot as plt
    return plt 



def animate():
    trainImage=BallLift[0,:]
    trainImage = np.reshape(trainImage, (20,20,3))
    fig4=plt.figure(4) 
    fig4.canvas.set_window_title('Figure 1: Training Image') 
    Trainingimage = plt.imshow(trainImage,interpolation='Nearest',animated=True,label="blah", cmap=plt.get_cmap('gray'))
    for i in range(500):
        timeStart=time.time()
        trainImage=BallLift[i,:]
        trainImage = np.reshape(trainImage, (20,20,3))
        Trainingimage.set_data(trainImage)
        plt.draw()
        time.sleep(0.015)
        print i, " FPS:",1/(time.time()-timeStart)


plt = setup_backend()
fig=plt.figure(4, figsize=(10, 5), dpi=90, facecolor='w', edgecolor='k')
win = fig.canvas.manager.window
win.after(10, animate)
plt.ion()
plt.show()

