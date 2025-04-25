import time
import board
from machine import pin,PWM

speaker=PWM(pin("pin nummer")

def trage_toon():
    speaker.frequency("geef de frequentie")
    speaker.duty_cycle() # plaats hier een waarde groter dan 0
    time.sleep("hoe lang voor hij uit gaat") #maak dit groter dan bij de rappe toon
    speaker.duty_cycle(0) #speaker gaat uit
    time.sleep("hoe lang voor hij weer aan gaat")

def rappe_toon():
    speaker.frequency("geef de frequentie")
    speaker.duty_cycle() # plaats hier een waarde groter dan 0
    time.sleep("hoe lang voor hij uit gaat")
    speaker.duty_cycle(0) #speaker gaat uit
    time.sleep("hoe lang voor hij weer aan gaat")



while achteruit:
    trage_toon()

while oprapen:
    rappe_toon()



# Write your code here :-)
