### memory puzzel game in python 

# importing modules 

from tkinter import *
from tkinter import ttk
import random
from venv import create    
 
gameInterfacce = Tk()
gameInterfacce.geometry("400x550")
# giving the title to the game interface 
gameInterfacce.title("Memory Puzzle Game In Python (GFG)")

## ttk Nodebook basiclly manage the windows in the GUI
tabs = ttk.Notebook(gameInterfacce)

## level1 is the first tab of the GUI
level1 = ttk.Frame(tabs)

### making the hidden stucture into the  box
def hiddenStructure(a,b,c):
    global base 
    if a=='A':
        createStructure = base.create_rectangle(100*b+20,c*100+20,100*b+100-20,100*c+100-20,fill='red') 
    elif a=='B':
        createStructure = base.create_rectangle(100*b+20,c*100+20,100*b+100-20,100*c+100-20,fill='blue')
    elif a=='C':
        createStructure = base.create_oval(100*b+20,c*100+20,100*b+100-20,100*c+100-20,fill='red')
    elif a=='D':
        createStructure = base.create_rectangle(100*b+20,c*100+20,100*b+100-20,100*c+100-20,fill='yellow')
    elif a=='E':
        createStructure = base.create_polygon(100*b+50,c*100+20,100*b+20,100*c+100-20,100*b+100-20,100*c+100-20,fill='red')
    elif a=='F':
        createStructure = base.create_oval(100*b+20,c*100+20,100*b+100-20,100*c+100-20,fill='yellow')
    elif a=='G':
        createStructure = base.create_oval(100*b+20,c*100+20,100*b+100-20,100*c+100-20,fill='blue')  
    elif a=='H':
        createStructure = base.create_polygon(100*b+50,c*100+20,100*b+20,100*c+100-20,100*b+100-20,100*c+100-20,fill='green')

## will show the hidden figure if they get matched otherwise keep them disappear 
def hidddenFigure(val) :
    global base,ans,box,shift,view 
    i = val.x//100
    j = val.y//100
    if box[i][j] != "." : 
        return 
    shift+=1
    if view[0]>4:
        view[0]=i
        view[1]=j
        box[i][j]=ans[i][j]
        boardboard()
    else:
        box [i][j]=ans[i][j]
        boardboard()
        if ans[i][j]==box [view[0]][view[1]] :
            print("Matched")
            view=[100,100]
            boardboard()
            return
        else :
            box[view[0]][view[1]]='.'
            boardboard()
            view=[i,j]
            return
        
### will make the base structure 
def boardboard() :
    global base,ans,box,shift
    count=0
    for i in range(4):
        for j in range(4):
            rec=base.create_rectangle(100*i,j*100,100*i+100,100*j+100,fill="white")
            if(box[i][j]!='.'):
                hiddenStructure(box[i][j],i,j)
                count+=1
    if count==16:
        base.create_text(200,450,text="Total moves : "+str(shift),font=('arial',20))

### ading the structure boarding 
base =Canvas(level1,width=500,height=500)
base.pack()

ans = list('AABBCCDDEEFFGGHH')
random.shuffle(ans)
ans = [ans[:4],
       ans[4:8],
       ans[8:12],
       ans[12:]]
### binding the hiddenFigure function 
base.bind("<Button-1>", hidddenFigure)
 
shift=IntVar()
shift=0
 
view=[100,100]
 
box = [list('.'*4) for num in range(4)]
boardboard()
tabs.add(level1, text ='Easy') 
tabs.pack(expand = 1, fill ="both") 

mainloop()

                        ### contribyted by amanansari003