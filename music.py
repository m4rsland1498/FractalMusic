import numpy as np
import pygame
import time
import random
import math

p1 = random.uniform(1,3)
p2 = 0
c1 = random.uniform(-1,1)
c2 = random.uniform(-1,1)
song=[]

def songGen(p1,p2,c1,c2,song):
    pygame.mixer.init(frequency=44100, channels=1)

    # Sampling rate and duration
    sample_rate = 44100
    duration = 0.25
    frequency = p1*100

    # Generate sine wave
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = np.sin(2 * np.pi * frequency * t)

    # Normalize the wave to fit within 16-bit range
    wave = np.int16(wave / np.max(np.abs(wave)) * 32767)

    # Convert the wave to bytes
    sound = pygame.sndarray.make_sound(wave)

    song.append(sound)

for i in range(10):
    songGen(random.uniform(1,3),p2,c1,c2,song)
for i in song:
    i.play()
    time.sleep(0.25)

"""
# Play the sound
sound.play()

# Wait until the sound has finished playing
time.sleep(duration)
"""