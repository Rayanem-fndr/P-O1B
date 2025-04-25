from machine import Pin, PWM
import time
rood=PWM(pin16)
groen=PWM(pin17)
blauw=PWM(pin18)

rood.freq(1000)
groen.freq(1000)
blauw.freq(1000)

def kleur(r,g,b):
    rood.duty_u16(int(r * 65535 / 255))
    groen.duty_u16(int(g * 65535 / 255))
    blauw.duty_u16(int(b * 65535 / 255))



def rijden():
    #wit en groen
    #RGB(t) = (L(t), 1, L(t))*255 t in seconden
    while True:
        L = 0.5 + (0.5 * sin(2 * pi * time.monotonic()))  # L tussen 0 en 1
        L_255 = int(L * 255)  # Omzetten naar 8-bit waarde (0-255)
        kleur(L_255, 255, L_255)
        time.sleep(0.05) #zou helpen voor een betere overgang

def oppakken():
    #oranje (224,163,46)
    #aan uit
    while True:
        kleur(224,163,46)
        time.sleep(0.5)
        kleur(0,0,0)
        time.sleep(0.5)

def achteruit():
    #rood (1,0,0)*255
    #aan uit
    while True:
        kleur(255,0,0)
        time.sleep(0.5)
        kleur(0,0,0)
        time.sleep(0.5)

def terugrijden():
    #blauw (0,0,1)*255
    #constant
    while True:
        kleur(0,0,255)
