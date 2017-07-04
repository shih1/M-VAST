from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os, sys # to get file system encoding
from psychopy import gui
import gui_functions, conversion, io_functions, csv, datetime

#Image Paths
ANTICIPATE = u'EIZO_Monitor/anticipate.png'

CHECKER_BW = u'EIZO_Monitor/checker_bw.png'
CHECKER_BY = u'EIZO_Monitor/checker_by.png'
CHECKER_RG = u'EIZO_Monitor/checker_rg.png'
CHECKER_BW_ = u'EIZO_Monitor/checker_bw_.png'
CHECKER_BY_ = u'EIZO_Monitor/checker_by_.png'
CHECKER_RG_ = u'EIZO_Monitor/checker_rg_.png'

ACHECK_BW = u'EIZO_Monitor/acheck_bw.png'
ACHECK_BY = u'EIZO_Monitor/acheck_by.png'
ACHECK_RG = u'EIZO_Monitor/acheck_rg.png'
ACHECK_BW_ = u'EIZO_Monitor/acheck_bw_.png'
ACHECK_BY_ = u'EIZO_Monitor/acheck_by_.png'
ACHECK_RG_ = u'EIZO_Monitor/acheck_rg_.png'

AFFECTIVE20 = u'EIZO_Monitor/affective20.png'
SENSORY20 = u'EIZO_Monitor/sensory20.png'
DOUBLESLIDER20 = u'EIZO_Monitor/doubleSlider20.png'

UNPLEASANT100 = u'EIZO_Monitor/unpleasant100.png'
BRIGHTNESS100 = u'EIZO_Monitor/brightness100.png'
DOUBLESLIDER100 = u'EIZO_Monitor/doubleSlider100.png'

STROBE_BLACK = u'EIZO_Monitor/strobe_black.png'
STROBE_WHITE = u'EIZO_Monitor/strobe_white.png'
STROBE_BLUE = u'EIZO_Monitor/strobe_blue.png'
STROBE_YELLOW = u'EIZO_Monitor/strobe_yellow.png'
STROBE_GREEN = u'EIZO_Monitor/strobe_green.png'
STROBE_RED = u'EIZO_Monitor/strobe_red.png'

MONITOR_WIDTH = 1600
MONITOR_HEIGHT = 1200

DEBUG_PRINT = 1
UNUSED_RATING = 555
INCOMPLETE_RATING = 999    
resp_brightness = 0.5
fixed_offset = 0

EDIT_BOOL = 0                   #user cancel edit?
START_BOOL = 0                  #user start?
MAX_STIMULUS = 50               #max stim num
MAX_PARAMETERS = 11             #parameters to set



#===================STIMULUS FUNCTIONS===================
def timedImage(picturePath, timed_duration):  #timedImage(GREEN_CROSS, 10) 
    """
        This function displays a picture located at <picturePath> for <timed_duration>.

        Inputs: 
            picturePath(str): path to picture (.jpg, .png, .bmp, etc)
            timed_duration(double): duration of image (multiple of 1/60) 
    """

    duration_of_timed_window = timed_duration
    x_timed_position = 0
    y_timed_position = 0
    x_timed_width = MONITOR_WIDTH
    y_timed_height = MONITOR_HEIGHT

    #Image Stimulus
    timed_window_image = visual.ImageStim(win=win, name='timed_window_image',
        image= picturePath, mask=None,
        ori=0, pos=[ x_timed_position, y_timed_position ], size=[x_timed_width, y_timed_height ],
        color=[1,1,1], colorSpace='rgb',
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)

    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(timed_window_image)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *timed_window_image* updates
        if t >= 0.0 and timed_window_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            timed_window_image.tStart = t  # underestimates by a little under one frame
            timed_window_image.frameNStart = frameN  # exact frame index
            timed_window_image.setAutoDraw(True)
        if timed_window_image.status == STARTED and t >= (0.0 + (duration_of_timed_window - win.monitorFramePeriod*0.75)): #most of one frame period left
            timed_window_image.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
            
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    routineTimer.reset()

def timedWindowText(text, duration):
    """
        Displays <text> for <duration>s

        Inputs:
            text(str): Text to be displayed
            duration(double): Duration of text (multiple of 1/60) 
    """
    text = visual.TextStim(win=win, ori=0, name='text',
    text=text,    font=u'Arial',
    pos=[0, 0], height=20, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)
    
    #Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(duration)
    # update component parameters for each repeat
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(text)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t  # underestimates by a little under one frame
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        if text.status == STARTED and t >= (fixed_offset + (duration-win.monitorFramePeriod*0.75)): #most of one frame period left
            text.setAutoDraw(False)
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

