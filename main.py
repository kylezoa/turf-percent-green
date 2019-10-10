# -*- coding: utf-8 -*-
"""
Calculate the percent green turf based on lightbox color and hue range of
turfgrass. Image calculations done on a HSV scale. Values exported to
pandas dataframe.

Kyle Cheung
kyhcheung@ucdavis.edu

Based on python 3.7
Dependencies:
    pandas
    numpy
    scikit-image
"""

import os
import pandas as pd
import numpy as np
import glob
from percentGreen import percentGreen
from date_and_serp import date_and_serp
from skimage import io as sk_io
from skimage.color import rgb2hsv

# loop through a folder recursively, taking the folder name as the column name
folder_path = r'C:\Users\kyle\Box\remote sensing turf drought Kearney\Digital images captured with lightbox\\'
files = [f for f in glob.glob(folder_path + "**/*.JPG", recursive=True)]
turfHue = [55, 100]
turfSaturation = [0, 255]
lightboxHue = [150, 160]
serpRange = [1, 36]

# start a blank pandas dataframe that has rows 1 through 36
df = pd.DataFrame(index=range(serpRange[0], serpRange[1]))

for file in files:
    # run the file path in a helper function that extracts serp and date
    date, serp = date_and_serp(file)
    
    # take the first string element because the helper
    # finds all possible digits, convert to integer
    serp = int(serp)
    
    print(date, serp)
    # open up that image as a numpy 3D-array
    rgb_image = sk_io.imread(file)
    
    # convert rgb to hsv
    hsv_image = rgb2hsv(rgb_image)
    
    # send it to the percentGreen function to return a percent value [0-1],
    # mask of the turf, and mask of the light box (references that can be used
    # in future analysis)
    
    value, turf_mask, lightbox_mask = percentGreen(hsv_image,
                                                   lightboxHue = lightboxHue, 
                                                   turfHue = turfHue, 
                                                   turfSaturation = turfSaturation)
    
    # add the percent value to the df
    df.loc[serp, date] = value
    