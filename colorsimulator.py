import tkinter 

import random 

colours = ['red','blue','green','pink','black', 
  'yellow','orange','white','purple','brown'] 
score = 0 

timeleft = 60 

def startGame(event): 
	
 if timeleft == 60: 
  
  countdown() 
  
 nextColour() 

def nextColour(): 

 global score 
 global timeleft 

 if timeleft > 0: 

  entry.focus_set() 


  if entry.get().lower() == colours[1].lower(): 
   
   score += 1 

  entry.delete(0, tkinter.END) 
  
  random.shuffle(colours) 
  
  label.config(fg = str(colours[1]), text = str(colours[0])) 

  scoreLabel.config(text = "Score: " + str(score)) 


def countdown(): 

 global timeleft 

 if timeleft > 0: 

  timeleft -= 1 
  
  timeLabel.config(text = "Time left: "
       + str(timeleft)) 
        
  timeLabel.after(1000, countdown) 
 if timeleft==0: 
  stop_button=tkinter.Button(root,text='stop',width=10,height=20,activeforeground='maroon2',command=root.destroy,activebackground='grey',fg='orange') 
  stop_button.pack() 

root = tkinter.Tk() 

root.title("MAGIC COLOR SIMULATOR") 

root.geometry("475x250") 

instructions = tkinter.Label(root,fg='dark orchid', text = "Type the colour"
      "of the words", 
         font = ('Times', 18,'bold')) 
instructions.pack() 

scoreLabel = tkinter.Label(root,fg='maroon3', text = "Press enter to start", 
         font = ('Times', 18,'bold')) 
scoreLabel.pack() 

timeLabel = tkinter.Label(root,fg='dark blue', text = "Time left: " +
   str(timeleft), font = ('Times', 18,'bold')) 
    
timeLabel.pack() 

label = tkinter.Label(root, font = ('Times', 60)) 
label.pack() 

entry = tkinter.Entry(root)
entry.pack() 

root.bind('<Return>', startGame)
 
entry.pack() 

entry.focus_set() 

root.mainloop() 