# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 07:59:12 2019

@author: kyle
"""

import pandas as pd
import numpy as np
from skimage import io as sk_io
from skimage.color import rgb2hsv

def percentGreen(image, lightboxHue = None, turfHue = None, 
                  turfSaturation = None):
    """
    value = percent_green(image, lightboxHue, turfHue, turfSaturation)
    
    Takes a HSV image, and returns a value of percent green and a mask of
    turf pixels.
    
    Equation:
        value = green pixels with turfHue AND turfSaturation range 
            / (total pixels - colorboxHue range)
    
    INPUT:
        image: a scikit image, 3D-array with [:, :, 0] being hue, [:,:,1] is
               saturation, [:, : ,2] is value
        lightBoxHue: a list of two values from min hue to max hue in range
                     0 to 255
        turfHue: a list of two values from min hue to max hue in range
                 0 to 255
        turfSaturation: a list of two values from min saturation to max saturation
                        in 0 to 255
    """
    # hue and saturation values are range 0-1, need to bring it up to 8-bit
    # 0-255 for what is commonly in literature   
    
    hue_img = np.around((image[:, :, 0] * 255),0)
    saturation_img = np.around((image[:, :, 1] * 255),0)

    
    # create a threshold mask that refer to turfgrass that match the hue
    # and saturation range
    
    turf_mask = ((hue_img > turfHue[0]) & (hue_img < turfHue[1])) * ((saturation_img 
                > turfSaturation[0]) & (saturation_img < turfSaturation[1]))
    
    lightbox_mask = ((hue_img > lightboxHue[0]) & (hue_img < lightboxHue[1]))
    
    # sum is used twice to sum in both directions of the array
    value = sum(sum(turf_mask)) / (np.size(hue_img) - sum(sum(lightbox_mask)))
    
    return (value, turf_mask, lightbox_mask)