#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 11:43:21 2018

@author: siddharth
"""

from PIL import Image
import glob

#%%
image_list = []
str = "/home/siddharth/Computer\ Vision/Data/Positive/PosImage"
count = 1
for filename in glob.glob('/home/siddharth/facescrub/download/*/face/*.jpg'): #assuming gif
    im=Image.open(filename)
    im = im.resize((100,100),Image.BILINEAR)
    im.save("/home/siddharth/Computer Vision/Data/Train_Positive/PosImage%d.jpg"%count)
    print("Iteration:",count)
    image_list.append(im)
    im2 = im.crop((0,0,25,25))
    im2 = im2.resize((100,100),Image.BILINEAR)
    im2.save("/home/siddharth/Computer Vision/Data/Train_Negative/NegImage%d.jpg"%count)        
    count = count + 1