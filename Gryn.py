#!/usr/bin/env python
# encoding: utf-8
from pyo import *
import random
import wx
import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop/")

print desktop

s = Server().boot()
s.start()
s.recordOptions(sampletype=3)
 
NAME = "GRYN"
VERSION = "1.2"

#######################################  CLASSES  #################################################







#####################################  INSTANCIATIONS  #############################################

master_frequency = 440
master_feedback = 0
master_frequency2 = 440
master_feedback2 = 0
master_frequency3 = 440
master_feedback3 = 0
master_frequency4 = 440
master_feedback4 = 0

active1 = 0 
active2 = 0
active3 = 0
active4 = 0
active5 = 0
active6 = 0
active7 = 0
active8 = 0

lfo_1 = LFO(freq=2, sharp=0.50, type=0, mul=1, add=0)
lfo_2 = LFO(freq=2, sharp=0.50, type=0, mul=1, add=0)
lfo_3 = LFO(freq=2, sharp=0.50, type=0, mul=1, add=0)
lfo_4 = LFO(freq=2, sharp=0.50, type=0, mul=1, add=0)
lfo_5 = LFO(freq=2, sharp=0.50, type=0, mul=1, add=0)
lfo_6 = LFO(freq=2, sharp=0.50, type=0, mul=1, add=0)
lfo_7 = LFO(freq=2, sharp=0.50, type=0, mul=1, add=0)
lfo_8 = LFO(freq=2, sharp=0.50, type=0, mul=1, add=0)

sine_1 = SineLoop(freq = 440, feedback = 0, mul=.3, add=0)
sine_2 = SineLoop(freq = 440, feedback = 0, mul=.3, add=0)
sine_3 = SineLoop(freq = 440, feedback = 0, mul=.3, add=0)
sine_4 = SineLoop(freq = 440, feedback = 0, mul=.3, add=0)

filter_1 = Biquad(input=sine_1, freq=20000, q=1, type=0, mul=1, add=0)
filter_2 = Biquad(input=sine_2, freq=20000, q=1, type=0, mul=1, add=0)
filter_3 = Biquad(input=sine_3, freq=20000, q=1, type=0, mul=1, add=0)
filter_4 = Biquad(input=sine_4, freq=20000, q=1, type=0, mul=1, add=0)

sineOut = DCBlock(input=(filter_1 + filter_2 + filter_3 + filter_4), mul=.25, add=0)
s_1 = sineOut.mix(2)
s_1.out()

#s.gui(locals())

#############################################  GUI  ###########################################



class MyFrame(wx.Frame):
    
    def __init__(self, parent, title, pos, size):

### UTILITY --------------

        # The Frame
        wx.Frame.__init__(self, parent, id=-1, title=title, pos=pos, size=size)
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour("#87EDB9")

### REC --------------

        # The REC Button
        self.record = wx.ToggleButton(self.panel, id=-1, label="REC", pos=(1, 1), size=wx.DefaultSize)
        self.record.Bind(wx.EVT_TOGGLEBUTTON, self.doREC)

### CHAOS --------------

        # The CHAOS Button
        self.chaos = wx.Button(self.panel, id=-1, label="CHAOS", pos=(539, 1), size=wx.DefaultSize)
        self.chaos.Bind(wx.EVT_BUTTON, self.doChaos)

### EXIT --------------

        # The Exit Bouton
        self.exitBouton = wx.Button(self.panel, id=-1, label="EXIT", pos=(1080, 1))
        self.exitBouton.Bind(wx.EVT_BUTTON, self.doExit)

### SYNC --------------

        # The SYNC Button
        self.sync = wx.ToggleButton(self.panel, id=-1, label="SYNC FREQ", pos=(539, 545), size=wx.DefaultSize)
        self.sync.Bind(wx.EVT_TOGGLEBUTTON, self.showSync)

        # The Sync Slider
        self.sync1 = wx.Slider(self.panel, id=-1, value=5, minValue=1, maxValue=50, pos=(640, 550), size=(250, -1))
        self.sync1.Hide()
        self.sync1.Bind(wx.EVT_SLIDER, self.doSyncFreq) 
        

### THE SOURCE --------------
        
        # The Master Freq 1 Slider 
        self.masterFreq1Text = wx.StaticText(self.panel, id=-1, label="Master Frequency", pos=(20, 50), size=wx.DefaultSize)
        self.masterFreq1 = wx.Slider(self.panel, id=-1, value=440, minValue=40, maxValue=800, pos=(20, 70), size=(250, -1))
        self.masterFreq1.Bind(wx.EVT_SLIDER, self.changeMasterFreq1)

        # The Master Feedback 1 Slider 
        self.masterFeedback1Text = wx.StaticText(self.panel, id=-1, label="Master Feedback", pos=(300, 50), size=wx.DefaultSize)
        self.masterFeedback1 = wx.Slider(self.panel, id=-1, value=0, minValue=0, maxValue=100, pos=(300, 70), size=(250, -1))
        self.masterFeedback1.Bind(wx.EVT_SLIDER, self.changeMasterFeedback1)

        # The Volume 1 Slider
        self.volume1 = wx.Slider(self.panel, id=-1, value=20000, minValue=0, maxValue=20000, pos=(560, 80), size=(-1,200), style=wx.SL_VERTICAL | wx.SL_INVERSE)
        self.volume1.Bind(wx.EVT_SLIDER, self.changeVolume1)


        # The Master Freq 2 Slider 
        self.masterFreq2Text = wx.StaticText(self.panel, id=-1, label="Master Frequency", pos=(20, 300), size=wx.DefaultSize)
        self.masterFreq2 = wx.Slider(self.panel, id=-1, value=440, minValue=40, maxValue=800, pos=(20, 320), size=(250, -1))
        self.masterFreq2.Bind(wx.EVT_SLIDER, self.changeMasterFreq2)

        # The Master Feedback 2 Slider 
        self.masterFeedback2Text = wx.StaticText(self.panel, id=-1, label="Master Feedback", pos=(300, 300), size=wx.DefaultSize)
        self.masterFeedback2 = wx.Slider(self.panel, id=-1, value=0, minValue=0, maxValue=100, pos=(300, 320), size=(250, -1))
        self.masterFeedback2.Bind(wx.EVT_SLIDER, self.changeMasterFeedback2)   

        # The Volume 2 Slider
        self.volume2 = wx.Slider(self.panel, id=-1, value=20000, minValue=0, maxValue=20000, pos=(560, 330), size=(-1,200), style=wx.SL_VERTICAL | wx.SL_INVERSE)
        self.volume2.Bind(wx.EVT_SLIDER, self.changeVolume2)


        # The Master Freq 3 Slider 
        self.masterFreq3Text = wx.StaticText(self.panel, id=-1, label="Master Frequency", pos=(620, 50), size=wx.DefaultSize)
        self.masterFreq3 = wx.Slider(self.panel, id=-1, value=440, minValue=40, maxValue=800, pos=(620, 70), size=(250, -1))
        self.masterFreq3.Bind(wx.EVT_SLIDER, self.changeMasterFreq3)

        # The Master Feedback 3 Slider 
        self.masterFeedback3Text = wx.StaticText(self.panel, id=-1, label="Master Feedback", pos=(900, 50), size=wx.DefaultSize)
        self.masterFeedback3 = wx.Slider(self.panel, id=-1, value=0, minValue=0, maxValue=100, pos=(900, 70), size=(250, -1))
        self.masterFeedback3.Bind(wx.EVT_SLIDER, self.changeMasterFeedback3)

        # The Volume 3 Slider
        self.volume3 = wx.Slider(self.panel, id=-1, value=20000, minValue=0, maxValue=20000, pos=(593, 80), size=(-1,200), style=wx.SL_VERTICAL | wx.SL_INVERSE)
        self.volume3.Bind(wx.EVT_SLIDER, self.changeVolume3)


        # The Master Freq 4 Slider 
        self.masterFreq4Text = wx.StaticText(self.panel, id=-1, label="Master Frequency", pos=(620, 300), size=wx.DefaultSize)
        self.masterFreq4 = wx.Slider(self.panel, id=-1, value=440, minValue=40, maxValue=800, pos=(620, 320), size=(250, -1))
        self.masterFreq4.Bind(wx.EVT_SLIDER, self.changeMasterFreq4)

        # The Master Feedback 4 Slider 
        self.masterFeedback4Text = wx.StaticText(self.panel, id=-1, label="Master Feedback", pos=(900, 300), size=wx.DefaultSize)
        self.masterFeedback4 = wx.Slider(self.panel, id=-1, value=0, minValue=0, maxValue=100, pos=(900, 320), size=(250, -1))
        self.masterFeedback4.Bind(wx.EVT_SLIDER, self.changeMasterFeedback4)   

        # The Volume 4 Slider
        self.volume4 = wx.Slider(self.panel, id=-1, value=20000, minValue=0, maxValue=20000, pos=(593, 330), size=(-1,200), style=wx.SL_VERTICAL | wx.SL_INVERSE)
        self.volume4.Bind(wx.EVT_SLIDER, self.changeVolume4)

              

