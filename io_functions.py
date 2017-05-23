from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding

from psychopy import gui

import csv
import datetime

#For Response Type One:; steveSlider.jpg
#it is a scale from 0 to 100 and the pixel pocatns are -556 to 546 

EDIT_BOOL = 0                   #user cancel edit?
START_BOOL = 0                  #user start?
MAX_STIMULUS = 50               #max stim num
MAX_PARAMETERS = 11             #parameters to set

#===================MISCELANEOUS FUNCTIONS===================
def runFromFile(filename):
    experimentMatrix = np.zeros((MAX_STIMULUS+1, MAX_PARAMETERS))
    
    
    file = open(filename)
    numline = len(file.readlines())
    

    with open(filename, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        
        filler = spamreader.next()
        
        for row_count in range(0,numline-1):
            row_data = spamreader.next()
            
            for col_count in range(0, MAX_PARAMETERS):
                experimentMatrix[row_count + 1][col_count] = row_data[col_count]#restingTime
                

    return experimentMatrix



def createOutputFile(filename):  #returns the editor object
    t = datetime.date.today()
    dateAndTime = datetime.datetime.now()
    filename = str(t) + '_' + str(dateAndTime.hour) + '_' + str(dateAndTime.minute) + '.csv'
    with open(filename, 'wb') as csvfile:
        write2file = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        write2file.writerow(u'PsychoPy Experiment made by Christopher Shih 2016 cjshih@umich.edu christophershih2@gmail.com 734 757 3501' )
        write2file.writerow(str(dateAndTime))