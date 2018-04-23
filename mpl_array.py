import matplotlib.pyplot as plt
import numpy as np

def show_array_hotspots(arr,xlabels=None,ylabels=None,color="Reds",marker_size=20,**kwargs):
    """Create a visual grid of an arrays positions. Values are represented by color coded dots"""
    
    plt.figure(**kwargs)
    plt.rc("grid",linestyle="--")
    x=np.arange(arr.shape[1])
    y=np.arange(arr.shape[0])
    xx,yy=np.meshgrid(x,y)
    
    colormap = plt.cm.get_cmap(color)
    if xlabels:
        plt.xticks(x,xlabels,rotation="vertical")
    else:
        plt.xticks(x,[])
    if ylabels:
        plt.yticks(y,ylabels)
    else:
        plt.yticks(x,[])

    sc=plt.scatter(xx,yy,c=arr,cmap=colormap,s=marker_size)
    plt.colorbar(sc)
    plt.show()