### LFO1 SINELOOP 1 : FREQ --------------

        # The LFO1 Button
        self.onlfo_1 = wx.ToggleButton(self.panel, id=-1, label="ON", pos=(180, 110), size=wx.DefaultSize)
        self.onlfo_1.Bind(wx.EVT_TOGGLEBUTTON, self.activelfo1)

        # The Freq 1 Slider 
        self.freq1Text = wx.StaticText(self.panel, id=-1, label="LFO Freq", pos=(20, 130), size=wx.DefaultSize)
        self.freq1 = wx.Slider(self.panel, id=-1, value=2, minValue=1, maxValue=50, pos=(20, 150), size=(250, -1))
        self.freq1.Bind(wx.EVT_SLIDER, self.changeFreq1)

        # The Sharp 1 Slider 
        self.sharp1Text = wx.StaticText(self.panel, id=-1, label="LFO Sharpness", pos=(20, 170), size=wx.DefaultSize)
        self.sharp1 = wx.Slider(self.panel, id=-1, value=50, minValue=0, maxValue=100, pos=(20, 190), size=(250, -1))
        self.sharp1.Bind(wx.EVT_SLIDER, self.changeSharp1)

        # The Amplitude 1 Slider 
        self.amp1Text = wx.StaticText(self.panel, id=-1, label="LFO Amplitude", pos=(20, 210), size=wx.DefaultSize)
        self.amp1 = wx.Slider(self.panel, id=-1, value=100, minValue=20, maxValue=100, pos=(20, 230), size=(250, -1))
        self.amp1.Bind(wx.EVT_SLIDER, self.changeAmp1)    

        # The Type Choice 
        self.type1Text = wx.StaticText(self.panel, id=-1, label="LFO Type", pos=(20, 255), size=wx.DefaultSize)
        self.type1Choice = ["Saw", "Square", "Triangle", "Pulse", "Bipolar Pulse", "Sample & Hold", "Modulated Sine"]
        self.type1 = wx.Choice(self.panel, id=-1, pos=(110, 255), size=wx.DefaultSize, choices=self.type1Choice)
        self.type1.Bind(wx.EVT_CHOICE, self.changeType1)    


### LFO2 SINELOOP 1 : FEEDBACK --------------

        # The LFO2 Button
        self.onlfo_2 = wx.ToggleButton(self.panel, id=-1, label="ON", pos=(460, 110), size=wx.DefaultSize)
        self.onlfo_2.Bind(wx.EVT_TOGGLEBUTTON, self.activelfo2)

        # The Freq 2 Slider 
        self.freq2Text = wx.StaticText(self.panel, id=-1, label="LFO Freq", pos=(300, 130), size=wx.DefaultSize)
        self.freq2 = wx.Slider(self.panel, id=-1, value=2, minValue=1, maxValue=300, pos=(300, 150), size=(250, -1))
        self.freq2.Bind(wx.EVT_SLIDER, self.changeFreq2)

        # The Sharp 2 Slider 
        self.sharp2Text = wx.StaticText(self.panel, id=-1, label="LFO Sharpness", pos=(300, 170), size=wx.DefaultSize)
        self.sharp2 = wx.Slider(self.panel, id=-1, value=50, minValue=0, maxValue=100, pos=(300, 190), size=(250, -1))
        self.sharp2.Bind(wx.EVT_SLIDER, self.changeSharp2)

        # The Amplitude 2 Slider 
        self.amp2Text = wx.StaticText(self.panel, id=-1, label="LFO Amplitude", pos=(300, 210), size=wx.DefaultSize)
        self.amp2 = wx.Slider(self.panel, id=-1, value=100, minValue=20, maxValue=100, pos=(300, 230), size=(250, -1))
        self.amp2.Bind(wx.EVT_SLIDER, self.changeAmp2)

        # The Type Choice 
        self.type2Text = wx.StaticText(self.panel, id=-1, label="LFO Type", pos=(300, 255), size=wx.DefaultSize)
        self.type2Choice = ["Saw", "Square", "Triangle", "Pulse", "Bipolar Pulse", "Sample & Hold", "Modulated Sine"]
        self.type2 = wx.Choice(self.panel, id=-1, pos=(390, 255), size=wx.DefaultSize, choices=self.type2Choice)
        self.type2.Bind(wx.EVT_CHOICE, self.changeType2)   


