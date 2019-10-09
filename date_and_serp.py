# -*- coding: utf-8 -*-
"""
helper function that extracts the date and serp based on the directory and
file name

method from: http://techs.studyhorror.com/python-get-last-directory-name-in-path-i-139
"""

import re
import os

def date_and_serp(file_path):
    
    date = os.path.basename(os.path.dirname(file_path))
    file_name = os.path.basename(file_path)
    serp = re.findall(r'\d+', file_name)
    serp = serp[0] # lazy hack, line 16 will return all numeric values in a
                   # the file name but i assume there's only one
    return (date, serp)
    