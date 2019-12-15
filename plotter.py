from math import *
from random import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from sortMethods import *
import sys

# First set up the figure, the axis, and the plot element we want to animate
def showSortList(wayToSort, wayName, arr=[],N=0):
    fig = plt.figure()
    x=arr
    if N==0:
        N = len(x)
    elif x==[]:
        x = list(range(1,N+1))
        shuffle(x)
    seq = wayToSort(x)

    plt.ylim(0,N+1)

    barcollection = plt.bar(range(N),x)

    # animation function.  This is called sequentially
    def animate(t):
        if t<len(seq):
            toDraw = seq[t]
            for i, b in enumerate(barcollection):
                b.set_height(toDraw[i])
            fig.canvas.draw()

    #print(seq)

    # call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, frames=len(seq), interval=1, blit=False)

    # save the animation as an mp4.  This requires ffmpeg or mencoder to be
    # installed.  The extra_args ensure that the x264 codec is used, so that
    # the video can be embedded in html5.  You may need to adjust this for
    # your system: for more information, see
    # http://matplotlib.sourceforge.net/api/animation_api.html
    anim.save(wayName+'.mp4',writer=animation.FFMpegWriter(fps=6))

    #plt.show()

if __name__ == "__main__":
    print(list(map(type,sys.argv)))
    args = sys.argv[1:]
    N = int(args[0])
    try:
        mode = args[1]
    except:
        mode = "random"
    x = list(range(1,N+1))
    if mode == "reversed":
        x = list(reversed(x))
    elif mode == "almost":
        for i in range(N-1):
            if not(randint(0,N//4)):
                temp = x[i]
                x[i] = x[i+1]
                x[i+1] = temp
        print(x)
    else:
        shuffle(x)
    sortingMethods = {
        "bubbleSort":bubbleSort,
        "insertionSort":insertionSort,
        "mergeSort":mergeSort,
        "selectionSort":selectionSort
    }
    for s in sortingMethods.keys():
        showSortList(sortingMethods[s],s,copy(x),N)
