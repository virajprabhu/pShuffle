import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

amp, freq = 5, 3
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
t = np.arange(0.0, 1.0, 0.001)
a0 = 5
f0 = 3
s = a0*np.sin(2*np.pi*f0*t)
l, = plt.plot(t,s, lw=2, color='red')
plt.axis([0, 1, -10, 10])

axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], axisbg=axcolor)
# axamp  = plt.axes([0.25, 0.15, 0.65, 0.03], axisbg=axcolor)

sfreq = Slider(axfreq, 'Freq', 0.1, 5.0, valinit=f0)
sfreq.valtext.set_visible(False)
# samp = Slider(axamp, 'Amp', 0.1, 5.0, valinit=a0)

def update(val):
	global freq
	freq = sfreq.val
	print 'amplitude:', amp, 'frequency:', freq
	l.set_ydata(amp*np.sin(2*np.pi*freq*t))
	fig.canvas.draw_idle()
sfreq.on_changed(update)
# samp.on_changed(update)

resetax = plt.axes([0.5, 0.025, 0.1, 0.04])
confirmax = plt.axes([0.3, 0.025, 0.1, 0.04])

reset_button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')
confirm_button = Button(confirmax, 'pShuffle', color=axcolor, hovercolor='0.975')

def reset(event):
	sfreq.reset()
	# samp.reset()
reset_button.on_clicked(reset)

def confirm(event):
	print 'Initializing pShuffle'
	plt.close(fig)
confirm_button.on_clicked(confirm)

def run():
	plt.show()