def doubleSlider(backgroundImagePath,responseType):#,minimumLocation,maximumLocation, ResponseType): #returns the x position of the mouse 
    """
        Creates an UNTIMED and HORIZONTAL double slider. 
        This is specifically calibrated for a specific image. 
        Right Click: Sets slider
        Left Click: Unsets slider
        Inputs:
            backgroundImagePath(str): Background Image path
            responseType(int): Deprecated input variable. Must always be set to 1. 
    """
    POLYGON1_Y = 280
    POLYGON2_Y = -342
    
    MIN_X = -646
    MAX_X = 610
    RECT_LENGTH = MAX_X - MIN_X
    
    top_slider_state = 0
    bottom_slider_state = 0
    complete_state = 0 
    
    image =  visual.ImageStim(win=win, name='image',units='pix', 
        image=backgroundImagePath, mask=None,
        ori=0, pos=[0, 0], size=[MONITOR_WIDTH,MONITOR_HEIGHT],
        color=[1,1,1], colorSpace='rgb', opacity=resp_brightness,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-1.0)
     
    squeak = event.Mouse(visible = True, newPos = None, win = win)
    squeakState = [0,0,0]
    #------Prepare to start Routine "trial"-------
    t = 0

    frameN = -1
    # update component parameters for each repeat
    # keep track of which components have finished
    polygon1 = visual.ShapeStim(win=win, name='polygon1',units='pix', 
        vertices = ( (-50,50) , (50,50) , (0,0) ),
        ori=0, pos=[0, POLYGON1_Y],
        lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
        fillColor=[1,-1,-1], fillColorSpace='rgb',
        opacity=resp_brightness,depth=-2.0, 
        interpolate=True)
        
    polygon2 = visual.ShapeStim(win=win, name='polygon2',units='pix', 
        vertices = ( (-50,50) , (50,50) , (0,0) ),
        ori=0, pos=[0,  POLYGON2_Y],
        lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
        fillColor=[1,-1,-1], fillColorSpace='rgb',
        opacity=resp_brightness,depth=-2.0, 
        interpolate=True)
        
    polygon3 = visual.Rect(win=win, name='polygon3',units='pix', 
        width = RECT_LENGTH, height = 10,
        ori=0, pos=[0,  0],
        lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
        fillColor=[-1,-1,1], fillColorSpace='rgb',
        opacity=resp_brightness,depth=-2.0, 
        interpolate=True)
        
    #-------Start Routine "trial"-------
    
    continueRoutine = True

    while continueRoutine and complete_state == 0:
        #take position and button states 
        
        squeakPosition = squeak.getPos()
        squeakState = squeak.getPressed()
        
        if responseType == 1:
            if squeakPosition[0] < MIN_X:
                squeakPosition[0] = MIN_X
            elif squeakPosition[0] > MAX_X:
                squeakPosition[0] = MAX_X
        
        
        #move the slider along the slider position
        if squeakPosition[1] > 0:
            if top_slider_state == 0: 
                top_slider_text = (squeakPosition[0] - MIN_X) * 100 /RECT_LENGTH
                polygon1.pos = [squeakPosition[0], POLYGON1_Y]
                polygon3.pos = [-10, POLYGON1_Y]
        elif squeakPosition[1] < 0:
            if bottom_slider_state == 0: 
                bottom_slider_text = (squeakPosition[0] - MIN_X) * 100 /RECT_LENGTH
                polygon2.pos = [squeakPosition[0], POLYGON2_Y]
                polygon3.pos = [-10, POLYGON2_Y]
        
        #Check for LMB Click
        if squeakState[0] == 1 and squeakPosition[1] > 0: #check for top completion
            top_slider_state = 1 
        
        if squeakState[0] == 1 and squeakPosition[1] < 0: #check for bottom completion
            bottom_slider_state = 1
        
        #Check for RMB Click
        if squeakState[2] == 1 and squeakPosition[1] > 0: #check for top completion
            top_slider_state = 0 
        
        if squeakState[2] == 1 and squeakPosition[1] < 0: #check for bottom completion
            bottom_slider_state = 0
            
        if top_slider_state == 1 and bottom_slider_state == 1: #check for final trial completion
            complete_state = 1 
        

        # get current time
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        
        # *polygon1* updates
        if t >= 0.0 and polygon1.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon1.tStart = t  # underestimates by a little under one frame
            polygon1.frameNStart = frameN  # exact frame index
            polygon1.setAutoDraw(True)
        # *polygon2* updates
        if t >= 0.0 and polygon2.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon2.tStart = t  # underestimates by a little under one frame
            polygon2.frameNStart = frameN  # exact frame index
            polygon2.setAutoDraw(True)
        # *polygon3* updates
        if t >= 0.0 and polygon3.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon3.tStart = t  # underestimates by a little under one frame
            polygon3.frameNStart = frameN  # exact frame index
            polygon3.setAutoDraw(True)
        # *ISI* period

        # check for quit (the Esc key)
        if event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
       
    
    polygon1.setAutoDraw(False)
    polygon2.setAutoDraw(False)
    polygon3.setAutoDraw(False)
    image.setAutoDraw(False)
    
    data_output = np.zeros((1,3))

    t = trialClock.getTime()
    
    if complete_state: 
        data_output[0,0] = int(top_slider_text)
        data_output[0,1] = int(bottom_slider_text)
        data_output[0,2] = t
    else: 
        data_output[0,0] = INCOMPLETE_RATING
        data_output[0,1] = INCOMPLETE_RATING
        data_output[0,2] = t
        
    squeak = event.Mouse(visible = False, newPos = None, win = win)

    return data_output
    
def timedDoubleSlider(backgroundImagePath, responseType, responseDuration):#,minimumLocation,maximumLocation, ResponseType): #returns the x position of the mouse 
    """
        Creates a TIMED and HORIZONTAL double slider for <responseDuration>. 
        This is specifically calibrated for a specific image. 
        Right Click: Sets slider
        Left Click: Unsets slider
        Inputs:
            backgroundImagePath(str): Background Image path
            responseType(int): Deprecated input variable. Must always be set to 1. 
            responseDuration(double): Duration of Response. If failed to set before
                <responseDuration> seconds, the value will be set to global INCOMPLETE_DURATION
    """
     
    POLYGON1_Y = 280
    POLYGON2_Y = -342
    
    MIN_X = -646
    MAX_X = 610
    RECT_LENGTH = MAX_X - MIN_X
    
    top_slider_state = 0
    bottom_slider_state = 0
    complete_state = 0 
    
    image =  visual.ImageStim(win=win, name='image',units='pix', 
        image=backgroundImagePath, mask=None,
        ori=0, pos=[0, 0], size=[MONITOR_WIDTH,MONITOR_HEIGHT],
        color=[1,1,1], colorSpace='rgb', opacity=resp_brightness,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-1.0)
    
        
    squeak = event.Mouse(visible = True, newPos = None, win = win)
    squeakState = [0,0,0]

    # update component parameters for each repeat
    # keep track of which components have finished
    polygon1 = visual.ShapeStim(win=win, name='polygon1',units='pix', 
        vertices = ( (-50,50) , (50,50) , (0,0) ),
        ori=0, pos=[0, POLYGON1_Y],
        lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
        fillColor=[1,-1,-1], fillColorSpace='rgb',
        opacity=resp_brightness,depth=-2.0, 
        interpolate=True)
        
    polygon2 = visual.ShapeStim(win=win, name='polygon2',units='pix', 
        vertices = ( (-50,50) , (50,50) , (0,0) ),
        ori=0, pos=[0,  POLYGON2_Y],
        lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
        fillColor=[1,-1,-1], fillColorSpace='rgb',
        opacity=resp_brightness,depth=-2.0, 
        interpolate=True)
        
    polygon3 = visual.Rect(win=win, name='polygon3',units='pix', 
        width = RECT_LENGTH, height = 10,
        ori=0, pos=[0,  0],
        lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
        fillColor=[-1,-1,1], fillColorSpace='rgb',
        opacity=resp_brightness,depth=-2.0, 
        interpolate=True)
        

    #-------Start Routine "trial"-------
    continueRoutine = True
    
    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
    t = 0
    frameN = -1
    rectTimer(responseDuration, t, True, False, False)


    while continueRoutine and complete_state == 0:
        #take position and button states 
        
        squeakPosition = squeak.getPos()
        squeakState = squeak.getPressed()
        
        
        if responseType == 1:
            if squeakPosition[0] < MIN_X:
                squeakPosition[0] = MIN_X
            elif squeakPosition[0] > MAX_X:
                squeakPosition[0] = MAX_X
        
        
        #move the slider along the slider position
        if squeakPosition[1] > 0:
            if top_slider_state == 0: 
                top_slider_text = (squeakPosition[0] - MIN_X) * 100 /RECT_LENGTH
                polygon1.pos = [squeakPosition[0], POLYGON1_Y]
                polygon3.pos = [-10, POLYGON1_Y]
        elif squeakPosition[1] < 0:
            if bottom_slider_state == 0: 
                bottom_slider_text = (squeakPosition[0] - MIN_X) * 100 /RECT_LENGTH
                polygon2.pos = [squeakPosition[0], POLYGON2_Y]
                polygon3.pos = [-10, POLYGON2_Y]
        #Check for LMB Click
        if squeakState[0] == 1 and squeakPosition[1] > 0: #check for top completion
            top_slider_state = 1 
        
        if squeakState[0] == 1 and squeakPosition[1] < 0: #check for bottom completion
            bottom_slider_state = 1
        
        #Check for RMB Click
        if squeakState[2] == 1 and squeakPosition[1] > 0: #check for top completion
            top_value = 9999
            top_slider_state = 0 
        
        if squeakState[2] == 1 and squeakPosition[1] < 0: #check for bottom completion
            bottom_value = 9999
            bottom_slider_state = 0
            
        if top_slider_state == 1 and bottom_slider_state == 1: #check for final trial completion
            complete_state = 1 
        

        # get current time
        t = trialClock.getTime()

        rectTimer(responseDuration, t, False, True, False)

        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        
        if image.status == STARTED and t >= (fixed_offset + (responseDuration - win.monitorFramePeriod*0.75)): #most of one frame period left
            image.setAutoDraw(False)
            top_value = 99999
            bottom_value = 99999
            continueRoutine = False
            
        # *polygon1* updates
        if t >= 0.0 and polygon1.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon1.tStart = t  # underestimates by a little under one frame
            polygon1.frameNStart = frameN  # exact frame index
            polygon1.setAutoDraw(True) 
        # *polygon2* updates
        if t >= 0.0 and polygon2.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon2.tStart = t  # underestimates by a little under one frame
            polygon2.frameNStart = frameN  # exact frame index
            polygon2.setAutoDraw(True)
        # *polygon3* updates
        if t >= 0.0 and polygon3.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon3.tStart = t  # underestimates by a little under one frame
            polygon3.frameNStart = frameN  # exact frame index
            polygon3.setAutoDraw(True)
        # *ISI* period

        # check for quit (the Esc key)
        if event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
       
    
    #print('mouseBox FunctionComplete')
    polygon1.setAutoDraw(False)
    polygon2.setAutoDraw(False)
    polygon3.setAutoDraw(False)
    image.setAutoDraw(False)
    rectTimer(responseDuration, t, False, False, True)

    data_output = np.zeros((1,3))

    t = trialClock.getTime()
    if complete_state: 
        data_output[0,0] = int(top_slider_text)
        data_output[0,1] = int(bottom_slider_text)
        data_output[0,2] = t
    else: 
        data_output[0,0] = INCOMPLETE_RATING
        data_output[0,1] = INCOMPLETE_RATING
        data_output[0,2] = t

    squeak = event.Mouse(visible = False, newPos = None, win = win)

    return data_output
        
