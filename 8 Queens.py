#8 Queens
#Need PIL (Python Image Library), installation file found in project folder

from Tkinter import *
from PIL import Image, ImageTk
import random

boardLength = 8
yLength = boardLength
xLength = boardLength
placed = []
count = 0
available = [[True for x in xrange(xLength)] for y in xrange(yLength)]

def place():
    global placed, count
    x = int(e1.get())
    y = int(e2.get())
    if([x, y] not in placed):
        if (len(placed) == 0):
            placed.append([x, y])
        else:
            placed.append([x, y])
        Button(root, bg="red", width=11, height=5).grid(row=y, column=x)
        count += 1
        if(count >= 8):
            Button(root, text="Check", command=check).grid(row=2, column=xLength, sticky = S)

def legal(placed, nextX):
    nextY = len(placed)
    for a in xrange(nextY):
        if abs(placed[a]-nextX) in (0, nextY-a):
            return False
    return True

def queens(num, placed = ()):
    for pos in xrange(num):
        if legal(placed, pos):
            if len(placed) == num-1:
                yield(pos,)
            else:
                for result in queens(num, placed + (pos,)):
                    yield(pos,) + result

def auto():
    global boardLength, solutionList
    solutionList = list(queens(boardLength))
    temp = random.choice(solutionList)
    Button(root, text="Find Solution", command=another).grid(row=4, column=xLength, sticky=S)
    for x in xrange(boardLength):
        for y in xrange(boardLength):
            if((x+y)%2 == 0):
                Button(root, bg="white", width=11, height=5).grid(row=y, column=x)
            else:
                Button(root, bg="gray", width=11, height=5).grid(row=y, column=x)
    for b in xrange(boardLength):
        Button(root, bg="red", width=11, height=5).grid(row=b, column=temp[b])

def another():
    global solutionList
    temp = random.choice(solutionList)
    for x in xrange(boardLength):
        for y in xrange(boardLength):
            if((x+y)%2 == 0):
                Button(root, bg="white", width=11, height=5).grid(row=y, column=x)
            else:
                Button(root, bg="gray", width=11, height=5).grid(row=y, column=x)
    for b in xrange(boardLength):
        Button(root, bg="red", width=11, height=5).grid(row=b, column=temp[b])

def reset():
    global count, available, placed
    placed = []
    count = 0
    available = [[True for x in xrange(xLength)] for y in xrange(yLength)]
    for x in xrange(boardLength):
        for y in xrange(boardLength):
            if((x+y)%2 == 0):
                Button(root, bg="white", width=11, height=5).grid(row=y, column=x)
            else:
                Button(root, bg="gray", width=11, height=5).grid(row=y, column=x)
    Button(root, text="Place", command=place).grid(row=2, column=xLength, sticky=S)

def check():
    global placed, available, xLength
    while(len(placed)>0):
        temp = placed.pop()
        if(available[temp[1]][temp[0]]):
            for a in xrange(xLength):
                available[a][temp[0]] = False
                available[temp[1]][a] = False
                if(temp[0]+a < xLength and temp[1]+a < xLength):
                    available[temp[1]+a][temp[0]+a] = False
                if(temp[0]-a >= 0 and temp[1]-a >= 0):
                    available[temp[1]-a][temp[0]-a] = False
                if(temp[0]+a < xLength and temp[1]-a >= 0):
                    available[temp[1]-a][temp[0]+a] = False
                if(temp[0]-a >= 0 and temp[1]+a < xLength):
                    available[temp[1]+a][temp[0]-a] = False
        else:
            return Label(root, text="Does not work!", height=2).grid(row=3, column=xLength, sticky = N)
    return Label(root, text="This works!", height=2).grid(row=3, column=xLength, sticky = N)
    
root = Tk()
root.title('8 Queens')
gridList = [[0 for x in xrange(xLength)] for y in xrange(yLength)]
e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=1, column=xLength, sticky=N)
e2.grid(row=2, column=xLength, sticky=N)
Label(root, text="x-value of queen").grid(row=0, column=xLength, sticky=S)
Label(root, text="y-value of queen").grid(row=1, column=xLength, sticky=S)
photo = ImageTk.PhotoImage(Image.open("black-queen-2d-icon.png"))
Label(image=photo).grid(row=6, column=xLength, rowspan=2, padx=10)
Button(root, text="Place", command=place).grid(row=2, column=xLength, sticky=S)
Button(root, text=" Reset", command=reset).grid(row=3, column=xLength, sticky = S)
Button(root, text="Find Solution", command=auto).grid(row=4, column=xLength, sticky=S)
for x in xrange(xLength):
    for y in xrange(yLength):
        if((x+y)%2 == 0):
            gridList[y][x] = Button(root, bg="white", width=11, height=5)
            gridList[y][x].grid(row=y, column=x)
        else:
            gridList[y][x] = Button(root, bg="gray", width=11, height=5)
            gridList[y][x].grid(row=y, column=x)



mainloop()
