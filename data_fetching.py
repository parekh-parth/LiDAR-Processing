!pip install laspy

import laspy
import scipy
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn import preprocessing
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import path

from google.colab import drive
drive.mount('/content/drive')

inFile = laspy.file.File('/content/drive/My Drive/asimple.las')