### LFO3 SINELOOP 2 : FREQ --------------

        # The LFO3 Button
        self.onlfo_3 = wx.ToggleButton(self.panel, id=-1, label="ON", pos=(180, 360), size=wx.DefaultSize)
        self.onlfo_3.Bind(wx.EVT_TOGGLEBUTTON, self.activelfo3)

        # The Freq 3 Slider 
        self.freq3Text = wx.StaticText(self.panel, id=-1, label="LFO Freq", pos=(20, 380), size=wx.DefaultSize)
        self.freq3 = wx.Slider(self.panel, id=-1, value=2, minValue=1, maxValue=50, pos=(20, 400), size=(250, -1))
        self.freq3.Bind(wx.EVT_SLIDER, self.changeFreq3)

        # The Sharp 3 Slider 
        self.sharp3Text = wx.StaticText(self.panel, id=-1, label="LFO Sharpness", pos=(20, 420), size=wx.DefaultSize)
        self.sharp3 = wx.Slider(self.panel, id=-1, value=50, minValue=0, maxValue=100, pos=(20, 440), size=(250, -1))
        self.sharp3.Bind(wx.EVT_SLIDER, self.changeSharp3)

        # The Amplitude 3 Slider 
        self.amp3Text = wx.StaticText(self.panel, id=-1, label="LFO Amplitude", pos=(20, 460), size=wx.DefaultSize)
        self.amp3 = wx.Slider(self.panel, id=-1, value=100, minValue=20, maxValue=100, pos=(20, 480), size=(250, -1))
        self.amp3.Bind(wx.EVT_SLIDER, self.changeAmp3)    

        # The Type Choice 
        self.type3Text = wx.StaticText(self.panel, id=-1, label="LFO Type", pos=(20, 505), size=wx.DefaultSize)
        self.type3Choice = ["Saw", "Square", "Triangle", "Pulse", "Bipolar Pulse", "Sample & Hold", "Modulated Sine"]
        self.type3 = wx.Choice(self.panel, id=-1, pos=(110, 505), size=wx.DefaultSize, choices=self.type3Choice)
        self.type3.Bind(wx.EVT_CHOICE, self.changeType3)  


### LFO4 SINELOOP 2 : FEEDBACK --------------

        # The LFO4 Button
        self.onlfo_4 = wx.ToggleButton(self.panel, id=-1, label="ON", pos=(460, 360), size=wx.DefaultSize)
        self.onlfo_4.Bind(wx.EVT_TOGGLEBUTTON, self.activelfo4)

        # The Freq 4 Slider 
        self.freq4Text = wx.StaticText(self.panel, id=-1, label="LFO Freq", pos=(300, 380), size=wx.DefaultSize)
        self.freq4 = wx.Slider(self.panel, id=-1, value=2, minValue=1, maxValue=300, pos=(300, 400), size=(250, -1))
        self.freq4.Bind(wx.EVT_SLIDER, self.changeFreq4)

        # The Sharp 4 Slider 
        self.sharp4Text = wx.StaticText(self.panel, id=-1, label="LFO Sharpness", pos=(300, 420), size=wx.DefaultSize)
        self.sharp4 = wx.Slider(self.panel, id=-1, value=50, minValue=0, maxValue=100, pos=(300, 440), size=(250, -1))
        self.sharp4.Bind(wx.EVT_SLIDER, self.changeSharp4)

        # The Amplitude 4 Slider 
        self.amp4Text = wx.StaticText(self.panel, id=-1, label="LFO Amplitude", pos=(300, 460), size=wx.DefaultSize)
        self.amp4 = wx.Slider(self.panel, id=-1, value=100, minValue=20, maxValue=100, pos=(300, 480), size=(250, -1))
        self.amp4.Bind(wx.EVT_SLIDER, self.changeAmp4)    

        # The Type Choice 
        self.type4Text = wx.StaticText(self.panel, id=-1, label="LFO Type", pos=(300, 505), size=wx.DefaultSize)
        self.type4Choice = ["Saw", "Square", "Triangle", "Pulse", "Bipolar Pulse", "Sample & Hold", "Modulated Sine"]
        self.type4 = wx.Choice(self.panel, id=-1, pos=(390, 505), size=wx.DefaultSize, choices=self.type4Choice)
        self.type4.Bind(wx.EVT_CHOICE, self.changeType4)  


### LFO5 SINELOOP 3 : FREQ --------------

        # The LFO5 Button
        self.onlfo_5 = wx.ToggleButton(self.panel, id=-1, label="ON", pos=(780, 110), size=wx.DefaultSize)
        self.onlfo_5.Bind(wx.EVT_TOGGLEBUTTON, self.activelfo5)

        # The Freq 5 Slider 
        self.freq5Text = wx.StaticText(self.panel, id=-1, label="LFO Freq", pos=(620, 130), size=wx.DefaultSize)
        self.freq5 = wx.Slider(self.panel, id=-1, value=2, minValue=1, maxValue=50, pos=(620, 150), size=(250, -1))
        self.freq5.Bind(wx.EVT_SLIDER, self.changeFreq5)

        # The Sharp 5 Slider 
        self.sharp5Text = wx.StaticText(self.panel, id=-1, label="LFO Sharpness", pos=(620, 170), size=wx.DefaultSize)
        self.sharp5 = wx.Slider(self.panel, id=-1, value=50, minValue=0, maxValue=100, pos=(620, 190), size=(250, -1))
        self.sharp5.Bind(wx.EVT_SLIDER, self.changeSharp5)

        # The Amplitude 5 Slider 
        self.amp5Text = wx.StaticText(self.panel, id=-1, label="LFO Amplitude", pos=(620, 210), size=wx.DefaultSize)
        self.amp5 = wx.Slider(self.panel, id=-1, value=100, minValue=20, maxValue=100, pos=(620, 230), size=(250, -1))
        self.amp5.Bind(wx.EVT_SLIDER, self.changeAmp5)    

        # The Type Choice 
        self.type5Text = wx.StaticText(self.panel, id=-1, label="LFO Type", pos=(620, 255), size=wx.DefaultSize)
        self.type5Choice = ["Saw", "Square", "Triangle", "Pulse", "Bipolar Pulse", "Sample & Hold", "Modulated Sine"]
        self.type5 = wx.Choice(self.panel, id=-1, pos=(710, 255), size=wx.DefaultSize, choices=self.type5Choice)
        self.type5.Bind(wx.EVT_CHOICE, self.changeType5)  


