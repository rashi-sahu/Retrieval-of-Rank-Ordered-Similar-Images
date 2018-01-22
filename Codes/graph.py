import Tkinter as tk
from Tkinter import *
import ttk
import xml.etree.ElementTree as ET
from PIL import Image,ImageTk
import cv2
import numpy as np
import time
import coverage
import matplotlib.cm as cm
from gaps_close import *



def show_graph(adjacency_matrix,text2,root):

    import networkx as nx
    import matplotlib.pyplot as plt

    # no_rows_cols=adjacency_matrix.shape()

    rows, cols = np.where(adjacency_matrix == 1)
    edges = zip(rows.tolist(), cols.tolist())
    gr = nx.Graph()
    gr.add_edges_from(edges)

    nx.draw_networkx(gr,node_color="#5072A7",node_size=1200,width=4)


    plt.axis('off')
    plt.savefig('graph.tiff')
    im1=cv2.imread('graph.tiff')
    res=cv2.resize(im1,(460,460),interpolation=cv2.INTER_CUBIC)
    im2=Image.fromarray(res)
    imgtkr=ImageTk.PhotoImage(image=im2)
    text2.window_create(tk.END, window=tk.Label(text2, image=imgtkr))
    w1=Label(root,image=imgtkr)
    w1.image=imgtkr

	#plt.show()



