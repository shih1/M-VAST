# M-VAST
Michigan Visual Aversion Stress Test

This test is created using PsychoPy 1.85.2 and Python 2.7.11. It maintains compatability with most older versions of PsychoPy and Python. 

**Overview**

There is some terminology that should be defined to understand the structure of each experiment. 

Experiment: A sequence of stimuli presented to a test subject. 
Stimuli: An aversive stimulus presented to a test subject paired with an optional rating screen. 

**Setup**

Executing `main.py` will open a first screen called *Stimulus Setup*. 

The following fields are present: 
    -Patient ID
    -Experimenter ID
    -Age
    -Sex
    -Ouput File
    -Input File
    -Save or Start Experiment
    -Stimulus Number

There are **four** different ways to use the M-VAST setup screen. 

**Method 1: Start from file**

This is the most common way M-VAST is designed to be used. You can create a `.csv` file with all the stimuli parameters for a specific set of patients and run the exact same experiment on everyone. 
The input file will be described later. 

**Method 2: Edit** 

This method allows you to edit <Stimulus Number> in the current experiment. Select "Edit" and select the Stimulus Number you wish to edit then press "OK". 
You can continue this process until you have edited all the stimuli you want in your experiment. 

**Method 3: Start**

This method starts the experiment you edited.  It's similar to "Start from file" but it uses the edited stimuli rather than the input file. 

**Method 4: Save to File** 

This method saves the experiment you edited into a `.csv` file specified in <Output File>. 

**Stimulus Edit**

There are 10 parameters to edit 

    -Time before Visual Cue(s)
        Resting time before 
        
    -Visual Cue Duration (s)
        Duration of stimuli
    
    -Stimulus Type
        There are 3 types of stimuli with 3 different color combinations resulting in 9 different stimuli. 
        There is an Annular Checkerboard, Checkerboard, or Strobe Light. 
        The color combinations are Black/White, Blue/Yellow, and Red/Green
    
    -Stimulus Duration(s) 
        The duration of the stimulus. 
    
    -Stimulus Frequency
        The frequency of the stimuli. You can only choose frequncies that have a period of a factor of 1/60. The period of the stimuli must be a factor of 1/60th. The allowable frequencies are as follows: 
        15, 10, 7.5, 6, 5, 3, 2, 1
    
    -Brightness
        A linear black filter on the entire stimuli screen is applied with 1 being no filter and 0 being full filter. 
    
    -Time until Rating(s)
        Time between stimuli and rating screen. 
    
    -Response Type
        There are 6 response type. 
            Brightness (0->100)
            Unpleasantness (0->100)
            Dual Scale (0->100) containing both Brightness and Unpleasantness
            Affective (0->20)
            Sensory (0->20)
            Dual Scale (0->20) containing both Affective and Sensory

            The (0->100) scales are horizontal and the (0->20) scales are vertical. 
    
    -Response Time(s)
        Time allowed to rate the stimulus. 
    
    -Limit Response Time? 
        Yes or No specification. 
        Yes: Limit response time.
        No: No Limit on response time. 

