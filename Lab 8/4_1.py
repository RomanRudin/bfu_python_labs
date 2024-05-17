#The same version, but with the possibility to change phases and sum multiple waves
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.widgets import Slider

number_of_waves = 3 #up to 4, I think, will be great
if number_of_waves > 4 or number_of_waves < 1 or type(number_of_waves) != type(2):
    raise "Number waves needs to be a positive integer less than 5"

colors = ['red', 'blue', 'yellow', 'green']

ChangebleGraphicInstances = []

class DynamicGraphic():
    def __init__(self, figure:plt.Figure, color:str, place:int, spec:gridspec.GridSpec):
        self.figure = figure
        self.x = np.arange(0, 1)
        self.y = np.arange(0, 1)
        self.figure.add_subplot(spec[(place * 3):(place * 3 + 4), :])
        self.line, = plt.plot(self.x, self.y, color=color)
        plt.axis([0, 4, -(number_of_waves * 10), (number_of_waves * 10)])
        plt.grid()

    def init__update(self):
        self.x = ChangebleGraphicInstances[0].x
        self.line.set_xdata(self.x)
        self.y = np.sum([d.y for d in ChangebleGraphicInstances], axis=0)
        self.update()

    def update(self):
        self.line.set_ydata(np.sum([d.y for d in ChangebleGraphicInstances], axis=0))
        self.figure.canvas.draw_idle()


class ChangebleGraphic():
    def __init__(self, figure:plt.Figure, color:str, place:int, spec:gridspec.GridSpec, dependent:DynamicGraphic):
        self.figure = figure
        self.dependent = dependent
        self.x = np.linspace(0, 4, num=400)
        self.amplitude = 5
        self.frequency = 2.5
        self.phase = 0
        self.y = self.amplitude*np.sin(np.pi*self.frequency*self.x + self.phase * np.pi)
        self.figure.add_subplot(spec[(place * 3):(place * 3 + 3), :3])
        self.line, = plt.plot(self.x, self.y, color=color)
        plt.grid()
        plt.axis([0, 4, -10, 10])

        axfreq = self.figure.add_subplot(spec[place * 3, 3])
        axamp = self.figure.add_subplot(spec[place * 3 + 1, 3])
        axaph = self.figure.add_subplot(spec[place * 3 + 2, 3])

        self.slider_freq = Slider(axfreq, 'Freq', 0.1, 10.0, valinit=self.frequency, valfmt="%f"[:4])
        self.slider_amp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=self.amplitude, valfmt="%f"[:4])
        self.slider_phase = Slider(axaph, 'Phase', 0 - 1, 1, valinit=self.phase, valfmt="%f"[:4])
        self.slider_freq.on_changed(self.update)
        self.slider_amp.on_changed(self.update)
        self.slider_phase.on_changed(self.update)

        ChangebleGraphicInstances.append(self)

    def update(self, val):
        self.amplitude = self.slider_amp.val
        self.frequency = self.slider_freq.val
        self.phase = self.slider_phase.val
        self.y = self.amplitude*np.sin(2*np.pi*self.frequency*self.x + self.phase * np.pi)
        self.line.set_ydata(self.y)
        self.figure.canvas.draw_idle()
        self.dependent.update()


figure = plt.figure(constrained_layout=True)
figure.set_size_inches(number_of_waves * 3 + 4, 8)
spec = figure.add_gridspec(ncols=4, nrows=(3*number_of_waves + 4), left=0.05, right=0.06, wspace=0.05)

result = DynamicGraphic(figure, "black", number_of_waves, spec)

for i in range(number_of_waves):
    ChangebleGraphic(figure, colors[i], i, spec, result)

result.init__update()

plt.show()