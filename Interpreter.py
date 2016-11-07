#
# MiddleWorks Scripting Interpreter
# Version 1.0
#
# Licensed under the MIT license
#
# Created by matthewgallant on 11/3/16
#
# (c) 2016 Matthew Gallant
#

# Imports
from Tkinter import *
import tkMessageBox
from sys import argv
from sys import platform

# Initialize Tkinter
root = Tk()

# Handle File Arguments
script, filename = argv
txt = open(filename)

# Read Text File
print "Running: %r:" % filename
text = txt.read()

# Variables
windowtitle_var = "MiddleWorks Project"
windowsize_var = "800x600"
windowloc_var = "+150+150"
label_var = "Default Label Text"
button_var = "Default Button"
dialogname_var = "Dialog"
dialog_var = "Default Dialog Text"
abouttitle_var = "About " + windowtitle_var
abouttext_var = "Powered by MiddleWorks"
theme_var = "white"
texttheme_var = "black"

# Function Definitions
def about():
    tkMessageBox.showinfo(
        abouttitle_var,
        abouttext_var
    )

def labelsmall_def():
    label0 = Label(root, text=labelsmall_var, font=("Helvetica", 10), bg=theme_var, fg=texttheme_var)
    label0.pack()

def labelregular_def():
    label1 = Label(root, text=labelregular_var, font=("Helvetica", 12), bg=theme_var, fg=texttheme_var)
    label1.pack()

def labelmedium_def():
    label2 = Label(root, text=labelmedium_var, font=("Helvetica", 18), bg=theme_var, fg=texttheme_var)
    label2.pack()

def labellarge_def():
    label3 = Label(root, text=labellarge_var, font=("Helvetica", 36), bg=theme_var, fg=texttheme_var)
    label3.pack()

def labelxl_def():
    label4 = Label(root, text=labelxl_var, font=("Helvetica", 72), bg=theme_var, fg=texttheme_var)
    label4.pack()

def field_def():
    entry1 = Entry(root, highlightbackground=theme_var)
    entry1.insert(0, field_var)
    entry1.pack()

def dialoginfo_def():
    tkMessageBox.showinfo(
        dialogname_var,
        dialog_var
    )

def dialogerror_def():
    tkMessageBox.showerror(
        dialogname_var,
        dialog_var
    )

def dialogwarning_def():
    tkMessageBox.showwarning(
        dialogname_var,
        dialog_var
    )

def buttondialoginfo_def():
    button0 = Button(root, text=button_var, command=dialoginfo_def, highlightbackground=theme_var)
    button0.pack()

def buttondialogerror_def():
    button1 = Button(root, text=button_var, command=dialogerror_def, highlightbackground=theme_var)
    button1.pack()

def buttondialogwarning_def():
    button3 = Button(root, text=button_var, command=dialogwarning_def, highlightbackground=theme_var)
    button3.pack()

def osxtitle_def():
    if platform == 'darwin':
        from Foundation import NSBundle
        bundle = NSBundle.mainBundle()
        if bundle:
            info = bundle.localizedInfoDictionary() or bundle.infoDictionary()
            if info and info['CFBundleName'] == 'Python':
                info['CFBundleName'] = osxtitle_var

def image_def():
    photo = PhotoImage(file=image_var)
    label5 = Label(image=photo)
    label5.pack()

# Search Code For Commands
for line in text.splitlines():
    if "WINDOWTITLE" in line:
        windowtitle_var = line[12:]
    if "WINDOWSIZE" in line:
        windowsize_var = line[11:]
    if "WINDOWLOC" in line:
        windowloc_var = "+" + line[10:]
    if "LABELSMALL" in line:
        labelsmall_var = line[11:]
        labelsmall_def()
    if "LABELREGULAR" in line:
        labelregular_var = line[13:]
        labelregular_def()
    if "LABELMEDIUM" in line:
        labelmedium_var = line[12:]
        labelmedium_def()
    if "LABELLARGE" in line:
        labellarge_var = line[11:]
        labellarge_def()
    if "LABELXL" in line:
        labelxl_var = line[8:]
        labelxl_def()
    if "FIELD" in line:
        field_var = line[6:]
        field_def()
    if "DIALOGTITLE" in line:
        dialogname_var = line[12:]
    if "DIALOGTEXT" in line:
        dialog_var = line[11:]
    if "BUTTONDIALOGINFO" in line:
        button_var = line[17:]
        buttondialoginfo_def()
    if "BUTTONDIALOGERROR" in line:
        button_var = line[18:]
        buttondialogerror_def()
    if "BUTTONDIALOGWARNING" in line:
        button_var = line[20:]
        buttondialogwarning_def()
    if "OSXTITLE" in line:
        osxtitle_var = line[9:]
        osxtitle_def()
    if "ABOUTTITLE" in line:
        abouttitle_var = line[11:]
    if "ABOUTTEXT" in line:
        abouttext_var = line[10:]
    if "WINDOWCOLOR" in line:
        theme_var = line[12:]
    if "DARKTHEME" in line:
        theme_var = "grey12"
        texttheme_var = "white"
    if "DISABLEWINDOWRESIZE" in line:
        root.resizable(0,0)
    if "IMAGE" in line:
        image_var = line[6:]
        image_def()
        

# MenuBar
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)
        
# Set Tkinter Properties
root.geometry(windowsize_var + windowloc_var)
root.title(windowtitle_var)
root.config(menu=menubar, background=theme_var)

# Initialize Window
if "START" in text:
    root.mainloop()
    print("\n")