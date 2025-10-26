import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sounddevice as sd
from PIL import Image
import queue
import math
from scipy.linalg import svd

DEVICE = 0
WINDOW = 1000
DOWNSAMPLE = 1
CHANNELS = [1]
INTERVAL = 30

img = Image.open('hate.png')
imggray = img.convert('L')
mat = np.array(list(imggray.getdata(band=0)), float)
mat.shape = (imggray.size[1], imggray.size[0])
mat = np.matrix(mat)

U, sigma, V = svd(mat)

q = queue.Queue()
device_info = sd.query_devices(DEVICE, 'input')
samplerate = device_info['default_samplerate']
length = int(WINDOW*samplerate/(1000*DOWNSAMPLE))

plotdata = np.zeros((length,len(CHANNELS)))

fig, ax = plt.subplots(figsize = (10, 6))

fig.canvas.draw()

def audio_callback(indata, frames, time, status):
    q.put(indata[::DOWNSAMPLE,[0]])

recon = np.matrix(U[:, :1]) * np.diag(sigma[:1]) * np.matrix(V[:1, :])
img_showing = ax.imshow(recon, cmap='gray')

def update(val):
    global plotdata
    while True:
        try:
            data = q.get_nowait()
        except queue.Empty:
            break
        shift = len(data)
        plotdata = np.roll(plotdata, -shift,axis=0)
        plotdata[-shift:,:] = data
        
    volume = math.sqrt(np.mean(plotdata**2))
    n = int(volume * 2000)
    n = np.clip(n, 1, len(sigma))
    
    recon = U[:, :n] @ np.diag(sigma[:n]) @ V[:n, :]
    img_showing.set_data(recon)
    ax.set_title(f"n = {n}")

stream  = sd.InputStream( device = DEVICE, channels = max(CHANNELS), samplerate = samplerate, callback  = audio_callback)


with stream:
    ani = FuncAnimation(fig, update, interval=INTERVAL)
    plt.show()
