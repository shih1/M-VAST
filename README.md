# M-VAST (Michigan Visual Aversion Stress Test)

This test is created using PsychoPy 1.85.2 and Python 2.7.11. It maintains compatability with most older versions of PsychoPy and Python. 

## **Overview**

There is some terminology that should be defined to understand the structure of each experiment. 

Experiment: A sequence of stimuli presented to a test subject. 
Stimuli: An aversive stimulus presented to a test subject paired with an optional rating screen. 

## **Setup**

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

### **Method 1: Start from file**

This is the most common way M-VAST is designed to be used. You can create a `.csv` file with all the stimuli parameters for a specific set of patients and run the exact same experiment on everyone. 
The input file will be described later. 

### **Method 2: Edit** 

This method allows you to edit <Stimulus Number> in the current experiment. Select "Edit" and select the Stimulus Number you wish to edit then press "OK". 
You can continue this process until you have edited all the stimuli you want in your experiment. 

### **Method 3: Start**

This method starts the experiment you edited.  It's similar to "Start from file" but it uses the edited stimuli rather than the input file. 

### **Method 4: Save to File** 

This method saves the experiment you edited into a `.csv` file specified in <Output File>. 

## **Stimulus Edit**

There are 11 parameters to edit 

1. Time before Visual Cue(s)
    * Resting time before visual cue

1. Visual Cue Duration (s)
    * Duration of stimulus

1. Stimulus Type
    * 3 types of stimuli with 3 different color combinations
        * 9 total combinations
    * Stimuli Types
        * Annular Checkerboard
        * Checkerboars
        * Strobe Light
    * Color Combinations
        * Black/White
        * Blue/Yellow
        * Red/Green

1. Stimulus Duration(s)
    * Duration of the stimulus

1. Stimulus Frequency
    * You can only choose frequncies that have a period of a factor of 1/60
    * The period of the stimuli must be a factor of 1/60th
    * The allowable frequencies are (in Hz):
        * 15
        * 10
        * 7.5
        * 6
        * 5
        * 3
        * 2
        * 1

1. Brightness
    * A linear black filter on the entire stimuli screen is applied
        * 1: no filter
        * 0 : full black filter 

1. Time until Rating(s)
    * Time between stimuli and rating screen

1. Response/Rating Type
There are 6 response types 
    * Brightness (0->100)
    * Unpleasantness (0->100)
    * Dual Scale (0->100) containing both Brightness and Unpleasantness
    * Affective (0->20)
    * Sensory (0->20)
    * Dual Scale (0->20) containing both Affective and Sensory
        * The (0->100) scales are horizontal 
        * (0->20) scales are vertical. 

1.  Response/Rating Time(s)
    * Time allowed to rate the stimulus. 

1.  Limit Response Time/Countdown? 
    * 1 - Yes: Limit response time.
    * 0 - No: No Limit on response time. 


## Example CSV File

*sample_test.csv*

Time before Visual Cue | Visual Cue Duration | Stimulus Type | Stimulus Duration | Stimulus Freqeuncy | Brightness | Time until rating | Rating Type | Rating Time | Countdown? |
--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
1 | 1 | 1 | 1 | 10 | 1 | 3 | 1 | 10 | 1 |
1 | 1 | 1 | 2 | 10 | 1 | 2 | 3 | 10 | 1 |
1 | 1 | 1 | 1 | 10 | 0.5 | 1 | 2 | 10 | 0 |
1 | 1 | 1 | 2 | 10 | 0.5 | 0 | 4 | 10 | 0 |


