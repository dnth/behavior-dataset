import numpy as np
from naoqi import ALProxy
import os, time
from cProfile import label
import matplotlib.pyplot as plt
import Image
import numpy as np
from scipy import ndimage
import vision_definitions
  
def setup_backend(backend='TkAgg'):
    import sys
    del sys.modules['matplotlib.backends']
    del sys.modules['matplotlib.pyplot']
    import matplotlib as mpl
    mpl.use(backend)  # do this before importing pyplot
    import matplotlib.pyplot as plt
    return plt
  
robotIP="192.168.0.108"
tts=ALProxy("ALTextToSpeech", robotIP, 9559)
motion = ALProxy("ALMotion", robotIP, 9559)
memory = ALProxy("ALMemory", robotIP, 9559)
camProxy = ALProxy("ALVideoDevice", robotIP, 9559)
posture = ALProxy("ALRobotPosture", robotIP, 9559)
  
resolution = 0    # kQQVGA
colorSpace = 11   # RGB
  
tts.say("Hello")
# posture.goToPosture("Crouch", 1.0)
# motion.rest()
# print "robot is at rest"
time.sleep(5)
tts.say("Sampling")
  
dataSize=10000
JointArray = np.zeros((10000,10))
ImageArrayGray = np.zeros((10000,400))
ImageArrayRGB = np.zeros((10000,1200))
jointdata = np.zeros((1,10))
videoClient = camProxy.subscribe("python_client77", resolution, colorSpace, 30)
camProxy.setParam(vision_definitions.kCameraBrightnessID, 40)
camProxy.setParam(vision_definitions.kCameraAutoWhiteBalanceID, 0)
camProxy.setParam(vision_definitions.kCameraAutoExpositionID, 0)
  
  
def animate():
    naoImage = camProxy.getImageRemote(videoClient)
  
    imageWidth = naoImage[0]
    imageHeight = naoImage[1]
    array = naoImage[6]
                              
    im = Image.fromstring("RGB", (imageWidth, imageHeight), array)
    imrgb=im.resize((20,20),Image.ANTIALIAS)
    imgray = imrgb.convert('L')
                              
    imrgbArray = np.array(imrgb)
    imgrayArray = np.array(imgray)
    fig3=plt.figure(3) # input image
    fig3.canvas.set_window_title('Figure 3: Input Image') 
    inputimage = plt.imshow(imrgbArray,interpolation='Nearest',animated=True,label="blah", cmap=plt.get_cmap('gray'))
  
    t_start=time.time()
    for i in range(dataSize):
        time_start=time.time()
        jointdata[0,0] = memory.getData("Device/SubDeviceList/RShoulderPitch/Position/Sensor/Value")
        jointdata[0,1] = memory.getData("Device/SubDeviceList/RShoulderRoll/Position/Sensor/Value")
        jointdata[0,2] = memory.getData("Device/SubDeviceList/RElbowRoll/Position/Sensor/Value")
        jointdata[0,3] = memory.getData("Device/SubDeviceList/RElbowYaw/Position/Sensor/Value")
        jointdata[0,4] = memory.getData("Device/SubDeviceList/RWristYaw/Position/Sensor/Value")
                   
        jointdata[0,5] = memory.getData("Device/SubDeviceList/LShoulderPitch/Position/Sensor/Value")
        jointdata[0,6] = memory.getData("Device/SubDeviceList/LShoulderRoll/Position/Sensor/Value")
        jointdata[0,7] = memory.getData("Device/SubDeviceList/LElbowRoll/Position/Sensor/Value")
        jointdata[0,8] = memory.getData("Device/SubDeviceList/LElbowYaw/Position/Sensor/Value")
        jointdata[0,9] = memory.getData("Device/SubDeviceList/LWristYaw/Position/Sensor/Value")
                
        JointArray[i,:] = jointdata
               
        naoImage = camProxy.getImageRemote(videoClient)
        imageWidth = naoImage[0]
        imageHeight = naoImage[1]
        array = naoImage[6]
                   
        im = Image.fromstring("RGB", (imageWidth, imageHeight), array)
        imrgb=im.resize((20,20),Image.ANTIALIAS)
        imgray = imrgb.convert('L')
                 
        imgrayArray = np.array(imgray)
        imrgbArray = np.array(imrgb)
        inputimage.set_data(imrgb)
        fig3.canvas.draw()
#         plt.draw()
          
        imgrayArray = imgrayArray.flatten()
        imrgbArray = imrgbArray.flatten()
        ImageArrayGray[i,:] = imgrayArray/255.0
        ImageArrayRGB[i,:] = imrgbArray/255.0
          
        time_end= time.time()
        print i, " FPS:",1/(time_end-time_start)
      
    camProxy.unsubscribe(videoClient)
    t_end = time.time()
    fps = dataSize/(t_end-t_start)
    print "Average FPS: ",fps
      
    np.savetxt('/home/camaro/workspace/nao_codes/20fpsFullBehaviorSampling/BellRingR/JointData.txt', JointArray)
    np.savetxt('/home/camaro/workspace/nao_codes/20fpsFullBehaviorSampling/BellRingR/ImageDataGray.txt', ImageArrayGray)
    np.savetxt('/home/camaro/workspace/nao_codes/20fpsFullBehaviorSampling/BellRingR/ImageDataRGB.txt', ImageArrayRGB)
          
plt = setup_backend()
fig=plt.figure(3, figsize=(5, 5), dpi=90, facecolor='w', edgecolor='k')
win = fig.canvas.manager.window
win.after(10, animate)
plt.ion()
plt.show()



