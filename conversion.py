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

#GLOBAL VARIABLES
IMAGE_PATH_1 = u'DELL_XPS_15_Monitor/steveSliderINVERT.jpg'
DOUBLE_SLIDER = u'DELL_XPS_15_Monitor/double_slider.jpg'
BLUE_YELLOW = u'DELL_XPS_15_Monitor/blue_yellow.png'
YELLOW_BLUE = u'DELL_XPS_15_Monitor/yellow_blue.png'

BLACK = u'DELL_XPS_15_Monitor/BLACK.png'
WHITE = u'DELL_XPS_15_Monitor/WHITE.png'
GREEN_CROSS = u'DELL_XPS_15_Monitor/green_cross.png'


EDIT_BOOL = 0                   #user cancel edit?
START_BOOL = 0                  #user start?
MAX_STIMULUS = 50               #max stim num
MAX_PARAMETERS = 11             #parameters to set


#Response Types
Type_0 = "None"
Type_1 = "Brightness (0 -> 100)"
Type_2 = "Unpleasantness (0 -> 100)"
Type_3 = "Dual Scale (0 -> 100)"
Type_4 = "Affective (0 -> 20)"
Type_5 = "Sensory (0 -> 20)"
Type_6 = "Dual Scale (0 -> 20)"

#Stimulus Types
Stim_0 = "None"
Stim_1 = "Annular Checkerboard Black/White"
Stim_2 = "Annular Checkerboard Blue/Yellow"
Stim_3 = "Annular Checkerboard Red/Green"
Stim_4 = "Checkerboard Black/White"
Stim_5 = "Checkerboard Blue/Yellow"
Stim_6 = "Checkerboard Red/Green"
Stim_7 = "Strobe Light Black/White"
Stim_8 = "Strobe Light Blue/Yellow"
Stim_9 = "Strobe Light Red/Green"

#Yes/No
Yes = "Yes"
No = "No"

#===================CONVERTING VALUES AND STRINGS===================
def convertResponseTypeToInt(responseType):
    if responseType == Type_0:
        return 0
    elif responseType == Type_1: 
        return 1
    elif responseType == Type_2: 
        return 2
    elif responseType == Type_3: 
        return 3
    elif responseType == Type_4: 
        return 4
    elif responseType == Type_5: 
        return 5
    elif responseType == Type_6: 
        return 6
    else:
        return 9999

def convertIntToResponseType(responseType):
    if responseType == 0:
        return Type_0
    elif responseType == 1: 
        return Type_1
    elif responseType == 2: 
        return Type_2
    elif responseType == 3: 
        return Type_3
    elif responseType == 4: 
        return Type_4
    elif responseType == 5: 
        return Type_5
    elif responseType == 6: 
        return Type_6
    else:
        return "Invalid Response Type "

def convertStimulusTypeToInt(stimulusType):
    if stimulusType == Stim_0:
        return 0
    elif stimulusType == Stim_1: 
        return 1
    elif stimulusType == Stim_2: 
        return 2
    elif stimulusType == Stim_3: 
        return 3
    elif stimulusType == Stim_4: 
        return 4
    elif stimulusType == Stim_5: 
        return 5
    elif stimulusType == Stim_6: 
        return 6
    elif stimulusType == Stim_7: 
        return 7
    elif stimulusType == Stim_8: 
        return 8
    elif stimulusType == Stim_9: 
        return 9
    else:
        return 9999

def convertIntToStimulusType(stimulusType):
    if stimulusType == 0:
        return Stim_0
    elif stimulusType == 1: 
        return Stim_1
    elif stimulusType == 2: 
        return Stim_2
    elif stimulusType == 3: 
        return Stim_3
    elif stimulusType == 4: 
        return Stim_4
    elif stimulusType == 5: 
        return Stim_5
    elif stimulusType == 6: 
        return Stim_6
    elif stimulusType == 7: 
        return Stim_7
    elif stimulusType == 8: 
        return Stim_8
    elif stimulusType == 9: 
        return Stim_9
    else:
        return "Invalid Stimulus Type "



def convertResponseCountdownToInt(responseCountdown):
    if responseCountdown == Yes:
        return 1
    else:
        return 0
        
def convertIntToResponseCountdown(responseCountdown):
    if responseCountdown == 1:
        return Yes
    else:
        return No
        
        
#Returns output Matrix
def dlgDataToMatrix(experimentNumber,dataArray):
    
    #dataArray is myDlg.data
    #experimentNumber is the experiment just edited
    restingTime  =          dataArray[0]
    anticipatoryTime =      dataArray[1]
    stimulusType =          dataArray[2]
    stimulusDuration =      dataArray[3]
    stimulusFrequency =     dataArray[4]
    brightness =            dataArray[5]
    timeUntilRating =       dataArray[6]
    responseType =          dataArray[7]
    responseTime =          dataArray[8]
    responseCountdown =     dataArray[9]
    
    outputMatrix = np.zeros( (1 , MAX_PARAMETERS) )
    outputMatrix[0][0] = restingTime #restingTime
    outputMatrix[0][1] = anticipatoryTime #anticipatoryTime
    outputMatrix[0][2] = convertStimulusTypeToInt(stimulusType) #stimulusType
    outputMatrix[0][3] = stimulusDuration #stimulusDuration
    outputMatrix[0][4] = stimulusFrequency #stimulusFrequency
    outputMatrix[0][5] = brightness #brightness
    outputMatrix[0][6] = timeUntilRating #timeUntilRating
    outputMatrix[0][7] = convertResponseTypeToInt(responseType) #responseType
    outputMatrix[0][8] = responseTime #ResponseTime
    outputMatrix[0][9] = convertResponseCountdownToInt(responseCountdown)#Response Countdown
    outputMatrix[0][10] = experimentNumber #expimentNumber
        
    return outputMatrix

#===================MATHEMATICAL CONVERSIONS===================
def convertFreqToTime(frequency):
    time = 1/(2 * frequency)
    
    print('time')
    print(time)
    return  time#time to display each image
    
    
def convertDurationToRepetitions(frequency, duration):
    reps = duration * frequency

    print('reps')
    print(reps)
    return reps #number of times to repeat to reach final time

def convertResponseTypeOneMouseToNumber(number):
    return int((number + 556) * 100 / 1102) 
