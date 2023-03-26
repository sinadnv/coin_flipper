import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Button
import random


def heads_or_tails():
    coin_side = random.randint(1,2)     #1: heads, 2: tails
    if coin_side ==1:
        alpha = np.linspace(0,8*90,80)*np.pi/180        # 4 coin flips before showing the heads
    else:
        alpha = np.linspace(0,8*90+2*90,100)*np.pi/180   # 4 coin flips before showing the tails
    return alpha


def flip(alpha):
    global axes
    global circle_radius
    plt.close('all')
    circle_radius = 50
    x = np.linspace(-circle_radius,circle_radius,100)

    for a in alpha:
        yP = np.sqrt(circle_radius * circle_radius - x * x) * np.cos(a)
        plt.plot(x, yP,color='gray')
        plt.plot(x, -yP,color='gray')
        if np.cos(a) >= 0:
            plt.fill_between(-x, -yP, yP, color='blue', alpha=0.5)
            plt.annotate('HEADS',(0,0), horizontalalignment = 'center', verticalalignment = 'center', weight = 'bold',
                         fontsize = 22)
        else:
            plt.fill_between(-x, -yP, yP, color='red', alpha=0.5)
            plt.annotate('TAILS',(0,0), horizontalalignment = 'center', verticalalignment = 'center', weight = 'bold',
                         fontsize = 22)

        plt.axis('equal')
        plt.xlim([-100,100])
        plt.ylim([-100, 100])
        plt.xticks([])
        plt.yticks([])
        plt.pause(.01)
        if a != alpha[-1]:
            plt.clf()
    #axes = plt.axes([0.81, 0.000001, 0.1, 0.075])
    axes = plt.axes([.4, 0, .2, .075])

    flip_button = Button(axes, 'Flip Again', color="yellow")
    flip_button.on_clicked(flip_again)
    plt.pause(.01)
    plt.show()


def flip_again(event):
    flip(heads_or_tails())


flip(heads_or_tails())


