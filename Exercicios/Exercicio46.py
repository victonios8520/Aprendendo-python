import time 
import playsound

for c in range(10,-1,-1):
    time.sleep(1)
    print(c)
print("Fogos")
playsound.playsound("fogos.mp3")

