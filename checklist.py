from tkinter import *
from tkinter import messagebox

root = Tk()

#root properties
root.title("My Check List App")
root.geometry("400x400")
root.resizable(0,0)
root.iconbitmap("checklistlogo.ico")


#setting up general fonts and colours
myFont = ("Times New Roman",12)
rootColour = "#e66c2c"
buttonColour = "#40826d"
root.config(bg=rootColour)
#function defination
#
def addItem():
    if listEntry.get() == "":
        #message popup
        messagebox.showinfo("Illegal Entry in the list","Cannot Enter Blank Item in List")
    else:
        listBox.insert(END,listEntry.get())
        listEntry.delete(0,END)
#function to remove anchored(selected) item
def removeItem():
    listBox.delete(ANCHOR)
#function to clear list
def clearList():
    listBox.delete(0,END)
#function to save list contents into AN external txt file.
def saveList():
    #we will open a file (in wirte mode) and wirte required conntents in it
    with open("checklist.txt","w") as f:
        #print(f)
        listTuple = listBox.get(0,END)

        for items in listTuple:
            f.write(items + "\n")
#function to re call stored element in text file
def openList():
    try:
        with open("checklist.txt","r") as f:
            for line in f:
                listBox.insert(END,line)
    except:
        pass
#create layouts for app
#create frames
inputFrame = Frame(root,bg=rootColour)
outputFrame = Frame(root,bg=rootColour)
buttonFrame = Frame(root,bg=rootColour)
inputFrame.pack()
outputFrame.pack()
buttonFrame.pack()

#creat layout of elements in input frame - entry widget , add item button
listEntry = Entry(inputFrame,width=35,borderwidth=3,font=myFont)
listAddButton = Button(inputFrame,text="Add Item",borderwidth=2,font=myFont,bg=buttonColour,command=addItem)
listEntry.grid(row=0,column=0,padx=5,pady=5)
listAddButton.grid(row=0,column=1,padx=5,pady=5)

#creat layout of elements- in output frame - list box ,scroller
scrollBar= Scrollbar(outputFrame)
listBox = Listbox(outputFrame,height=15,width=45,borderwidth=3,font=myFont,yscrollcommand=scrollBar.set)
scrollBar.config(command=listBox.yview)
listBox.grid(row=0,column=0)
scrollBar.grid(row=0,column=1,sticky="NS")




#creat layout of elements in button frame - remove item,clear list,save ,quit
listRemoveButton = Button(buttonFrame,text="Remove Item",borderwidth=2,font=myFont,bg=buttonColour,command=removeItem)
listClearButton = Button(buttonFrame,text="Clear List",borderwidth=2,font=myFont,bg=buttonColour,command=clearList)
saveButton = Button(buttonFrame,text="Save",borderwidth=2,font=myFont,bg=buttonColour,command=saveList)
quitButton = Button(buttonFrame,text="Quit",borderwidth=2,font=myFont,bg=buttonColour,command=root.destroy)
listRemoveButton.grid(row=0,column=0,padx=2,pady=10)
listClearButton.grid(row=0,column=1,padx=2,pady=10,ipadx=7)
saveButton.grid(row=0,column=2,padx=2,pady=10,ipadx=20)
quitButton.grid(row=0,column=3,padx=2,pady=10,ipadx=20)









openList()
#main loop
root.mainloop()
