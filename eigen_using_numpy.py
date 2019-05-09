import matplotlib.pyplot as plt
import numpy as np

image = plt.imread("image.jpg")
rows, cols = image.shape
i,j = np.mgrid[:rows, :cols]
coords = np.vstack((i.reshape(-1), j.reshape(-1), image.reshape(-1))).T
cov = np.cov(coords)
eigvals, eigvecs = np.linalg.eigh(cov)
