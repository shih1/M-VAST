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


DEBUG_PRINT = 0

#For Response Type One:; steveSlider.jpg
#it is a scale from 0 to 100 and the pixel pocatns are -556 to 546 
import conversion

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

#===================GUI FUNCTIONS===================
def mainGUI(myDlg):
    myDlg.addText('Stimulus Setup')
    myDlg.addField('Patient ID:' , '')
    myDlg.addField('Experimenter ID:' , '')
    myDlg.addField('Age:', '')
    myDlg.addField('Sex:', choices=["Male", "Female"])
    myDlg.addField('Output File' ,'output.csv')
    myDlg.addField('Input File' ,'input.csv')
    myDlg.addText(' ')
    myDlg.addField('Save or Start Experiment', choices =[ "Edit", "Start","Start from input file", "Save to output file"])
    myDlg.addText(' ')
    myDlg.addField('Stimulus Number',choices=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50"])

def secondGUI(myDlg, pastExperimentData, pastExperimentNumber):
    myDlg.addText('Stimulus ' + str(pastExperimentNumber) + ' settings')
    
    #Resting time is set before the rest because of the change to do Resting --> Anticipatory --> Stimulus for each experiment 
    
    #convert Past Experiment Data to variables 
    restingTime  = str(pastExperimentData[0])
    anticipatoryTime = str(pastExperimentData[1])
    stimulusType = str(pastExperimentData[2])
    stimulusDuration = str(pastExperimentData[3])
    stimulusFrequency = str(pastExperimentData[4])
    brightness = str(pastExperimentData[5])
    timeUntilRating = str(pastExperimentData[6])
    responseType = str(pastExperimentData[7])
    responseTime = str(pastExperimentData[8])
    
    
    myDlg.addText('Time before Visual Cue: ' + restingTime)  #RestingTime
    myDlg.addText('Visual Cue Duration: ' + anticipatoryTime)#anticipatoryTime
    myDlg.addText('Stimulus Type: ' + stimulusType)#stimulusType
    myDlg.addText('Stimulus Duration: ' + stimulusDuration) #stimulusDuration
    myDlg.addText('Stimulus Frequency: ' + stimulusFrequency) #stimulusFrequency
    myDlg.addText('Brightness: ' + brightness)  #Brightness
    myDlg.addText('Time until Rating: ' + timeUntilRating )  #Time until Rating
    myDlg.addText('Response Type: ' + responseType)  #ResponseType
    myDlg.addText('Response Time: ' + responseTime)  #ResponseTime
    
    myDlg.addText(' ')
    
    myDlg.addText('Stimulus Setup')
    myDlg.addField('Patient ID:' , '')
    myDlg.addField('Experimenter ID:' , '')
    myDlg.addField('Age:', '')
    myDlg.addField('Sex:', choices=["Male", "Female"])
    myDlg.addField('Output File' ,'output.csv')
    myDlg.addField('Input File' ,'input.csv')
    myDlg.addText(' ')
    myDlg.addField('Save or Start Experiment', choices =[ "Edit", "Start","Start from input file", "Save to output file"])
    myDlg.addText(' ')
    myDlg.addField('Stimulus Number',choices=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50"])


def createStimEdit(experimentNumber, myDlg): #myDlg2.data 
    myDlg.addText('Stimulus ' + str(experimentNumber) + ' Setup')#title
    
    myDlg.addField('Time before Visual Cue(s)','10')#myDlg.data[0]
    myDlg.addField('Visual Cue Duration(s):', '5')#myDlg.data[1]
    myDlg.addField('Stimulus Type:',choices=[Stim_0,Stim_1,Stim_2,Stim_3,Stim_4,Stim_5, Stim_6, Stim_7,Stim_8, Stim_9])#myDlg.data[2]
    myDlg.addField('Stimulus Duration (s):', '10')#myDlg.data[3]
    myDlg.addField('Stimulus Frequency (Hz):', '10')#myDlg.data[4]
    myDlg.addField('Brightness:', choices=["1.0", "0.9", "0.8", "0.7", "0.6", "0.5", "0.4", "0.3" , "0.2", "0.1", "0.0","random"])#myDlg.data[5]
    myDlg.addText(' ')
    myDlg.addText('ISI Specifications')
    myDlg.addField('Time until Rating(s):','0')#myDlg.data[6]
    myDlg.addField('Response Type:',choices=[Type_1,Type_2, Type_3, Type_4, Type_5, Type_6, Type_0])#myDlg.data[7]
    myDlg.addField('Response Time (s):', '10')#myDlg.data[8]
    myDlg.addField('Limit Response Time ?', choices = ["Yes", "No"]) #myDlg.data[9]
    ok_data_2 = myDlg.show()

def createSecondStimEdit(experimentNumber, myDlg, past_data):
    myDlg.addText('Stimulus ' + str(experimentNumber) + ' Setup')#title
    
    myDlg.addField('Time before Visual Cue(s)',past_data[0])#myDlg.data[0]
    myDlg.addField('Visual Cue Duration(s):', past_data[1])#myDlg.data[1]
    
    pastStimType = conversion.convertIntToStimulusType(past_data[2])

    myDlg.addField('Stimulus Type:',choices=[Stim_0,Stim_1,Stim_2,Stim_3,Stim_4,Stim_5, Stim_6, Stim_7,Stim_8, Stim_9])#myDlg.data[2]
    myDlg.addField('Stimulus Duration (s):', past_data[3])#myDlg.data[3]
    myDlg.addField('Stimulus Frequency (Hz):',past_data[4])#myDlg.data[4]
    myDlg.addField('Brightness:', choices=[past_data[5],"1.0", "0.9", "0.8", "0.7", "0.6", "0.5", "0.4", "0.3" , "0.2", "0.1", "0.0","random"])#myDlg.data[5]
    myDlg.addText(' ')
    myDlg.addText('ISI Specifications')
    myDlg.addField('Time until Rating(s):',past_data[6])#myDlg.data[6]
    
    pastResponseType = conversion.convertIntToResponseType(past_data[7])
    
    myDlg.addField('Response Type:',choices=[Type_1,Type_2, Type_3, Type_4, Type_5, Type_6, Type_0])#myDlg.data[7]
    myDlg.addField('Response Time (s):', past_data[8])#myDlg.data[8]
        
    pastCountdownOption = conversion.convertIntToResponseCountdown(past_data[9])

    myDlg.addField('Limit Response Time ?', choices = [pastCountdownOption, "Yes", "No"]) #myDlg.data[9]
    ok_data_2 = myDlg.show()