### LFO6 SINELOOP 3 : FEEDBACK --------------

        # The LFO6 Button
        self.onlfo_6 = wx.ToggleButton(self.panel, id=-1, label="ON", pos=(1060, 110), size=wx.DefaultSize)
        self.onlfo_6.Bind(wx.EVT_TOGGLEBUTTON, self.activelfo6)

        # The Freq 6 Slider 
        self.freq6Text = wx.StaticText(self.panel, id=-1, label="LFO Freq", pos=(900, 130), size=wx.DefaultSize)
        self.freq6 = wx.Slider(self.panel, id=-1, value=2, minValue=1, maxValue=300, pos=(900, 150), size=(250, -1))
        self.freq6.Bind(wx.EVT_SLIDER, self.changeFreq6)

        # The Sharp 6 Slider 
        self.sharp6Text = wx.StaticText(self.panel, id=-1, label="LFO Sharpness", pos=(900, 170), size=wx.DefaultSize)
        self.sharp6 = wx.Slider(self.panel, id=-1, value=50, minValue=0, maxValue=100, pos=(900, 190), size=(250, -1))
        self.sharp6.Bind(wx.EVT_SLIDER, self.changeSharp6)

        # The Amplitude 6 Slider 
        self.amp6Text = wx.StaticText(self.panel, id=-1, label="LFO Amplitude", pos=(900, 210), size=wx.DefaultSize)
        self.amp6 = wx.Slider(self.panel, id=-1, value=100, minValue=20, maxValue=100, pos=(900, 230), size=(250, -1))
        self.amp6.Bind(wx.EVT_SLIDER, self.changeAmp6)

        # The Type Choice 
        self.type6Text = wx.StaticText(self.panel, id=-1, label="LFO Type", pos=(900, 255), size=wx.DefaultSize)
        self.type6Choice = ["Saw", "Square", "Triangle", "Pulse", "Bipolar Pulse", "Sample & Hold", "Modulated Sine"]
        self.type6 = wx.Choice(self.panel, id=-1, pos=(990, 255), size=wx.DefaultSize, choices=self.type6Choice)
        self.type6.Bind(wx.EVT_CHOICE, self.changeType6)     


### LFO7 SINELOOP 4 : FREQ --------------

        # The LFO7 Button
        self.onlfo_7 = wx.ToggleButton(self.panel, id=-1, label="ON", pos=(780, 360), size=wx.DefaultSize)
        self.onlfo_7.Bind(wx.EVT_TOGGLEBUTTON, self.activelfo7)

        # The Freq 7 Slider 
        self.freq7Text = wx.StaticText(self.panel, id=-1, label="LFO Freq", pos=(620, 380), size=wx.DefaultSize)
        self.freq7 = wx.Slider(self.panel, id=-1, value=2, minValue=1, maxValue=50, pos=(620, 400), size=(250, -1))
        self.freq7.Bind(wx.EVT_SLIDER, self.changeFreq7)

        # The Sharp 7 Slider 
        self.sharp7Text = wx.StaticText(self.panel, id=-1, label="LFO Sharpness", pos=(620, 420), size=wx.DefaultSize)
        self.sharp7 = wx.Slider(self.panel, id=-1, value=50, minValue=0, maxValue=100, pos=(620, 440), size=(250, -1))
        self.sharp7.Bind(wx.EVT_SLIDER, self.changeSharp7)

        # The Amplitude 7 Slider 
        self.amp7Text = wx.StaticText(self.panel, id=-1, label="LFO Amplitude", pos=(620, 460), size=wx.DefaultSize)
        self.amp7 = wx.Slider(self.panel, id=-1, value=100, minValue=20, maxValue=100, pos=(620, 480), size=(250, -1))
        self.amp7.Bind(wx.EVT_SLIDER, self.changeAmp7)    

        # The Type Choice 
        self.type7Text = wx.StaticText(self.panel, id=-1, label="LFO Type", pos=(620, 505), size=wx.DefaultSize)
        self.type7Choice = ["Saw", "Square", "Triangle", "Pulse", "Bipolar Pulse", "Sample & Hold", "Modulated Sine"]
        self.type7 = wx.Choice(self.panel, id=-1, pos=(710, 505), size=wx.DefaultSize, choices=self.type7Choice)
        self.type7.Bind(wx.EVT_CHOICE, self.changeType7)  


### LFO8 SINELOOP 4 : FEEDBACK --------------

        # The LFO8 Button
        self.onlfo_8 = wx.ToggleButton(self.panel, id=-1, label="ON", pos=(1060, 360), size=wx.DefaultSize)
        self.onlfo_8.Bind(wx.EVT_TOGGLEBUTTON, self.activelfo8)

        # The Freq 8 Slider 
        self.freq8Text = wx.StaticText(self.panel, id=-1, label="LFO Freq", pos=(900, 380), size=wx.DefaultSize)
        self.freq8 = wx.Slider(self.panel, id=-1, value=2, minValue=1, maxValue=300, pos=(900, 400), size=(250, -1))
        self.freq8.Bind(wx.EVT_SLIDER, self.changeFreq8)

        # The Sharp 8 Slider 
        self.sharp8Text = wx.StaticText(self.panel, id=-1, label="LFO Sharpness", pos=(900, 420), size=wx.DefaultSize)
        self.sharp8 = wx.Slider(self.panel, id=-1, value=50, minValue=0, maxValue=100, pos=(900, 440), size=(250, -1))
        self.sharp8.Bind(wx.EVT_SLIDER, self.changeSharp8)

        # The Amplitude 8 Slider 
        self.amp8Text = wx.StaticText(self.panel, id=-1, label="LFO Amplitude", pos=(900, 460), size=wx.DefaultSize)
        self.amp8 = wx.Slider(self.panel, id=-1, value=100, minValue=20, maxValue=100, pos=(900, 480), size=(250, -1))
        self.amp8.Bind(wx.EVT_SLIDER, self.changeAmp8)    

        # The Type Choice 
        self.type8Text = wx.StaticText(self.panel, id=-1, label="LFO Type", pos=(900, 505), size=wx.DefaultSize)
        self.type8Choice = ["Saw", "Square", "Triangle", "Pulse", "Bipolar Pulse", "Sample & Hold", "Modulated Sine"]
        self.type8 = wx.Choice(self.panel, id=-1, pos=(990, 505), size=wx.DefaultSize, choices=self.type4Choice)
        self.type8.Bind(wx.EVT_CHOICE, self.changeType8)  



        