def singleSlider(backgroundImagePath,responseType):#,minimumLocation,maximumLocation, ResponseType): #returns the x position of the mouse ] 
    """
        Creates an UNTIMED and HORIZONTAL single slider. 
        This is specifically calibrated for a specific image. 
        Right Click: Sets slider
        Left Click: There is no undo functinality for a single slider

        Inputs:
            backgroundImagePath(str): Background Image path
            responseType(int): Deprecated input variable. Must always be set to 1. 
    """
    
    MIN_X = -646
    MAX_X = 610
    Y_POS = -18
    RECT_LENGTH = MAX_X - MIN_X
    image =  visual.ImageStim(win=win, name='image',units='pix', 
        image=backgroundImagePath, mask=None,
        ori=0, pos=[0, 0], size=[MONITOR_WIDTH,MONITOR_HEIGHT],
        color=[1,1,1], colorSpace='rgb', opacity=resp_brightness,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-1.0)
            
    squeak = event.Mouse(visible = True, newPos = None, win = win)
    squeakState = [0,0,0]

    # update component parameters for each repeat
    # keep track of which components have finished
    polygon = visual.ShapeStim(win=win, name='polygon',units='pix', 
        vertices = ( (-50,50) , (50,50) , (0,0) ),
        ori=0, pos=[0, Y_POS],
        lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
        fillColor=[1,-1,-1], fillColorSpace='rgb',
        opacity=resp_brightness,depth=-2.0, 
        interpolate=True)
    #-------Start Routine "trial"-------
    
    continueRoutine = True
    #------Prepare to start Routine "trial"-------
    t = 0
    frameN = -1
    
    while continueRoutine and squeakState[0] == 0:
        
        squeakPosition = squeak.getPos()
        squeakState = squeak.getPressed()
        
        if responseType == 1:
            if squeakPosition[0] < MIN_X:
                squeakPosition[0] = MIN_X
            elif squeakPosition[0] > MAX_X:
                squeakPosition[0] = MAX_X
        displayText = int( ( squeakPosition[0] - MIN_X) * 100 /RECT_LENGTH )
                        
        polygon.pos = [squeakPosition[0], Y_POS]
        
        
        # get current time
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        
        # *polygon* updates
        if t >= 0.0 and polygon.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon.tStart = t  # underestimates by a little under one frame
            polygon.frameNStart = frameN  # exact frame index
            polygon.setAutoDraw(True)
        # *ISI* period

        # check for quit (the Esc key)
        if event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    polygon.setAutoDraw(False)
    image.setAutoDraw(False)
    squeak = event.Mouse(visible = False, newPos = None, win = win)

    data_output = np.zeros((1,3))

    t = trialClock.getTime()
    
    data_output[0,0] = displayText
    data_output[0,1] = UNUSED_RATING
    data_output[0,2] = t
    
    return data_output

def timedSingleSlider(backgroundImagePath, responseType, responseDuration):
    """
        Creates a TIMED and HORIZONTAL single slider for <responseDuration>. 
        This is specifically calibrated for a specific image. 
        Right Click: Sets slider
        Left Click: Unsets slider
        Inputs:
            backgroundImagePath(str): Background Image path
            responseType(int): Deprecated input variable. Must always be set to 1. 
            responseDuration(double): Duration of Response. If failed to set before
                <responseDuration> seconds, the value will be set to global INCOMPLETE_DURATION
    """
    
    MIN_X = -646
    MAX_X = 610
    Y_POS = -18
    RECT_LENGTH = MAX_X - MIN_X
    image =  visual.ImageStim(win=win, name='image',units='pix', 
        image=backgroundImagePath, mask=None,
        ori=0, pos=[0, 0], size=[MONITOR_WIDTH,MONITOR_HEIGHT],
        color=[1,1,1], colorSpace='rgb', opacity=resp_brightness,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-1.0)
    
    
    squeak = event.Mouse(visible = True, newPos = None, win = win)
    squeakState = [0,0,0]
    
    # update component parameters for each repeat
    # keep track of which components have finished
    polygon = visual.ShapeStim(win=win, name='polygon',units='pix', 
        vertices = ( (-50,50) , (50,50) , (0,0) ),
        ori=0, pos=[0, Y_POS],
        lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
        fillColor=[1,-1,-1], fillColorSpace='rgb',
        opacity=resp_brightness,depth=-2.0, 
        interpolate=True)
    #-------Start Routine "trial"-------
    
    rectTime = visual.Rect(win=win, name='rectTime',units='pix', 
        width = MONITOR_WIDTH - 200 , height = 10,
        ori=0, pos=[0, MONITOR_HEIGHT/2-5],
        lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
        fillColor=[-1,-1,1], fillColorSpace='rgb',
        opacity=resp_brightness,depth=-2.0, 
        interpolate=True)
    t = 0
    rectTimer(responseDuration, t, True, False, False)

    displayText = 0
    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
    #------Prepare to start Routine "trial"-------
    trialClock.reset()  # clock 
    globalClock.reset()
    routineTimer.reset()
    frameN = -1
    
    trialComponents = []
    trialComponents.append(image)
    
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    continueRoutine = True
    complete_state = 0
    while continueRoutine and squeakState[0] == 0:
        squeakPosition = squeak.getPos()
        squeakState = squeak.getPressed()
        rectTime.width = (MONITOR_WIDTH - 200)/2 -((MONITOR_WIDTH - 200)/2) / responseDuration * (t)

        if responseType == 1:
            if squeakPosition[0] < MIN_X:
                squeakPosition[0] = MIN_X
            elif squeakPosition[0] > MAX_X:
                squeakPosition[0] = MAX_X
        displayText = int( ( squeakPosition[0] - MIN_X) * 100 /RECT_LENGTH )
                
        polygon.pos = [squeakPosition[0], Y_POS]        
        # get current time
        # update/draw components on each frame
        
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        rectTimer(responseDuration, t, False, True, False)

        # *timed_window_image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        if image.status == STARTED and t >= (fixed_offset + (responseDuration - win.monitorFramePeriod*0.75)): #most of one frame period left
            image.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
            
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        
        # *polygon* updates
        if t >= 0.0 and polygon.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon.tStart = t  # underestimates by a little under one frame
            polygon.frameNStart = frameN  # exact frame index
            polygon.setAutoDraw(True)
            
                    # *polygon* updates
        if t >= 0.0 and rectTime.status == NOT_STARTED:
            # keep track of start time/frame for later
            rectTime.tStart = t  # underestimates by a little under one frame
            rectTime.frameNStart = frameN  # exact frame index
            rectTime.setAutoDraw(True)
            # *ISI* period

        # check for quit (the Esc key)
        if event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            
    
    if squeakState[0] == 1: 
            complete_state = 1    
            
    polygon.setAutoDraw(False)
    image.setAutoDraw(False)
    rectTime.setAutoDraw(False)
    rectTimer(responseDuration, t, False, False, True)

    squeak = event.Mouse(visible = False, newPos = None, win = win)

    data_output = np.zeros((1,3))

    t = trialClock.getTime()
    
    if complete_state == 1:
        data_output[0,0] = displayText
        data_output[0,1] = UNUSED_RATING
        data_output[0,2] = t
    elif complete_state == 0: 
        data_output[0,0] = INCOMPLETE_RATING
        data_output[0,1] = UNUSED_RATING
        data_output[0,2] = t
        
    return data_output

