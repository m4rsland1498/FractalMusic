import pygame
import random
import cmath
import time
import numpy as np

# Julia set equation: z_{n+1} = (z_n)^p + c

def juliaFractal (width, height, p, c, max_iterations, gamma=2):
    pixels=[]
    for y in range(height):
        for x in range(width):
            zx = (x-width/2)*4/width
            zy = (y-height/2)*4/height
            z = complex(zx, zy)
            iterations = 0
            while abs(z) < 2 and iterations < max_iterations:
                z = z**p + c
                iterations += 1
            colour = (iterations%256, (iterations*2)%256, (iterations*4)%256)
            colour = tuple(int(255 * (val / 255) ** (1/gamma)) for val in colour)
            pixels.append(colour)
    return pixels

def displayJulia(width, height, pixels):
    screen = pygame.display.set_mode((width, height))
    for i, colour in enumerate(pixels):
        x = i%width
        y = i//width
        screen.set_at((x, y), colour)
    pygame.display.flip()

def songGen(p1,p2,c1,c2,song):
    pygame.mixer.init(frequency=44100, channels=1)

    # Sampling rate and duration
    sample_rate = 44100
    duration = 0.25
    frequency = random.choice([p1,c1])
    if frequency == p1:
        frequency = frequency*100
    else:
        frequency = frequency*450*c2

    # Generate sine wave
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = np.sin(2 * np.pi * frequency * t)

    # Normalize the wave to fit within 16-bit range
    normalisedWave = np.int16(wave / np.max(np.abs(wave)) * 32767)

    # Convert the wave to bytes
    sound = pygame.mixer.Sound(normalisedWave)

    song.append(sound)

def main():
    pygame.init()
    width, height = 1000, 900
    p1 = random.uniform(1,3)
    p2 = 0
    c1 = random.uniform(-1,1)
    c2 = random.uniform(-1,1)
    p = complex(p1, p2)
    c = complex(c1, c2)
    max_iterations = 100
    song = []
    print(p,c)

    pixels = juliaFractal(width, height, p, c, max_iterations)
    displayJulia(width, height, pixels)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for i in range(10):
            songGen(p1,p2,c1,c2,song)
        for i in song:
            i.play()
            time.sleep(0.25)
    pygame.quit()

main()