from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from functools import reduce
from collections import Counter


def cex():
    noaex=open('noaex.txt', 'a')
    an=range(0,10)
    vn=range(1,10)

    for en in an:
        for ev in vn:
            #print('.'.join([str(en), str(ev)]))
            fpath='images/numbers/'+'.'.join([str(en), str(ev)])+'.png'
            ei=Image.open(fpath)
            eiar=np.array(ei)
            eiar1=str(eiar.tolist())
            lno=str(en)+'::'+eiar1+'\n'
            noaex.write(lno)

def threshold(imgArr):
    barr=[]
    narr=imgArr
    
    for erow in imgArr:
        for epix in erow:
            avgNum=reduce(lambda x, y: x+y, epix[:3])/len(epix[:3])
            barr.append(avgNum)

    b=reduce(lambda x, y: x+y, barr)/len(barr)

    for erow in narr:
        for epix in erow:
            if reduce(lambda x, y: x+y, epix[:3])/len(epix[:3]) > b:
                epix[0]= 255
                epix[1]= 255
                epix[2]= 255
                epix[3]= 255
            else:
                epix[0]= 0
                epix[1]= 0
                epix[2]= 0
                epix[3]= 255

    return narr


def match(filepath):
    mar=[]
    loadex=open('noaex.txt', 'r').read()
    loadex=loadex.split('\n')

    i = Image.open(filepath)
    iar=np.array(i)
    iar1=iar.tolist()
    ask= str(iar1)

    for eex in loadex:
        if len(eex)>3:
            splitex=eex.split('::')
            cno=splitex[0]
            car=splitex[1]

            pixin=car.split('],')
            pixiq=ask.split('],')

            l=0

            while l<len(pixin):
                if pixin[l]==pixiq[l]:
                    mar.append(int(cno))
                l+=1

    print(mar)
    l = Counter(mar)
    print(l)
    graphx=[]
    graphy=[]

    for et in l:
        print(et)
        graphx.append(et)
        print(l[et])
        graphy.append(l[et])

    fig=plt.figure()
    ax1=plt.subplot2grid((4,4),(0,0), rowspan=1, colspan=4)
    ax2=plt.subplot2grid((4,4),(1,0), rowspan=3, colspan=4)
    ax1.imshow(iar)
    ax2.bar(graphx,graphy, align='center')
    plt.ylim(400)
    xloc=plt.MaxNLocator(12)
    ax2.xaxis.set_major_locator(xloc)

    plt.show()



match('images/numbers/0.1.png')




















        