def rectTimer(duration, t, instantiate, update, end):
    global rectTime
    """
        Creates a blue rectangle that linearly converges to the center of the monitor over <duration>. 
        Used for timed sliders. 
        Inputs: 
            duration(double): Duration of slider 
            t(double): Current Slider Time
            instantiate(bool): Create rect object
            update(bool): Update Width
            end(bool): set autodraw to False 
    """
    if instantiate:
        rectTime = visual.Rect(win=win, name='rectTime',units='pix', 
            width = MONITOR_WIDTH - 200 , height = 10,
            ori=0, pos=[0, 0],#MONITOR_HEIGHT/2-5],
            lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
            fillColor=[-1,-1,1], fillColorSpace='rgb',
            opacity=resp_brightness,depth=-2.0, 
            interpolate=True)
        rectTime.setAutoDraw(True)

    if update: 

        rectTime.width = (MONITOR_WIDTH - 200)/2 -((MONITOR_WIDTH - 200)/2) / duration * (t)
        print (MONITOR_WIDTH - 200)/2 -((MONITOR_WIDTH - 200)/2) / duration * (t)
        rectTime.setAutoDraw(True)

    if end:
        rectTime.setAutoDraw(False)

#=============#

def verticalDoubleSlider(backgroundImagePath,responseType):#,minimumLocation,maximumLocation, ResponseType): #returns the x position of the mouse 
    """
        Creates an UNTIMED and VERTICAL double slider for <responseDuration>. 
        This is specifically calibrated for a specific image. 
        Right Click: Sets slider
        Left Click: Unsets slider
        Inputs:
            backgroundImagePath(str): Background Image path
            responseType(int): Deprecated input variable. Must always be set to 1. 
    """
    POLYGON1_X = -72
    POLYGON2_X = 74
    
    MIN_Y = -543
    MAX_Y = 497
    RECT_LENGTH = MAX_Y - MIN_Y
    
    top_slider_state = 0
    bottom_slider_state = 0
    complete_state = 0 
    
    image =  visual.ImageStim(win=win, name='image',units='pix', 
        image=backgroundImagePath, mask=None,
        ori=0, pos=[0, 0], size=[MONITOR_WIDTH,MONITOR_HEIGHT],
        color=[1,1,1], colorSpace='rgb', opacity=resp_brightness,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-1.0)
    
        
    squeak = event.Mouse(visible = True, newPos = None, win = win)
    squeakState = [0,0,0]
    #------Prepare to start Routine "trial"-------
    t = 0

    frameN = -1
    # update component parameters for each repeat
    # keep track of which components have finished
    polygon1 = visual.ShapeStim(win=win, name='polygon1',units='pix', 
        vertices = ( (50,-50) , (50,50) , (0,0) ),
        ori=0, pos=[POLYGON1_X,0],
        lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
        fillColor=[1,-1,-1], fillColorSpace='rgb',
        opacity=1,depth=-2.0, 
        interpolate=True)
        
    polygon2 = visual.ShapeStim(win=win, name='polygon2',units='pix', 
        vertices = ( (-50,50) , (-50,-50) , (0,0) ),
        ori=0, pos=[POLYGON2_X,0],
        lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
        fillColor=[1,-1,-1], fillColorSpace='rgb',
        opacity=resp_brightness,depth=-2.0, 
        interpolate=True)
        
    polygon3 = visual.Rect(win=win, name='polygon3',units='pix', 
        width = 10, height = RECT_LENGTH,
        ori=0, pos=[0,  0],
        lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
        fillColor=[-1,-1,1], fillColorSpace='rgb',
        opacity=resp_brightness,depth=-2.0, 
        interpolate=True)
        
    
    continueRoutine = True

    while continueRoutine and complete_state == 0:
        #take position and button states 
        
        squeakPosition = squeak.getPos()
        squeakState = squeak.getPressed()
        
        if responseType == 1:
            if squeakPosition[1] < MIN_Y:
                squeakPosition[1] = MIN_Y
            elif squeakPosition[1] > MAX_Y:
                squeakPosition[1] = MAX_Y
        
        
        #move the slider along the slider position
        if squeakPosition[0] > 0:
            if bottom_slider_state == 0: 
                bottom_slider_text = (squeakPosition[1] - MIN_Y) * 21 /RECT_LENGTH
                polygon2.pos = [POLYGON2_X , squeakPosition[1]]
                polygon3.pos = [POLYGON2_X,-20]
        elif squeakPosition[0] < 0:
            if top_slider_state == 0: 
                top_slider_text = (squeakPosition[1] - MIN_Y) * 21 /RECT_LENGTH
                polygon1.pos = [ POLYGON1_X, squeakPosition[1]]
                polygon3.pos = [POLYGON1_X,-20]

        
        #Check for LMB Click
        if squeakState[0] == 1 and squeakPosition[0] < 0: #check for top completion
            top_slider_state = 1 
        
        if squeakState[0] == 1 and squeakPosition[0] > 0: #check for bottom completion
            bottom_slider_state = 1
        
        #Check for RMB Click
        if squeakState[2] == 1 and squeakPosition[0] < 0: #check for top completion
            top_slider_text = 9999
            top_slider_state = 0 
        
        if squeakState[2] == 1 and squeakPosition[0] > 0: #check for bottom completion
            bottom_slider_text = 9999
            bottom_slider_state = 0
            
        if top_slider_state == 1 and bottom_slider_state == 1: #check for final trial completion
            complete_state = 1 
        

        # get current time
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        
        # *polygon1* updates
        if t >= 0.0 and polygon1.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon1.tStart = t  # underestimates by a little under one frame
            polygon1.frameNStart = frameN  # exact frame index
            polygon1.setAutoDraw(True)
        # *polygon2* updates
        if t >= 0.0 and polygon2.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon2.tStart = t  # underestimates by a little under one frame
            polygon2.frameNStart = frameN  # exact frame index
            polygon2.setAutoDraw(True)
        # *polygon3* updates
        if t >= 0.0 and polygon3.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon3.tStart = t  # underestimates by a little under one frame
            polygon3.frameNStart = frameN  # exact frame index
            polygon3.setAutoDraw(True)
        # *ISI* period

        # check for quit (the Esc key)
        if event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
       
    
    polygon1.setAutoDraw(False)
    polygon2.setAutoDraw(False)
    polygon3.setAutoDraw(False)
    image.setAutoDraw(False)
    
    
    data_output = np.zeros((1,3))

    t = trialClock.getTime()
    
    if complete_state: 
        data_output[0,0] = int(top_slider_text)
        data_output[0,1] = int(bottom_slider_text)
        data_output[0,2] = t
    else: 
        data_output[0,0] = INCOMPLETE_RATING
        data_output[0,1] = INCOMPLETE_RATING
        data_output[0,2] = t
        
    squeak = event.Mouse(visible = False, newPos = None, win = win)

    return data_output

