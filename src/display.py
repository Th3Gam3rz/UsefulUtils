import time

def clear():
    print("\n"*100)

def animate(sequence,length=1,loop=10,firstClear=True):
    if loop == -1:
        if firstClear == True:
            clear()
        while True:
            for seq in sequence:
                print(seq)
                time.sleep(length)
                clear()
    else:
        if firstClear == True:
            clear()
        counter = 0
        while counter < loop:
            for seq in sequence:
                print(seq)
                time.sleep(length)
                clear()
            counter += 1

def animateText(text, delay=0.05):
    for x in text:
        print(x, end='')
        time.sleep(delay)
