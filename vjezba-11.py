#igra

import random

tajnibroj = random.randint(1,30)

while True:

    pogodi = int(input("pogodi broj između 1 i 30: "))

    if pogodi == tajnibroj:
        print("bravo, pogodio si traženi broj!")
        break
    else:
        print("pogriješio si, probaj ponovno...")