### LINES & TEXT --------------
        
        # The Source
        self.sourceBox = wx.StaticLine(self.panel, -1, style=wx.LI_VERTICAL, pos=(10, 30), size=(555, 80))
        # Master Frequency 1
        self.master1Box = wx.StaticLine(self.panel, -1, style=wx.LI_VERTICAL, pos=(10, 30), size=(280, 80))
        # Master Frequency 1 + LFO1
        self.master1Box = wx.StaticLine(self.panel, -1, style=wx.LI_VERTICAL, pos=(10, 30), size=(280, 260))
        # Master Feedback 1
        self.master1Box = wx.StaticLine(self.panel, -1, style=wx.LI_VERTICAL, pos=(284, 30), size=(280, 80))
        # Master Feedback 1 + LFO2
        self.master1Box = wx.StaticLine(self.panel, -1, style=wx.LI_VERTICAL, pos=(284, 30), size=(280, 260))

        # The Source 2
        self.sourceBox = wx.StaticLine(self.panel, -1, style=wx.LI_VERTICAL, pos=(10, 280), size=(555, 80))
        # Master Frequency 2
        self.master1Box = wx.StaticLine(self.panel, -1, style=wx.LI_VERTICAL, pos=(10, 280), size=(280, 80))
        # Master Frequency 2 + LFO3
        self.master1Box = wx.StaticLine(self.panel, -1, style=wx.LI_VERTICAL, pos=(10, 280), size=(280, 260))
        # Master Feedback 2 
        self.master1Box = wx.StaticLine(self.panel, -1, style=wx.LI_VERTICAL, pos=(284, 280), size=(280, 80))
        # Master Feedback 2 + LFO4
        self.master1Box = wx.StaticLine(self.panel, -1, style=wx.LI_VERTICAL, pos=(284, 280), size=(280, 260))

        # The Source 3
        self.sourceBox = wx.StaticLine(self.panel, -1, style=wx.LI_VERTICAL, pos=(610, 30), size=(555, 80))
        # Master Frequency 3
        self.master1Box = wx.StaticLine(self.panel, -1, style=wx.LI_VERTICAL, pos=(610, 30), size=(280, 80))
        # Master Frequency 3 + LFO5
        self.master1Box = wx.StaticLine(self.panel, -1, style=wx.LI_VERTICAL, pos=(610, 30), size=(280, 260))
        # Master Feedback 3
        self.master1Box = wx.StaticLine(self.panel, -1, style=wx.LI_VERTICAL, pos=(884, 30), size=(280, 80))
        # Master Feedback 3 + LFO6
        self.master1Box = wx.StaticLine(self.panel, -1, style=wx.LI_VERTICAL, pos=(884, 30), size=(280, 260))
        
        # The Source 4
        self.sourceBox = wx.StaticLine(self.panel, -1, style=wx.LI_VERTICAL, pos=(610, 280), size=(555, 80))
        # Master Frequency 4
        self.master1Box = wx.StaticLine(self.panel, -1, style=wx.LI_VERTICAL, pos=(610, 280), size=(280, 80))
        # Master Frequency 4 + LFO7
        self.master1Box = wx.StaticLine(self.panel, -1, style=wx.LI_VERTICAL, pos=(610, 280), size=(280, 260))
        # Master Feedback 4
        self.master1Box = wx.StaticLine(self.panel, -1, style=wx.LI_VERTICAL, pos=(884, 280), size=(280, 80))
        # Master Feedback 4 + LFO8
        self.master1Box = wx.StaticLine(self.panel, -1, style=wx.LI_VERTICAL, pos=(884, 280), size=(280, 260))


            
#############################################  GUI TO PROGRAM FUNCTIONS  ###########################################


#------ REC
    def doREC(self, evt):
        x = evt.GetInt()
        if (x ==1):
            saveBox = wx.TextEntryDialog(None, "File name ? (will be saved on desktop)", "Saving", "GRYN_rec")
            if saveBox.ShowModal()==wx.ID_OK:
                saveName = saveBox.GetValue()
                print saveName
                s.recstart(filename=desktop + saveName + ".wav")
        else:
            s.recstop()

#------ EXIT
    def doExit(self, evt):
        sys.exit(0)

#------ SHOW SYNC
    def showSync(self, evt):
        x = evt.GetInt()
        if x==1:
            self.freq1Text.SetForegroundColour((255, 0, 0))
            self.freq2Text.SetForegroundColour((255, 0, 0))
            self.freq3Text.SetForegroundColour((255, 0, 0))
            self.freq4Text.SetForegroundColour((255, 0, 0))
            self.freq5Text.SetForegroundColour((255, 0, 0))
            self.freq6Text.SetForegroundColour((255, 0, 0))
            self.freq7Text.SetForegroundColour((255, 0, 0))
            self.freq8Text.SetForegroundColour((255, 0, 0))
            self.freq1.SetValue(30)
            self.freq2.SetValue(30)
            self.freq3.SetValue(30)
            self.freq4.SetValue(30)
            self.freq5.SetValue(30)
            self.freq6.SetValue(30)
            self.freq7.SetValue(30)
            self.freq8.SetValue(30)
            self.sync1.Show()
        if x==0:
            self.freq1Text.SetForegroundColour((0, 0, 0))
            self.freq2Text.SetForegroundColour((0, 0, 0))
            self.freq3Text.SetForegroundColour((0, 0, 0))
            self.freq4Text.SetForegroundColour((0, 0, 0))
            self.freq5Text.SetForegroundColour((0, 0, 0))
            self.freq6Text.SetForegroundColour((0, 0, 0))
            self.freq7Text.SetForegroundColour((0, 0, 0))
            self.freq8Text.SetForegroundColour((0, 0, 0))
            self.sync1.Hide()

    def doSyncFreq(self, evt):
        x = evt.GetInt()
        self.freq1.SetValue(x)
        self.freq2.SetValue(x)
        self.freq3.SetValue(x)
        self.freq4.SetValue(x)
        self.freq5.SetValue(x)
        self.freq6.SetValue(x)
        self.freq7.SetValue(x)
        self.freq8.SetValue(x)
        lfo_1.setFreq(x)
        lfo_2.setFreq(x)
        lfo_3.setFreq(x)
        lfo_4.setFreq(x)
        lfo_5.setFreq(x)
        lfo_6.setFreq(x)
        lfo_7.setFreq(x)
        lfo_8.setFreq(x)




