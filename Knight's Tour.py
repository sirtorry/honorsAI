#Knight's Tour
#Need PIL (Python Image Library), installation file found in project folder

from Tkinter import *
from PIL import Image, ImageTk
import math
import time

yLength = 8
xLength = 8
lastVisitedX = -1
lastVisitedY = -1
curBest = 9
visited = [[False for x in xrange(xLength)] for y in xrange(yLength)]
kMoves = ((1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1))

def reset():
    global lastVisitedX, lastVisitedY, curBest, visited, kMoves
    lastVisitedX = -1
    lastVisitedY = -1
    curBest = 9
    visited = [[False for x in xrange(xLength)] for y in xrange(yLength)]
    kMoves = ((1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1))
    Button(root, text="Start", command=gameStart).grid(row=3, column=xLength, sticky=N)
    for x in xrange(xLength):
                for y in xrange(yLength):
                    if(not visited[y][x]):
                        if((x+y)%2 == 0):
                            Button(root, bg="white", width=11, height=5).grid(row=y, column=x)
                        else:
                            Button(root, bg="gray", width=11, height=5).grid(row=y, column=x)
    

def gameStart():
    visit(int(e1.get()), int(e2.get()))
    Label(root, text="x-value of destination").grid(row=0, column=xLength, sticky=S)
    Label(root, text="y-value of destination").grid(row=1, column=xLength, sticky=S)
    Button(root, text="Move", command=move).grid(row=3, column=xLength, sticky=N)

def legal(x, y):
    if(y >= 0 and x >= 0 and y <yLength and x < xLength):
        if(visited[y][x] == False):
            return True
        
def inRange(x, y):
    global lastVisitedX, lastVisitedY
    if(((math.fabs(lastVisitedX - x) == 2) or (math.fabs(lastVisitedX - x) == 1))
       and ((math.fabs(lastVisitedY - y) == 2) or (math.fabs(lastVisitedY - y) == 1))):
        return True

def move():
    if(inRange(int(e1.get()), int(e2.get())) and legal(int(e1.get()), int(e2.get()))):
        for x in xrange(xLength):
            for y in xrange(yLength):
                if(not visited[y][x]):
                    if((x+y)%2 == 0):
                        Button(root, bg="white", width=11, height=5).grid(row=y, column=x)
                    else:
                        Button(root, bg="gray", width=11, height=5).grid(row=y, column=x)
    if (inRange(int(e1.get()), int(e2.get()))):
        visit(int(e1.get()), int(e2.get()))

def check(x, y):
    a = 0
    count = 0
    while(a < 8):
        tempX = x + kMoves[a][1]
        tempY = y + kMoves[a][0]
        if(legal(tempX, tempY)):
            count += 1
        a += 1
    return count

def gameSolve():
    global lastVisitedX, lastVisitedY, curBest
    if curBest is not 0:
        curBest = 9
        b = 0
        for x in xrange(xLength):
                for y in xrange(yLength):
                    if(not visited[y][x]):
                        if((x+y)%2 == 0):
                            Button(root, bg="white", width=11, height=5).grid(row=y, column=x)
                        else:
                            Button(root, bg="gray", width=11, height=5).grid(row=y, column=x)
        while(b < 8):
            tempX = lastVisitedX + kMoves[b][1]
            tempY = lastVisitedY + kMoves[b][0]
            temp = check(tempX,tempY)
            if legal(tempX,tempY) and temp < curBest:
                curBest = temp
                nextX = tempX
                nextY = tempY
            b += 1
        visit(nextX,nextY)
        root.update()
        time.sleep(0.5)
        gameSolve()
   
def visit(x, y):
    global lastVisitedX, lastVisitedY
    if(legal(x,y)):
        visited[y][x] = True
        if lastVisitedX is not -1:
            Button(root, bg="red", width=11, height=5).grid(row=lastVisitedY, column=lastVisitedX)
        lastVisitedX = x
        lastVisitedY = y
        photo = ImageTk.PhotoImage(Image.open("12205467171891699302portablejim_Chess_tile_-_Knight_2.svg.med.png"))
        if((x+y)%2 == 0):
            Button(root, bg="white", text="X", width=11, height=5).grid(row=y, column=x)
        else:
            Button(root, bg="gray", text="X", width=11, height=5).grid(row=y, column=x)
        b = 0
        while(b < 8):
            tempX = x + kMoves[b][1]
            tempY = y + kMoves[b][0]
            if(legal(tempX, tempY)):
                if((tempX+tempY)%2 == 0):
                    Button(root, text=str(check(tempX,tempY)), bg="white", fg="black", width=11, height=5).grid(row=tempY, column=tempX)
                else:
                    Button(root, text=str(check(tempX,tempY)), bg="gray", fg="white", width=11, height=5).grid(row=tempY, column=tempX)
            b += 1
        
root = Tk()
root.title('Knight\'s Tour')
gridList = [[0 for x in xrange(xLength)] for y in xrange(yLength)]
e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=1, column=xLength, sticky=N)
e2.grid(row=2, column=xLength, sticky=N)
Label(root, text="x-value of starting").grid(row=0, column=xLength, sticky=S)
Label(root, text="y-value of starting").grid(row=1, column=xLength, sticky=S)
photo = ImageTk.PhotoImage(Image.open("12205467171891699302portablejim_Chess_tile_-_Knight_2.svg.med.png"))
l1 = Label(image=photo)
l1.grid(row=6, column=xLength, rowspan=2, padx=5)
Button(root, text="Start", command=gameStart).grid(row=3, column=xLength, sticky=N)
Button(root, text="Finish Tour", command=gameSolve).grid(row=5, column=xLength, sticky=N)
Button(root, text="Reset", command=reset).grid(row=4, column=xLength, sticky=N)
for x in xrange(xLength):
    for y in xrange(yLength):
        if((x+y)%2 == 0):
            gridList[y][x] = Button(root, bg="white", width=11, height=5)
            gridList[y][x].grid(row=y, column=x)
        else:
            gridList[y][x] = Button(root, bg="gray", width=11, height=5)
            gridList[y][x].grid(row=y, column=x)



mainloop()
