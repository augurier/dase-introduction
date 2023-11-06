import librosa
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from moviepy.editor import *

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False


audio, freq = librosa.load('./video.wav')#audio 采样信号，freq采样率
time = np.arange(0, len(audio)) / freq


plt.plot(time, audio)
plt.show()