#------ THE CHAOS

    def doChaos(self, evt):
        global active1
        global master_frequency
        global active2
        global master_feedback
    #----Master Freq 1
        randomFrequency1 = random.uniform(40, 800)
        self.masterFreq1.SetValue(randomFrequency1)
        master_frequency1 = randomFrequency1
        if active1 == 0:
            sine_1.setFreq(randomFrequency1)
        if active1 == 1:
            sine_1.setFreq(randomFrequency1*lfo_1)
    #----Master Feedback 1
        randomFeedback1 = random.uniform(0, 100) 
        self.masterFeedback1.SetValue(randomFeedback1)
        randomFeedbackFloat1 = randomFeedback1 * 0.01
        master_feedback1 = randomFeedbackFloat1
        if active2 == 0:
            sine_1.setFeedback(randomFeedbackFloat1)
        if active2 == 1:
            sine_1.setFeedback(randomFeedbackFloat1*lfo_2)
    #----Master Freq 2
        randomFrequency2 = random.uniform(40, 800)
        self.masterFreq2.SetValue(randomFrequency2)
        master_frequency2 = randomFrequency2
        if active3 == 0:
            sine_2.setFreq(randomFrequency2)
        if active3 == 1:
            sine_2.setFreq(randomFrequency2*lfo_3)
    #----Master Feedback 2
        randomFeedback2 = random.uniform(0, 100) 
        self.masterFeedback2.SetValue(randomFeedback2)
        randomFeedbackFloat2 = randomFeedback2 * 0.01
        master_feedback2 = randomFeedbackFloat2
        if active4 == 0:
            sine_2.setFeedback(randomFeedbackFloat2)
        if active4 == 1:
            sine_2.setFeedback(randomFeedbackFloat2*lfo_4)
    #----Master Freq 3
        randomFrequency3 = random.uniform(40, 800)
        self.masterFreq3.SetValue(randomFrequency3)
        master_frequency3 = randomFrequency3
        if active5 == 0:
            sine_3.setFreq(randomFrequency3)
        if active5 == 1:
            sine_3.setFreq(randomFrequency3*lfo_5)
    #----Master Feedback 3
        randomFeedback3 = random.uniform(0, 100) 
        self.masterFeedback3.SetValue(randomFeedback3)
        randomFeedbackFloat3 = randomFeedback3 * 0.01
        master_feedback3 = randomFeedbackFloat3
        if active6 == 0:
            sine_3.setFeedback(randomFeedbackFloat3)
        if active6 == 1:
            sine_3.setFeedback(randomFeedbackFloat3*lfo_6)
    #----Master Freq 4
        randomFrequency4 = random.uniform(40, 800)
        self.masterFreq4.SetValue(randomFrequency4)
        master_frequency4 = randomFrequency4
        if active7 == 0:
            sine_4.setFreq(randomFrequency4)
        if active7 == 1:
            sine_4.setFreq(randomFrequency4*lfo_7)
    #----Master Feedback 4
        randomFeedback4 = random.uniform(0, 100) 
        self.masterFeedback4.SetValue(randomFeedback4)
        randomFeedbackFloat4 = randomFeedback4 * 0.01
        master_feedback4 = randomFeedbackFloat4
        if active8 == 0:
            sine_4.setFeedback(randomFeedbackFloat4)
        if active8 == 1:
            sine_4.setFeedback(randomFeedbackFloat4*lfo_8)
    #----LFO 1
        #---Freq
        randomFreq1 = random.uniform(1, 50)
        self.freq1.SetValue(randomFreq1)
        lfo_1.setFreq(randomFreq1)
        #---Sharp
        randomSharp1 = random.uniform(0, 100)
        self.sharp1.SetValue(randomSharp1)
        randomSharp1Float = randomSharp1 * 0.01
        lfo_1.setSharp(randomSharp1Float)
        #---Amp
        randomAmp1 = random.uniform(0, 100)
        self.amp1.SetValue(randomAmp1)
        randomAmp1Float = randomAmp1 * 0.01
        lfo_1.setMul(randomAmp1Float)
        #---Type
        randomType1 = random.uniform(0,6)
        self.type1.SetSelection(randomType1)
        lfo_1.setType(int(randomType1)+1)
    #----LFO 2
        #---Freq
        randomFreq2 = random.uniform(1, 300)
        self.freq2.SetValue(randomFreq2)
        lfo_2.setFreq(randomFreq2)
        #---Sharp
        randomSharp2 = random.uniform(0, 100)
        self.sharp2.SetValue(randomSharp2)
        randomSharp2Float = randomSharp2 * 0.01
        lfo_2.setSharp(randomSharp2Float)
        #---Amp
        randomAmp2 = random.uniform(0, 100)
        self.amp2.SetValue(randomAmp2)
        randomAmp2Float = randomAmp2 * 0.01
        lfo_2.setMul(randomAmp2Float)
        #---Type
        randomType2 = random.uniform(0,6)
        self.type2.SetSelection(randomType2)
        lfo_2.setType(int(randomType2)+1)
    #----LFO 3
        #---Freq
        randomFreq3 = random.uniform(1, 50)
        self.freq3.SetValue(randomFreq3)
        lfo_3.setFreq(randomFreq3)
        #---Sharp
        randomSharp3 = random.uniform(0, 100)
        self.sharp3.SetValue(randomSharp3)
        randomSharp3Float = randomSharp3 * 0.01
        lfo_3.setSharp(randomSharp3Float)
        #---Amp
        randomAmp3 = random.uniform(0, 100)
        self.amp3.SetValue(randomAmp3)
        randomAmp3Float = randomAmp3 * 0.01
        lfo_3.setMul(randomAmp3Float)
        #---Type
        randomType3 = random.uniform(0,6)
        self.type3.SetSelection(randomType3)
        lfo_3.setType(int(randomType3)+1)        
    #----LFO 4
        #---Freq
        randomFreq4 = random.uniform(1, 300)
        self.freq4.SetValue(randomFreq4)
        lfo_4.setFreq(randomFreq4)
        #---Sharp
        randomSharp4 = random.uniform(0, 100)
        self.sharp4.SetValue(randomSharp4)
        randomSharp4Float = randomSharp4 * 0.01
        lfo_4.setSharp(randomSharp4Float)
        #---Amp
        randomAmp4 = random.uniform(0, 100)
        self.amp4.SetValue(randomAmp4)
        randomAmp4Float = randomAmp4 * 0.01
        lfo_4.setMul(randomAmp4Float)
        #---Type
        randomType4 = random.uniform(0,6)
        self.type4.SetSelection(randomType4)
        lfo_4.setType(int(randomType4)+1) 
    #----LFO 5
        #---Freq
        randomFreq5 = random.uniform(1, 50)
        self.freq5.SetValue(randomFreq5)
        lfo_5.setFreq(randomFreq5)
        #---Sharp
        randomSharp5 = random.uniform(0, 100)
        self.sharp5.SetValue(randomSharp5)
        randomSharp5Float = randomSharp5 * 0.01
        lfo_5.setSharp(randomSharp5Float)
        #---Amp
        randomAmp5 = random.uniform(0, 100)
        self.amp5.SetValue(randomAmp5)
        randomAmp5Float = randomAmp5 * 0.01
        lfo_5.setMul(randomAmp5Float)
        #---Type
        randomType5 = random.uniform(0,6)
        self.type5.SetSelection(randomType5)
        lfo_5.setType(int(randomType5)+1)
    #----LFO 6
        #---Freq
        randomFreq6 = random.uniform(1, 300)
        self.freq6.SetValue(randomFreq6)
        lfo_6.setFreq(randomFreq6)
        #---Sharp
        randomSharp6 = random.uniform(0, 100)
        self.sharp6.SetValue(randomSharp6)
        randomSharp6Float = randomSharp6 * 0.01
        lfo_6.setSharp(randomSharp6Float)
        #---Amp
        randomAmp6 = random.uniform(0, 100)
        self.amp6.SetValue(randomAmp6)
        randomAmp6Float = randomAmp6 * 0.01
        lfo_6.setMul(randomAmp6Float)
        #---Type
        randomType6 = random.uniform(0,6)
        self.type6.SetSelection(randomType6)
        lfo_6.setType(int(randomType6)+1)
    #----LFO 7
        #---Freq
        randomFreq7 = random.uniform(1, 50)
        self.freq7.SetValue(randomFreq7)
        lfo_7.setFreq(randomFreq7)
        #---Sharp
        randomSharp7 = random.uniform(0, 100)
        self.sharp7.SetValue(randomSharp7)
        randomSharp7Float = randomSharp7 * 0.01
        lfo_7.setSharp(randomSharp7Float)
        #---Amp
        randomAmp7 = random.uniform(0, 100)
        self.amp7.SetValue(randomAmp7)
        randomAmp7Float = randomAmp7 * 0.01
        lfo_7.setMul(randomAmp7Float)
        #---Type
        randomType7 = random.uniform(0,6)
        self.type7.SetSelection(randomType7)
        lfo_7.setType(int(randomType7)+1)        
    #----LFO 8
        #---Freq
        randomFreq8 = random.uniform(1, 300)
        self.freq8.SetValue(randomFreq8)
        lfo_8.setFreq(randomFreq8)
        #---Sharp
        randomSharp8 = random.uniform(0, 100)
        self.sharp8.SetValue(randomSharp8)
        randomSharp8Float = randomSharp8 * 0.01
        lfo_8.setSharp(randomSharp8Float)
        #---Amp
        randomAmp8 = random.uniform(0, 100)
        self.amp8.SetValue(randomAmp8)
        randomAmp8Float = randomAmp8 * 0.01
        lfo_8.setMul(randomAmp8Float)
        #---Type
        randomType8 = random.uniform(0,6)
        self.type8.SetSelection(randomType8)
        lfo_8.setType(int(randomType8)+1) 

        """
#------ THE CHRONOS
    def doChronos(self, evt):
    #----LFO 1
        #---Freq
        lfo1freqchronos = Randi(min=1, max=50, freq=.1, mul=1, add=0)
        lfo_1.setFreq(lfo1freqchronos)
        while(1):
            self.freq1.SetValue(int(lfo1freqchronos.get()))             
        #---Sharp
        lfo_1.setSharp(Randi(min=0.00, max=1.00, freq=.1, mul=1, add=0))
        #---Amp
        lfo_1.setMul(Randi(min=0.00, max=1.00, freq=.2, mul=1, add=0))
    #----LFO 2
        #---Freq
        lfo_2.setFreq(Randi(min=1, max=300, freq=.3, mul=1, add=0))
        #---Sharp
        lfo_2.setSharp(Randi(min=0.00, max=1.00, freq=.05, mul=1, add=0))
        #---Amp
        lfo_2.setMul(Randi(min=0.00, max=1.00, freq=1.00, mul=1, add=0))
    #----LFO 3
        #---Freq
        lfo_3.setFreq(Randi(min=1, max=50, freq=.01, mul=1, add=0))
        #---Sharp
        lfo_3.setSharp(Randi(min=0.00, max=1.00, freq=.7, mul=1, add=0))
        #---Amp
        lfo_3.setMul(Randi(min=0.00, max=1.00, freq=.4, mul=1, add=0))
    #----LFO 4
        #---Freq
        lfo_4.setFreq(Randi(min=1, max=300, freq=.3, mul=1, add=0))
        #---Sharp
        lfo_4.setSharp(Randi(min=0.00, max=1.00, freq=.2, mul=1, add=0))
        #---Amp
        lfo_4.setMul(Randi(min=0.00, max=1.00, freq=.1, mul=1, add=0))
        """
        

