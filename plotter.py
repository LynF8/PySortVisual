from math import *
from random import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from sortMethods import *
import sys

sortingMethods = {
    "bubble-sort":bubbleSort,
    "heap-sort":heapSort,
    "insertion-sort":insertionSort,
    "merge-sort":mergeSort,
    "selection-sort":selectionSort,
    "quick-sort":quickSort
}

#TODO: set up colors

# First set up the figure, the axis, and the plot element we want to animate
def showSortList(wayName, arr=[],N=0,todo="play"):
    fig = plt.figure()
    if N==0:
        N = len(arr)
    elif arr==[]:
        arr = list(range(1,N+1))
        shuffle(arr)
    wayToSort = sortingMethods[wayName]
    res = wayToSort(arr)
    seq = res[0]
    toColor = res[1]
    #print(seq[0],toColor[0])

    plt.ylim(0,N+1)

    barcollection = plt.bar(range(N),x)

    defaultColors = {}
    values = list(set(x))
    values.sort()
    l = len(values)
    for i in range(l):
        defaultColors[values[i]] = (0,(l-i-1)/(l-1),i/(l-1))

    l = ceil(log(N,2))
    standOutColors = [((l-i+1)/(l+1),i/(l+1)*0.8,0) for i in range(1,l+1)]
    standOutColors += [(i/(l+1),0,(l-i+1)/(l+1)*0.8) for i in range(1,l+1)]
    standOutColors = [(1,0,0),(0,0,0),(0.4,0.4,0.4)] + standOutColors[::2] + standOutColors[1::2]

    # animation function.  This is called sequentially
    def animate(t):
        if t<len(seq):
            toDraw = seq[t]
            for i, b in enumerate(barcollection):
                b.set_height(toDraw[i])
                try:
                    isSpecial = False
                    for j in range(len(toColor[t])):
                        if i in toColor[t][j]:
                            isSpecial = True
                            b.set_color(standOutColors[j])
                            break
                    if not(isSpecial):
                        b.set_color(defaultColors[toDraw[i]])
                except:
                    b.set_color(defaultColors[toDraw[i]])
            fig.canvas.draw()

    #print(seq)

    # call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, frames=len(seq), interval=250, blit=False)

    # save the animation as an mp4.  This requires ffmpeg or mencoder to be
    # installed.  The extra_args ensure that the x264 codec is used, so that
    # the video can be embedded in html5.  You may need to adjust this for
    # your system: for more information, see
    # http://matplotlib.sourceforge.net/api/animation_api.html
    if todo=="play":
        plt.show()
    elif todo=="save-mp4":
        anim.save(wayName+'.mp4', writer=animation.FFMpegWriter(fps=6))

    return fig

if __name__ == "__main__":
    #print(list(map(type,sys.argv)))
    args = sys.argv

    action = args[1]

    try:
        sortMethod = args[2]
    except:
        sortMethod = "all"
    assert sortMethod in list(sortingMethods.keys())+["all"], sortMethod + " should be in " + str(list(sortingMethods.keys())+["all"])


    N = 10
    x = list(range(1,N+1))
    try:
        N = int(args[4])
        x = list(range(1,N+1))
    except:
        if len(args)>=4 and args[4]!="":
            x = list(map(int,args[4].split(",")))
            N = 0
    
    try:
        mode = args[3]
    except:
        if N==0:
            mode = "fixed"
        else:
            mode = "random"
    if mode == "reversed":
        x = list(reversed(x))
    elif mode == "almost":
        for i in range(N-1):
            if not(randint(0,N//4)):
                temp = x[i]
                x[i] = x[i+1]
                x[i+1] = temp
        #print(x)
    elif mode == "random":
        shuffle(x)
    
    if sortMethod=="all":
        for s in sortingMethods.keys():
            print("generating video for {}".format(s))
            res = showSortList(sortingMethods[s],s,copy(x),N,action)
    else:
        print("generating video for {}".format(sortMethod))
        res = showSortList(sortMethod,copy(x),N,action)
