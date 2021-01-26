import peempy.imageproc as imp
import matplotlib.pyplot as plt
from skimage.data import astronaut
from skimage.color import rgb2grey
from scipy.ndimage import shift
import numpy as np

# n images
n_images = 20
base_img = rgb2grey(astronaut())
print (np.shape(base_img))
# Generate randomised shift vectors
rand_scale = 2
mean_drift_scale = 1
mean_drift_vec = np.random.random(2) * mean_drift_scale + np.array([1, 1])
insert_vec = np.random.random((n_images, 2)) * rand_scale
ind = np.arange(n_images).reshape((n_images, 1))
drift = ind * mean_drift_vec + insert_vec
drift -= drift[4]
print (np.shape(drift))
# Create the drifted image set
dataset = []
for i in range(n_images):
    drifted = shift(base_img, drift[i])
    dataset.append(drifted)
dataset = np.asarray(dataset)
print (np.shape(dataset))

# Construct corrector object
cor = imp.DriftCorrector(dataset, 4, ((411, 34), (325, 112)))
cor.calc_drifts()
cor.super_sample = 4
#%
# Plot
plt.subplot(211)
plt.plot(drift[:, 0], drift[:, 1], 'r-x', label="Image drift")
plt.plot(-cor.drifts[:, 0], -cor.drifts[:, 1], 'b-x', label="detected")
plt.legend()
plt.subplot(212)
plt.plot(-cor.drifts[:, 0] - drift[:, 0],
         -cor.drifts[:, 1] - drift[:, 1],
         ".-",
         label="Error")
plt.legend()
plt.show()