#------ THE SOURCE 

    def changeMasterFreq1(self, evt):
        global active1
        global master_frequency1
        x = evt.GetInt() 
        master_frequency1 = x
        if active1 == 0:
            sine_1.setFreq(x)
        if active1 == 1:
            sine_1.setFreq(x*lfo_1)         

    def changeMasterFeedback1(self, evt):
        global active2
        global master_feedback1
        x = evt.GetInt() * 0.01
        master_feedback1 = x
        if active2 == 0:
            sine_1.setFeedback(x)
        if active2 == 1:
            sine_1.setFeedback(x*lfo_2)

    def changeVolume1(self, evt):
        x = evt.GetInt() 
        filter_1.setFreq(x)

    #---

    def changeMasterFreq2(selt, evt):
        global active3
        global master_frequency2
        x = evt.GetInt() 
        master_frequency2 = x
        if active3 == 0:
            sine_2.setFreq(x)
        if active3 == 1:
            sine_2.setFreq(x*lfo_3)         

    def changeMasterFeedback2(self, evt):
        global active4
        global master_feedback2
        x = evt.GetInt() * 0.01
        master_feedback2 = x
        if active4 == 0:
            sine_2.setFeedback(x)
        if active4 == 1:
            sine_2.setFeedback(x*lfo_4)

    def changeVolume2(self, evt):
        x = evt.GetInt() 
        filter_2.setFreq(x)

    #---

    def changeMasterFreq3(self, evt):
        global active5
        global master_frequency3
        x = evt.GetInt() 
        master_frequency3 = x
        if active5 == 0:
            sine_3.setFreq(x)
        if active5 == 1:
            sine_3.setFreq(x*lfo_5)         

    def changeMasterFeedback3(self, evt):
        global active6
        global master_feedback3
        x = evt.GetInt() * 0.01
        master_feedback3 = x
        if active6 == 0:
            sine_3.setFeedback(x)
        if active6 == 1:
            sine_3.setFeedback(x*lfo_6)

    def changeVolume3(self, evt):
        x = evt.GetInt() 
        filter_3.setFreq(x)

    #---

    def changeMasterFreq4(selt, evt):
        global active7
        global master_frequency4
        x = evt.GetInt() 
        master_frequency4 = x
        if active7 == 0:
            sine_4.setFreq(x)
        if active7 == 1:
            sine_4.setFreq(x*lfo_7)         

    def changeMasterFeedback4(self, evt):
        global active8
        global master_feedback4
        x = evt.GetInt() * 0.01
        master_feedback4 = x
        if active8 == 0:
            sine_4.setFeedback(x)
        if active8 == 1:
            sine_4.setFeedback(x*lfo_8)

    def changeVolume4(self, evt):
        x = evt.GetInt() 
        filter_4.setFreq(x)

