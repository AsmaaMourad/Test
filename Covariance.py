import matplotlib.pyplot as plt
import numpy as np

image = plt.imread("image.jpg")
cov = np.cov(image)
