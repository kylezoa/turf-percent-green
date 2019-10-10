# -*- coding: utf-8 -*-
"""
Calculate the percent green turf based on lightbox color and hue range of
turfgrass. Image calculations done on a HSV scale. Values exported to
pandas dataframe.

Kyle Cheung
kyhcheung@ucdavis.edu

Based on python 3.7

External Dependencies:
    pandas
    numpy
    opencv (cv2)
"""

import pandas as pd
import glob
from percentGreen import percentGreen
from date_and_serp import date_and_serp
import cv2

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
    bgr_image = cv2.imread(file)
    
    # convert rgb to hsv
    hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
    
    # send it to the percentGreen function to return a percent value [0-1],
    # mask of the turf, and mask of the light box (references that can be used
    # in future analysis)
    
    value, turf_mask, lightbox_mask = percentGreen(hsv_image,
                                                   lightboxHue = lightboxHue, 
                                                   turfHue = turfHue, 
                                                   turfSaturation = turfSaturation)
    
    # add the percent value to the df
    df.loc[serp, date] = value
    