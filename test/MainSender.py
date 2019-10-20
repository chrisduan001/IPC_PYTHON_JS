import random
import sys
import time

i = 0
while i < 20:
    time.sleep(random.random() * 5)
    temperature = (random.random() * 20) - 5
    i = i + 1
    print(i)
    sys.stdout.flush()
exit(0)