def verticalTimedDoubleSlider(backgroundImagePath, responseType, responseDuration):#,minimumLocation,maximumLocation, ResponseType): #returns the x position of the mouse 
    """
        Creates a TIMED and VERTICAL double slider for <responseDuration>. 
        This is specifically calibrated for a specific image. 
        Right Click: Sets slider
        Left Click: Unsets slider
        Inputs:
            backgroundImagePath(str): Background Image path
            responseType(int): Deprecated input variable. Must always be set to 1. 
            responseDuration(double): Duration of Response. If failed to set before
                <responseDuration> seconds, the value will be set to global INCOMPLETE_DURATION
    """
     
    POLYGON1_X = -72
    POLYGON2_X = 74
    
    MIN_Y = -543
    MAX_Y = 497
    RECT_LENGTH = MAX_Y - MIN_Y
    
    top_slider_state = 0
    bottom_slider_state = 0
    complete_state = 0 
    
    image =  visual.ImageStim(win=win, name='image',units='pix', 
        image=backgroundImagePath, mask=None,
        ori=0, pos=[0, 0], size=[MONITOR_WIDTH,MONITOR_HEIGHT],
        color=[1,1,1], colorSpace='rgb', opacity=resp_brightness,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-1.0)
    
        
    squeak = event.Mouse(visible = True, newPos = None, win = win)
    squeakState = [0,0,0]
    #------Prepare to start Routine "trial"-------
    t = 0

    frameN = -1
    # update component parameters for each repeat
    # keep track of which components have finished
    polygon1 = visual.ShapeStim(win=win, name='polygon1',units='pix', 
        vertices = ( (50,-50) , (50,50) , (0,0) ),
        ori=0, pos=[POLYGON1_X,0],
        lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
        fillColor=[1,-1,-1], fillColorSpace='rgb',
        opacity=resp_brightness,depth=-2.0, 
        interpolate=True)
        
    polygon2 = visual.ShapeStim(win=win, name='polygon2',units='pix', 
        vertices = ( (-50,50) , (-50,-50) , (0,0) ),
        ori=0, pos=[POLYGON2_X,0],
        lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
        fillColor=[1,-1,-1], fillColorSpace='rgb',
        opacity=resp_brightness,depth=-2.0, 
        interpolate=True)
        
    polygon3 = visual.Rect(win=win, name='polygon3',units='pix', 
        width = 10, height = RECT_LENGTH,
        ori=0, pos=[0,  0],
        lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
        fillColor=[-1,-1,1], fillColorSpace='rgb',
        opacity=resp_brightness,depth=-2.0, 
        interpolate=True)
    
    continueRoutine = True
    rectTimer(responseDuration, t, True, False, False)

    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
    t = 0
    frameN = -1

    while continueRoutine and complete_state == 0:
        #take position and button states 
        
        squeakPosition = squeak.getPos()
        squeakState = squeak.getPressed()
        
        
        if responseType == 1:
            if squeakPosition[1] < MIN_Y:
                squeakPosition[1] = MIN_Y
            elif squeakPosition[1] > MAX_Y:
                squeakPosition[1] = MAX_Y
        
        
        #move the slider along the slider position
        if squeakPosition[0] > 0:
            if bottom_slider_state == 0: 
                bottom_slider_text = (squeakPosition[1] - MIN_Y) * 20 /RECT_LENGTH
                polygon2.pos = [POLYGON2_X , squeakPosition[1]]
                polygon3.pos = [POLYGON2_X,-20]
        elif squeakPosition[0] < 0:
            if top_slider_state == 0: 
                top_slider_text = (squeakPosition[1] - MIN_Y) * 20 /RECT_LENGTH
                polygon1.pos = [ POLYGON1_X, squeakPosition[1]]
                polygon3.pos = [POLYGON1_X,-20]
        
        #Check for LMB Click
        if squeakState[0] == 1 and squeakPosition[0] < 0: #check for top completion
            top_slider_state = 1 
        
        if squeakState[0] == 1 and squeakPosition[0] > 0: #check for bottom completion
            bottom_slider_state = 1
        
        #Check for RMB Click
        if squeakState[2] == 1 and squeakPosition[0] < 0: #check for top completion
            top_slider_text = 9999
            top_slider_state = 0 
        
        if squeakState[2] == 1 and squeakPosition[0] > 0: #check for bottom completion
            bottom_slider_text = 9999
            bottom_slider_state = 0
            
        if top_slider_state == 1 and bottom_slider_state == 1: #check for final trial completion
            complete_state = 1 
        
        
        # get current time
        t = trialClock.getTime()
        rectTimer(responseDuration, t, False, True, False)

        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        
        if image.status == STARTED and t >= (fixed_offset + (responseDuration - win.monitorFramePeriod*0.75)): #most of one frame period left
            image.setAutoDraw(False)
            top_value = 99999
            bottom_value = 99999
            continueRoutine = False
            
        # *polygon1* updates
        if t >= 0.0 and polygon1.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon1.tStart = t  # underestimates by a little under one frame
            polygon1.frameNStart = frameN  # exact frame index
            polygon1.setAutoDraw(True) 
        # *polygon2* updates
        if t >= 0.0 and polygon2.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon2.tStart = t  # underestimates by a little under one frame
            polygon2.frameNStart = frameN  # exact frame index
            polygon2.setAutoDraw(True)
        # *polygon3* updates
        if t >= 0.0 and polygon3.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon3.tStart = t  # underestimates by a little under one frame
            polygon3.frameNStart = frameN  # exact frame index
            polygon3.setAutoDraw(True)
        # *ISI* period

        # check for quit (the Esc key)
        if event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
       
    
    #print('mouseBox FunctionComplete')
    polygon1.setAutoDraw(False)
    polygon2.setAutoDraw(False)
    polygon3.setAutoDraw(False)
    image.setAutoDraw(False)
    rectTimer(responseDuration, t, False, False, True)

    data_output = np.zeros((1,3))

    t = trialClock.getTime()
    if complete_state: 
        data_output[0,0] = int(top_slider_text)
        data_output[0,1] = int(bottom_slider_text)
        data_output[0,2] = t
    else: 
        data_output[0,0] = INCOMPLETE_RATING
        data_output[0,1] = INCOMPLETE_RATING
        data_output[0,2] = t

    squeak = event.Mouse(visible = False, newPos = None, win = win)

    return data_output
        
