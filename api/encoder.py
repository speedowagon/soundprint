#import pyaudio
#import numpy as np
from __future__ import division
import sys
import math
import wave
import struct
import argparse
from itertools import *
import base64

from .models import Sound


def encode(usertext):

    bitrate = 44100       # sampling rate, Hz, must be integer
    duration = 0.01   # in seconds, may be float

    #create 2d list with each base-64 char linking to the respective sine wave frequency 
    base_64 = [chr(x) for x in (range(65,91)+range(97,123)+range(48,58)+[45,95])]

    def mysine(i):
        frequency = 400 + 50*i
        frames = int(bitrate*duration)
        samples = ''
        for x in range(frames):        
            samples = samples+chr(int(math.sin(x/((bitrate/frequency)/(2*math.pi)))*127+128))
        #(np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32) #generates sine wave using numpy
        return samples    
       
        
    elements = {x: mysine(n) for n, x in enumerate(base_64)}

    '''
    import pprint
    p = pprint.PrettyPrinter(width=50)
    p.pprint(elements)
    '''

    #encode text
    encoded = base64.urlsafe_b64encode(usertext) #replaces + with - and / with _
    #create sound file by starting stream
    wf = wave.open('soundprint.wav', 'w')
    wf.setparams((1,1,bitrate,0,'NONE','not compressed'))
    #convert each char in 64base string into sound
    for c in encoded.replace('=', ''):
        wf.writeframes(elements[c])
        #wf.writeframes(''.join([x for x in elements[c]]))
    wf.close
    return True


def handle(fname):

    # Generate Sound()
    s = Sound(soundprint=fname, message='mesg')
    s.save()

    return s.id()