#------ LFO 1 : MODIFY FREQUENCY OF SINELOOP 1

    def activelfo1(self, evt):
        global active1
        x = evt.GetInt() 
        if x == 0:
            active1 = 0
            sine_1.setFreq(master_frequency)
        if x == 1:
            active1 = 1
            sine_1.setFreq(master_frequency*lfo_1)

        
    def changeFreq1(self, evt):
        x = evt.GetInt() 
        lfo_1.setFreq(x)

    def changeSharp1(self, evt):
        x = evt.GetInt() * 0.01
        lfo_1.setSharp(x)

    def changeAmp1(self, evt):
        x = evt.GetInt() * 0.01
        lfo_1.setMul(x)

    def changeType1(self, evt):
        x = evt.GetInt()
        lfo_1.setType(x+1)


#------ LFO 2 : MODIFY FEEDBACK OF SINELOOP 1

    def activelfo2(self, evt):
        global active2
        x = evt.GetInt() 
        if x == 0:
            active2 = 0
            sine_1.setFeedback(master_feedback)
        if x == 1:
            active2 = 1
            sine_1.setFeedback(master_feedback*lfo_2)
        
    def changeFreq2(self, evt):
        x = evt.GetInt() 
        lfo_2.setFreq(x)

    def changeSharp2(self, evt):
        x = evt.GetInt() * 0.01
        lfo_2.setSharp(x)

    def changeAmp2(self, evt):
        x = evt.GetInt() * 0.01
        lfo_2.setMul(x)

    def changeType2(self, evt):
        x = evt.GetInt()
        lfo_2.setType(x+1)


#------ LFO 3 : MODIFY FREQUENCY OF SINELOOP 2

    def activelfo3(self, evt):
        global active3
        x = evt.GetInt() 
        if x == 0:
            active3 = 0
            sine_2.setFreq(master_frequency2)
        if x == 1:
            active3 = 1
            sine_2.setFreq(master_frequency2*lfo_3)
        
    def changeFreq3(self, evt):
        x = evt.GetInt() 
        lfo_3.setFreq(x)

    def changeSharp3(self, evt):
        x = evt.GetInt() * 0.01
        lfo_3.setSharp(x)

    def changeAmp3(self, evt):
        x = evt.GetInt() * 0.01
        lfo_3.setMul(x)

    def changeType3(self, evt):
        x = evt.GetInt()
        lfo_3.setType(x+1)

#------ LFO 4 : MODIFY FEEDBACK OF SINELOOP 2

    def activelfo4(self, evt):
        global active4
        x = evt.GetInt() 
        if x == 0:
            active4 = 0
            sine_2.setFeedback(master_feedback2)
        if x == 1:
            active4 = 1
            sine_2.setFeedback(master_feedback2*lfo_4)
        
    def changeFreq4(self, evt):
        x = evt.GetInt() 
        lfo_4.setFreq(x)

    def changeSharp4(self, evt):
        x = evt.GetInt() * 0.01
        lfo_4.setSharp(x)

    def changeAmp4(self, evt):
        x = evt.GetInt() * 0.01
        lfo_4.setMul(x)

    def changeType4(self, evt):
        x = evt.GetInt()
        lfo_4.setType(x+1)

#------ LFO 5 : MODIFY FREQUENCY OF SINELOOP 3

    def activelfo5(self, evt):
        global active5
        x = evt.GetInt() 
        if x == 0:
            active5 = 0
            sine_3.setFreq(master_frequency3)
        if x == 1:
            active5 = 1
            sine_3.setFreq(master_frequency3*lfo_5)
        
    def changeFreq5(self, evt):
        x = evt.GetInt() 
        lfo_5.setFreq(x)

    def changeSharp5(self, evt):
        x = evt.GetInt() * 0.01
        lfo_5.setSharp(x)

    def changeAmp5(self, evt):
        x = evt.GetInt() * 0.01
        lfo_5.setMul(x)

    def changeType5(self, evt):
        x = evt.GetInt()
        lfo_5.setType(x+1)

#------ LFO 6 : MODIFY FEEDBACK OF SINELOOP 3

    def activelfo6(self, evt):
        global active6
        x = evt.GetInt() 
        if x == 0:
            active6 = 0
            sine_3.setFeedback(master_feedback3)
        if x == 1:
            active6 = 1
            sine_3.setFeedback(master_feedback3*lfo_6)
        
    def changeFreq6(self, evt):
        x = evt.GetInt() 
        lfo_6.setFreq(x)

    def changeSharp6(self, evt):
        x = evt.GetInt() * 0.01
        lfo_6.setSharp(x)

    def changeAmp6(self, evt):
        x = evt.GetInt() * 0.01
        lfo_6.setMul(x)

    def changeType6(self, evt):
        x = evt.GetInt()
        lfo_6.setType(x+1)

#------ LFO 7 : MODIFY FREQUENCY OF SINELOOP 4

    def activelfo7(self, evt):
        global active7
        x = evt.GetInt() 
        if x == 0:
            active7 = 0
            sine_4.setFreq(master_frequency4)
        if x == 1:
            active7 = 1
            sine_4.setFreq(master_frequency4*lfo_7)
        
    def changeFreq7(self, evt):
        x = evt.GetInt() 
        lfo_7.setFreq(x)

    def changeSharp7(self, evt):
        x = evt.GetInt() * 0.01
        lfo_7.setSharp(x)

    def changeAmp7(self, evt):
        x = evt.GetInt() * 0.01
        lfo_7.setMul(x)

    def changeType7(self, evt):
        x = evt.GetInt()
        lfo_7.setType(x+1)

#------ LFO 8 : MODIFY FEEDBACK OF SINELOOP 4

    def activelfo8(self, evt):
        global active8
        x = evt.GetInt() 
        if x == 0:
            active8 = 0
            sine_4.setFeedback(master_feedback4)
        if x == 1:
            active8 = 1
            sine_4.setFeedback(master_feedback4*lfo_8)
        
    def changeFreq8(self, evt):
        x = evt.GetInt() 
        lfo_8.setFreq(x)

    def changeSharp8(self, evt):
        x = evt.GetInt() * 0.01
        lfo_8.setSharp(x)

    def changeAmp8(self, evt):
        x = evt.GetInt() * 0.01
        lfo_8.setMul(x)

    def changeType8(self, evt):
        x = evt.GetInt()
        lfo_8.setType(x+1)
    
        
        
if __name__ =='__main__':
    app = wx.App()
    mainFrame = MyFrame(None, title=NAME + " " + VERSION, pos=(100, 100), size=(1180, 600))
    mainFrame.Show()
    app.MainLoop()