def verticalSingleSlider(leftOrRight, backgroundImagePath,responseType):#,minimumLocation,maximumLocation, ResponseType): #returns the x position of the mouse ] 
    """
        Creates an UNTIMED and VERTICAL single slider for <responseDuration>. 
        This is specifically calibrated for a specific image. 
        Right Click: Sets slider
        Left Click: No Undo functionality
        Inputs:
            leftOrRight(str): Either "LEFT" or "RIGHT" for 2 different types of vertical sliders
            backgroundImagePath(str): Background Image path
            responseType(int): Deprecated input variable. Must always be set to 1. 
    """
    
    MIN_Y = -545
    MAX_Y = 497
    
    if leftOrRight == 'LEFT': 
        X_POS = 79
    elif leftOrRight == 'RIGHT':
        X_POS = -165
        
    
    RECT_LENGTH = MAX_Y - MIN_Y
    
    image =  visual.ImageStim(win=win, name='image',units='pix', 
        image=backgroundImagePath, mask=None,
        ori=0, pos=[0, 0], size=[MONITOR_WIDTH,MONITOR_HEIGHT],
        color=[1,1,1], colorSpace='rgb', opacity=resp_brightness,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-1.0)
    
        
    squeak = event.Mouse(visible = True, newPos = None, win = win)
    squeakState = [0,0,0]

    # update component parameters for each repeat
    # keep track of which components have finished
    polygon = visual.ShapeStim(win=win, name='polygon',units='pix', 
        vertices = ( (-50,50) , (50,50) , (0,0) ),
        ori=0, pos=[0, X_POS],
        lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
        fillColor=[1,-1,-1], fillColorSpace='rgb',
        opacity=resp_brightness,depth=-2.0, 
        interpolate=True)
    #-------Start Routine "trial"-------
    
    if leftOrRight == 'LEFT': 
        polygon.vertices = ( (50,-50) , (50,50) , (0,0) )
    elif leftOrRight == 'RIGHT':
        polygon.vertices = ( (-50,50) , (-50,-50) , (0,0) )
        
    continueRoutine = True
    #------Prepare to start Routine "trial"-------
    t = 0
    frameN = -1
    
    while continueRoutine and squeakState[0] == 0:
        
        squeakPosition = squeak.getPos()
        squeakState = squeak.getPressed()
        
        if responseType == 1:
            if squeakPosition[1] < MIN_Y:
                squeakPosition[1] = MIN_Y
            elif squeakPosition[1] > MAX_Y:
                squeakPosition[1] = MAX_Y
        displayText = int( ( squeakPosition[1] - MIN_Y) * 21 /RECT_LENGTH )
                
        
        polygon.pos = [X_POS, squeakPosition[1]]
        
        
        # get current time
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        
        # *polygon* updates
        if t >= 0.0 and polygon.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon.tStart = t  # underestimates by a little under one frame
            polygon.frameNStart = frameN  # exact frame index
            polygon.setAutoDraw(True)
        # *ISI* period

        # check for quit (the Esc key)
        if event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()



    polygon.setAutoDraw(False)
    image.setAutoDraw(False)
    squeak = event.Mouse(visible = False, newPos = None, win = win)

    data_output = np.zeros((1,3))

    t = trialClock.getTime()
    
    data_output[0,0] = displayText
    data_output[0,1] = UNUSED_RATING
    data_output[0,2] = t
    
    return data_output

def verticalTimedSingleSlider(leftOrRight,backgroundImagePath, responseType, responseDuration):     
    """
        Creates a TIMED and VERTICAL single slider for <responseDuration>. 
        This is specifically calibrated for a specific image. 
        Right Click: Sets slider
        Left Click: No Undo functionality
        Inputs:
            leftOrRight(str): Either "LEFT" or "RIGHT" for 2 different types of vertical sliders
            backgroundImagePath(str): Background Image path
            responseType(int): Deprecated input variable. Must always be set to 1. 
            responserDruation(double): Duration of slider
    """
    MIN_Y = -545
    MAX_Y = 497
    
    if leftOrRight == 'LEFT': 
        X_POS = 79
    elif leftOrRight == 'RIGHT':
        X_POS = -165
        
    
    RECT_LENGTH = MAX_Y - MIN_Y
    
    image =  visual.ImageStim(win=win, name='image',units='pix', 
        image=backgroundImagePath, mask=None,
        ori=0, pos=[0, 0], size=[MONITOR_WIDTH,MONITOR_HEIGHT],
        color=[1,1,1], colorSpace='rgb', opacity=resp_brightness,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-1.0)
    
        
    squeak = event.Mouse(visible = True, newPos = None, win = win)
    squeakState = [0,0,0]

    # update component parameters for each repeat
    # keep track of which components have finished
    polygon = visual.ShapeStim(win=win, name='polygon',units='pix', 
        vertices = ( (-50,50) , (50,50) , (0,0) ),
        ori=0, pos=[0, X_POS],
        lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
        fillColor=[1,-1,-1], fillColorSpace='rgb',
        opacity=resp_brightness,depth=-2.0, 
        interpolate=True)
    #-------Start Routine "trial"-------
    
    if leftOrRight == 'LEFT': 
        polygon.vertices = ( (50,-50) , (50,50) , (0,0) )
    elif leftOrRight == 'RIGHT':
        polygon.vertices = ( (-50,50) , (-50,-50) , (0,0) )
     
    continueRoutine = True
    
    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
    #------Prepare to start Routine "trial"-------
    t = 0
    rectTimer(responseDuration, t, True, False, False)

    trialClock.reset()  # clock 
    globalClock.reset()
    routineTimer.reset()
    frameN = -1
    
    trialComponents = []
    trialComponents.append(image)

    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    continueRoutine = True
    
    while continueRoutine and squeakState[0] == 0:
        squeakPosition = squeak.getPos()
        squeakState = squeak.getPressed()
        
        if responseType == 1:
            if squeakPosition[1] < MIN_Y:
                squeakPosition[1] = MIN_Y
            elif squeakPosition[1] > MAX_Y:
                squeakPosition[1] = MAX_Y
        displayText = int( ( squeakPosition[1] - MIN_Y) * 21 /RECT_LENGTH )
                        
        polygon.pos = [X_POS, squeakPosition[1]]
        
        # get current time
        # update/draw components on each frame
        
        # get current time
        t = trialClock.getTime()
        rectTimer(responseDuration, t, False, True, False)

        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *timed_window_image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        if image.status == STARTED and t >= (fixed_offset + (responseDuration - win.monitorFramePeriod*0.75)): #most of one frame period left
            image.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
            
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        
        # *polygon* updates
        if t >= 0.0 and polygon.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon.tStart = t  # underestimates by a little under one frame
            polygon.frameNStart = frameN  # exact frame index
            polygon.setAutoDraw(True)
            # *ISI* period

        # check for quit (the Esc key)
        if event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            

    complete_state =    0 
    if squeakState[0] == 1: 
            complete_state = 1 
    
    #print('Timed mouseBox FunctionComplete')
    polygon.setAutoDraw(False)
    image.setAutoDraw(False)
    rectTimer(responseDuration, t, False, False, True)

    squeak = event.Mouse(visible = False, newPos = None, win = win)
   
    data_output = np.zeros((1,3))

    t = trialClock.getTime()
    
    if complete_state == 1:
        data_output[0,0] = displayText
        data_output[0,1] = UNUSED_RATING
        data_output[0,2] = t
    elif complete_state == 0: 
        data_output[0,0] = INCOMPLETE_RATING
        data_output[0,1] = UNUSED_RATING
        data_output[0,2] = t
        
    return data_output

