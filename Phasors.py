import numpy as np
import matplotlib.pyplot as pl

class PhasorPlotter:

    def __init__(self, myFigure=None, figx=5, figy=5):
        if myFigure is None:
            myFigure = pl.figure(figsize=(figx, figy))
        self.figure = myFigure
        self.ax = self.figure.add_subplot(111,aspect=1)
        pl.xlabel("real")
        pl.ylabel("imaginary")
        pl.title("Phasor plot")

    def plot(self, c, color='k'):
        self.ax.plot([0,c.real],[0,c.imag],'k')
        self.ax.annotate("",xy=(c.real,c.imag), xycoords='data',
                         xytext=(0,0), textcoords='data',
                         arrowprops=dict(arrowstyle="->"),
                     )
                     
    def grid(self):
        self.ax.grid()

