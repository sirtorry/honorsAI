from Tkinter import *

def convert(t):
	f = open(t, "r").read()
	lower = f.lower()
	return f

def record(t):
	rec = dict()
	for a in t:
		if a not in rec:
			rec[a] = 1
		else:
			rec[a] += 1
	return rec

def total(s):
        a = "abcdefghijklmnopqrstuvwxyz"
        occur = {letter: 0 for letter in a}
        tot = 0
        for letter in s:
            if letter in occur:
                tot += 1
        return tot

def frequency(d, l, t):
        return (d.get(l)/(t*1.0))*100

def totaldist(x, y, z):
#x is being checked, y is standard, z is current total
        dist = 0.0
        z += abs(x - y)
        return z

def check(loc):
        str = convert(loc)
        rec = record(str)
        tot = total(str)
        english = {'a' : 8.127, 'b' : 1.492, 'c' : 2.782, 'd' : 4.253, 'e' : 12.702, 'f' : 2.228, 'g' : 2.015, 'h'
            : 6.094, 'i' : 6.966, 'j' : 0.153, 'k' : 0.747, 'l' : 4.025, 'm' : 2.406, 'n' : 6.749, 'o' : 7.507, 'p' : 1.929, 'q' :
           0.095, 'r' : 5.987, 's' : 6.327, 't' : 9.056, 'u' : 2.758, 'v' : 1.037, 'w' : 2.365, 'x' : 0.150, 'y' : 1.974, 'z' :
           0.074}
        french = {'a' : 8.000, 'b' : 0.901, 'c' : 3.260, 'd' : 3.669, 'e' : 14.715, 'f' : 1.066, 'g' : 0.866, 'h' :
           0.737, 'i' : 7.529, 'j' : 0.545, 'k' : 0.049, 'l' : 5.456, 'm' : 2.968, 'n' : 7.095, 'o' : 5.378, 'p' : 3.021, 'q' :
           1.362, 'r' : 6.553, 's' : 7.948, 't' : 7.244, 'u' : 6.311, 'v' : 1.628, 'w' : 0.114, 'x' : 0.387, 'y' : 0.308, 'z' :
           0.074}
        german = {'a' : 6.51, 'b' : 1.89, 'c' : 3.06, 'd' : 5.08, 'e' : 17.40, 'f' : 1.66, 'g' : 3.01, 'h' :
           4.76, 'i' : 7.55, 'j' : 0.27, 'k' : 1.21, 'l' : 3.44, 'm' : 2.53, 'n' : 9.78, 'o' : 2.51, 'p' : 0.79, 'q' :
           0.02, 'r' : 7.00, 's' : 7.217, 't' : 6.15, 'u' : 4.35, 'v' : 0.67, 'w' : 1.89, 'x' : 0.03, 'y' : 0.04, 'z' :
           1.13}
        spanish = {'a' : 12.53, 'b' : 1.42, 'c' : 4.68, 'd' : 5.86, 'e' : 13.68, 'f' : 0.69, 'g' : 1.01, 'h' :
           0.7, 'i' : 6.25, 'j' : 0.44, 'k' : 0.01, 'l' : 4.97, 'm' : 3.15, 'n' : 6.71, 'o' : 8.68, 'p' : 2.51, 'q' :
           0.88, 'r' : 6.87, 's' : 7.98, 't' : 4.63, 'u' : 3.93, 'v' : 0.90, 'w' : 0.02, 'x' : 0.22, 'y' : 0.90, 'z' :
           0.52}
        portuguese = {'a' : 14.63, 'b' : 1.04, 'c' : 3.88, 'd' : 4.99, 'e' : 12.57, 'f' : 1.02, 'g' : 1.3, 'h' :
           1.28, 'i' : 6.18, 'j' : 0.40, 'k' : 0.02, 'l' : 2.78, 'm' : 4.74, 'n' : 5.05, 'o' : 10.73, 'p' : 2.52, 'q' :
           1.2, 'r' : 6.53, 's' : 7.81, 't' : 4.74, 'u' : 4.63, 'v' : 1.67, 'w' : 0.01, 'x' : 0.21, 'y' : 0.01, 'z' :
           0.47}
        likeEng = 0
        likeFre = 0
        likeGer = 0
        likeSpa = 0
        likePor = 0
        likeEsp = 0
        a = "abcdefghijklmnopqrstuvwxyz"
        x = 0
        while(x < 26):
            y = a[x:x+1]
            if y in str:
                cur = frequency(rec, y, tot)
                likeEng = totaldist(cur, english.get(y), likeEng)
                likeFre = totaldist(cur, french.get(y), likeFre)
                likeGer = totaldist(cur, german.get(y), likeGer)
                likeSpa = totaldist(cur, spanish.get(y), likeSpa)
                likePor = totaldist(cur, portuguese.get(y), likePor)
            x += 1
        if(likeEng <= likeFre and likeEng <= likeGer and likeEng <= likeSpa and likeEng <= likePor):
            return "English"
        elif(likeFre <= likeEng and likeFre <= likeGer and likeFre <= likeSpa and likeFre <= likePor):
            return "French"
        elif(likeGer <= likeFre and likeGer <= likeEng and likeGer <= likeSpa and likeGer <= likePor):
            return "German"
        elif(likeSpa <= likeFre and likeSpa <= likeGer and likeSpa <= likeEng and likeSpa <= likePor):
            return "Spanish"
        else:
            return "Portuguese"
def callback():
        direct = e.get()
        print direct
        n = Label(graphic, bg="blue", width=100, text=check(direct))
        n.pack()

graphic = Tk()
graphic.geometry("400x400")
graphic.title("Language Guesser")
graphic.configure(background="white")
d = Label(graphic, width=100, text='Enter directory:')
d.pack()
e = Entry(graphic, width=100, fg="black",bg="white",text='Enter directory...')
e.pack()
b = Button(graphic, width=100, text='Guess', command = callback)
b.pack()
l = Label(graphic, width=100, text='Guessed language will show up below...')
l.pack()
mainloop()