#=================#

def displayInstructions(displayPhrase):
    """
        Displays <displaysPhrase> until ESC input

    """
    # Initialize components for Routine "Instructions"
    InstructionsClock = core.Clock()
    User = visual.TextStim(win=win, ori=0, name='User',
        text= displayPhrase,    font='Arial',
        pos=[0, 0], height=20, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
            depth=0.0)
        #------Prepare to start Routine "Instructions"-------
    t = 0
    InstructionsClock.reset()  # clock 
    frameN = -1
    
    #initiate mouse
    squeak = event.Mouse(visible = False, newPos = None, win = win)
    squeakState = [0,0,0]
    
    
     # update component parameters for each repeat
    key_resp_2 = event.BuilderKeyResponse()
    key_resp_2.status = NOT_STARTED
    # keep track of which components have finished
    InstructionsComponents = []
    InstructionsComponents.append(User)
    InstructionsComponents.append(key_resp_2)
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    #-------Start Routine "Instructions"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = InstructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *User* updates
        if t >= 0.0 and User.status == NOT_STARTED:
            # keep track of start time/frame for later
            User.tStart = t  # underestimates by a little under one frame
            User.frameNStart = frameN  # exact frame index
            User.setAutoDraw(True)
        
        # *key_resp_2* updates
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t  # underestimates by a little under one frame
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                key_resp_2.rt = key_resp_2.clock.getTime()
                # a response ends the routine
                continueRoutine = False
            
            #check for mouse click 
            squeakState = squeak.getPressed()
            if squeakState[0] != 0 or squeakState[1] != 0 or squeakState[2] != 0:
                continueRoutine = False
            
            
            
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    #-------Ending Routine "Instructions"-------
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
       key_resp_2.keys=None
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

def frequencyImage(imagepath1,imagepath2,reps, picDuration, brightness):
      
    # Initialize components for Routine "trial"
    trialClock = core.Clock()
    image = visual.ImageStim(
        win=win, name='image',
        image=imagepath1, mask=None,
        ori=0, pos=(0, 0), size=[MONITOR_WIDTH,MONITOR_HEIGHT],
        color=[1,1,1], colorSpace='rgb', opacity=brightness,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)

    image_2 = visual.ImageStim(
        win=win, name='image_2',
        image=imagepath2, mask=None,
        ori=0, pos=(0, 0), size=[MONITOR_WIDTH,MONITOR_HEIGHT],
        color=[1,1,1], colorSpace='rgb', opacity=brightness,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-1.0)

    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
    
    
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=reps, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
        
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)

    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial.keys():
                exec(paramName + '= thisTrial.' + paramName)
        
        # ------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(picDuration*2)
        # update component parameters for each repeat
        # keep track of which components have finished
        trialComponents = [image, image_2]
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image* updates
            if t >= 0 and image.status == NOT_STARTED:
                # keep track of start time/frame for later
                image.tStart = t
                image.frameNStart = frameN  # exact frame index
                image.setAutoDraw(True)
            frameRemains = 0 + picDuration- win.monitorFramePeriod * 0.5  # most of one frame period left
            if image.status == STARTED and t >= frameRemains:
                image.setAutoDraw(False)
            
            # *image_2* updates
            if t >= picDuration and image_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_2.tStart = t
                image_2.frameNStart = frameN  # exact frame index
                image_2.setAutoDraw(True)
            frameRemains = picDuration + picDuration- win.monitorFramePeriod * 0.5  # most of one frame period left
            if image_2.status == STARTED and t >= frameRemains:
                image_2.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

    # completed 100 repeats of 'trials'


#===================RUNNING EXPERIMENT===================

def runStimulus(dataArray):#dataArray is outputMatrix
    #print('dataArray')
    #print(dataArray[0])
    pain = 99
    
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
    experimentNumber =      dataArray[10]
    
    
    #print('experiment number ') 
    #print(experimentNumber)
    if experimentNumber == 1:
        displayInstructions('Press ESC anytime to exit. Press any key to continue.')
    
    
    #resting time
    if DEBUG_PRINT:
        timedWindowText('RESTING TIME', restingTime)
    else:
        timedWindowText('   ', restingTime)
        
    #anticipatoryTime
    timedImage(ANTICIPATE, anticipatoryTime) 
    
    repetitions = conversion.convertDurationToRepetitions(stimulusFrequency, stimulusDuration)
    picDuration = conversion.convertFreqToTime(stimulusFrequency)
    
    #Stimlus Time
    if stimulusType== 1:
        frequencyImage(ACHECK_BW,ACHECK_BW_,repetitions, picDuration , brightness )
    elif stimulusType == 2:
        frequencyImage(ACHECK_BY,ACHECK_BY_,repetitions, picDuration , brightness ) 
    elif stimulusType == 3:
        frequencyImage(ACHECK_RG,ACHECK_RG_,repetitions, picDuration , brightness ) 
    elif stimulusType == 4:
        frequencyImage(CHECKER_BW,CHECKER_BW_,repetitions, picDuration , brightness ) 
    elif stimulusType == 5:
        frequencyImage(CHECKER_BY,CHECKER_BY_,repetitions, picDuration , brightness ) 
    elif stimulusType == 6:
        frequencyImage(CHECKER_RG,CHECKER_RG_,repetitions, picDuration , brightness ) 
    elif stimulusType == 7:
        frequencyImage(STROBE_BLACK,STROBE_WHITE,repetitions, picDuration , brightness ) 
    elif stimulusType == 8:
        frequencyImage(STROBE_BLUE,STROBE_YELLOW,repetitions, picDuration , brightness ) 
    elif stimulusType == 9:
        frequencyImage(STROBE_RED,STROBE_GREEN,repetitions, picDuration , brightness ) 

    elif stimulusType == 0: #'None':
        if DEBUG_PRINT:
            print 'Experiment ' + str(experimentNumber) +' skipped by user'
    else:    
        print "In development - this should never print"
    
    
    #Response Type
    if stimulusType != 0:
        pain = runResponse(timeUntilRating, responseType, responseTime, responseCountdown)#def runResponse(timeUntilResponseDuration, responseType,responseTime):


    return pain

