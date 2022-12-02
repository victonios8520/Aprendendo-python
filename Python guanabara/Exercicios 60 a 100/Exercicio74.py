import random 
import os

os.system('clear')

pc = (random.randrange(0,10),random.randrange(0,10),random.randrange(0,10),random.randrange(0,10))

print(f'Os valores gerados foram :{pc}')
print(f'O maior valor é {max(pc)}')
print(f'O menor valor é {min(pc)}')