def runResponse(timeUntilResponseDuration, responseType, responseTime, responseCountdown):
    #TIME UNTIL RESPONSE 
    if DEBUG_PRINT:
        timedWindowText('TIME UNTIL RESPONSE', timeUntilResponseDuration)
    else:
        timedWindowText('   ', timeUntilResponseDuration)

    #RESPONSE Type
    textDisplay = 1; 
    if responseType == 1:
        if responseCountdown == 0:
            pain = singleSlider(BRIGHTNESS100,textDisplay) # actual value only for 10 s 
        elif responseCountdown == 1: 
            pain = timedSingleSlider(BRIGHTNESS100, textDisplay,responseTime)
    elif responseType == 2:
        if responseCountdown == 0:
            pain = singleSlider(UNPLEASANT100,textDisplay)
        elif responseCountdown == 1:
            pain = timedSingleSlider(UNPLEASANT100, textDisplay, responseTime)
    elif responseType == 3:
        if responseCountdown == 0:
            pain = doubleSlider(DOUBLESLIDER100,textDisplay)
        elif responseCountdown == 1:
            pain = timedDoubleSlider(DOUBLESLIDER100, textDisplay, responseTime)
    elif responseType == 4:
        if responseCountdown == 0:
            pain = verticalSingleSlider('LEFT', AFFECTIVE20,textDisplay)
        elif responseCountdown == 1:
            pain = verticalTimedSingleSlider('LEFT', AFFECTIVE20, textDisplay, responseTime)
    elif responseType == 5:
        if responseCountdown == 0:
            pain = verticalSingleSlider('RIGHT', SENSORY20,textDisplay)
        elif responseCountdown == 1:
            pain = verticalTimedSingleSlider('RIGHT', SENSORY20, textDisplay, responseTime)
    elif responseType == 6:
        if responseCountdown == 0:
            pain = verticalDoubleSlider(DOUBLESLIDER20,textDisplay)
        elif responseCountdown == 1:
            pain = verticalTimedDoubleSlider(DOUBLESLIDER20, textDisplay, responseTime)
    
    return pain



#Main Function

#matrix of empty parameters
experimentMatrix = np.zeros((MAX_STIMULUS+1, MAX_PARAMETERS),dtype = float)

#create GUI object
myDlg = gui.Dlg(title="Michigan Aversion Stimulus Test (M-VAST)")
#define GUI object
gui_functions.mainGUI(myDlg)
#present GUI 
ok_data = myDlg.show()


EDIT = 'Edit'
START = 'Start'

START_FROM_FILE = 'Start from file' 
SAVE_TO_FILE = 'Save to output file' 

while START_BOOL == 0:

    if myDlg.OK:
        if myDlg.data[6] == EDIT:
            
            #Set the experiment number based on the 
            experimentNum = int(myDlg.data[7])
            
            windowTitle = 'Edit Stimulus ' + str(experimentNum)
            
            #create new DLG object
            myDlg2 = gui.Dlg(title= windowTitle)
            
            if experimentMatrix[experimentNum][10] == 0: # if the experiment number of said matrix has not been instantiated yet
                
                #create new stimulus edit window 
                gui_functions.createStimEdit(experimentNum , myDlg2)
            elif experimentNum == experimentMatrix[experimentNum][10]: #if the experiment number of said matrix has already been instantiated 
                
                #create a GUI but with the information from the past edit still included 
                gui_functions.createSecondStimEdit(experimentNum, myDlg2, experimentMatrix[experimentNum])
                
            if myDlg2.OK:#if the data state is stored correctly 
                
                #outputMatrix of all the experiment settings 
                experimentMatrix[experimentNum] = conversion.dlgDataToMatrix(experimentNum, myDlg2.data) #def dlgDataToMatrix(experimentNumber,dataArray):
                
                if DEBUG_PRINT:
                    print('experiment Matrix for experiment ' + str(experimentNum))
                    print(experimentMatrix[experimentNum])
                
                            
            else:#if cancel on the stimulus Edit 
                EDIT_BOOL = 1
                
        elif myDlg.data[6] == START:
            START_BOOL = 1
            break
            
        elif myDlg.data[6] == START_FROM_FILE:
            experimentMatrix = io_functions.runFromFile(myDlg.data[5])
            break
        
        elif myDlg.data[6] == SAVE_TO_FILE:
            with open(myDlg.data[4], 'wb') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter = ',')
                for num in range(1,MAX_STIMULUS+1):
                    spamwriter.writerow(experimentMatrix[num])
            #print('Saved to file')
            sys.exit()
            
    else:
        #print('user cancelled')
        sys.exit()
        
    #Completed edit - instantiate the GUI with the previous experiment information
    if EDIT_BOOL == 0:
        myDlg = gui.Dlg(title="Michigan Aversion Stimulus Test (M-VAST)")
        gui_functions.secondGUI(myDlg, myDlg2.data, experimentNum)
        ok_data = myDlg.show()
        
        if DEBUG_PRINT:
            print('Completed Stimulus Edit')
            print('Trial is NOT starting and the stimulus edit was completed')


    #Canceled edit - instantiate the original GUI
    elif EDIT_BOOL == 1 :
        myDlg = gui.Dlg(title="Michigan Aversion Stimulus Test (M-VAST)")
        gui_functions.mainGUI(myDlg)
        ok_data = myDlg.show()
        
        if DEBUG_PRINT:
            print('Trial is NOT starting and the stimulus edit was CANCELED')


if DEBUG_PRINT:
    print('Editing has been completed')


#Starting the Trial because Start State has been called.
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Setup the Window
win = visual.Window(size=(MONITOR_WIDTH, MONITOR_HEIGHT), fullscr=True, screen=1, allowGUI=False, allowStencil=False,
    blendMode='add', color = 'black', 
    units='pix')

rectTime = visual.Rect(win=win, name='rectTime',units='pix', 
    width = MONITOR_WIDTH - 200 , height = 10,
    ori=0, pos=[0, MONITOR_HEIGHT/2-5],
    lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,1], fillColorSpace='rgb',
    opacity=resp_brightness,depth=-2.0, 
    interpolate=True)

# Store info about the experiment session
expName = 'untitled.py'
expInfo = {'participant':'', 'session':'001'}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# Initialize components for Routine "trial"
trialClock = core.Clock()

t = datetime.date.today()
dateAndTime = datetime.datetime.now()
filename = str(t) + '_' + str(dateAndTime.hour) + '_' + str(dateAndTime.minute) + '_' + str(myDlg.data[0]) +'.csv'

with open(filename, 'wb') as csvfile:
    
    output_fs = csv.writer(csvfile, delimiter = ',')
    output_fs.writerow(['Time before Visual Cue', 'Visual Cue Duration', 'Stimulus Type', 'Stimulus Duration', \
                        'Stimulus Frequency','Brightness', 'Time Until Rating', 'Rating Type', 'Rating Time', \
                        'Countdown', 'Experiment Number','Top/Left Slider', 'Bottom/Right Slider','Time to Rate'\
                        ,'Patient ID', 'PATIENT ID VARIABLE'])
    for num in range(1,MAX_STIMULUS + 1):
        if experimentMatrix[num][10]== 0:
            continue
            
        
        userRating = runStimulus(experimentMatrix[num])
        #userRatingArray = [ userRating[0,0], userRating[0,1],userRating[0,2] ]
        
        paramNum = len(experimentMatrix[num])
        end = paramNum+3

        outputArray = np.zeros( (1, end) )
        outputArray[0,0:paramNum] = experimentMatrix[num]
        outputArray[0,paramNum:end] = userRating 
        output_fs.writerow(outputArray[0,:])


displayInstructions('Experiment Sequence complete. Press any button to end. ')

win.close()
core.quit()



