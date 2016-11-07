![alt text](https://github.com/ChilliNerd/MiddleWorks/blob/master/Img/icon128.png "MiddleWorks Logo")

# MiddleWorks
MiddleWorks is an interpreter between MiddleWorks Scripting and Python Tkinter. MiddleWorks is written in pure Python.

---

### About MiddleWorks
MiddleWorks was created to make creating Tkinter applications easier. Overall, as long as you are not doing anything too specific, it should work.
MiddleWorks does not interpret every Tkinter command. There are currently 22 commands available. There is documentation below for the commands.

---

### License
MiddleWorks is available under the MIT License, see [LICENSE](../blob/master/LICENSE).

---
### Terminology and Information
**MiddleWorks** - The interpreter between MiddleWorks Scripting and Python Tkinter.

**MiddleWorks Scripting** - The language which MiddleWorks interprets.

**MiddleWorks Shell** - The shell that allows you to build a featureless window. I never finished developing it as it is pretty much useless. If someone builds a useful version I wouldn't mind checking it out.

**C Files** - Simple C bindings for the python script. Not necessary, but nice for quick prototyping.

---

### Commands
**WINDOWTITLE** - Sets window title.
```
WINDOWTITLE MiddleWorks Demo
```

**WINDOWSIZE** - Sets window size.
```
WINDOWSIZE 800x500
```

**WINDOWLOC** - Sets window location.
```
WINDOWLOC 150+150
```

**WINDOWCOLOR** - Sets the color of the window canvas.
```
WINDOWCOLOR white
```

**DISBALEWINDOWRESIZE** - Disables the ability for the user to resize the window.
```
DISABLEWINDOWRESIZE
```

**DARKTHEME** - Enables a dark theme for all elements in the application.
```
DARKTHEME
```

**OSXTITLE** - If on OSX, changes the application title in the menubar from Python to your custon title.
```
OSXTITLE MiddleWorks Demo
```

**ABOUTTITLE** - Sets title of about window. Access the about window in Help > About.
```
ABOUTTITLE About MiddleWorks
```

**ABOUTTEXT** - Sets text for about window.
```
ABOUTTEXT MiddleWorks v1.0: A simple interpreter between MiddleWorks Scripting and Python Tkinter.
```

**LABELXL** - Extra large label.
```
LABELXL XL Label
```

**LABELLARGE** - Large label.
```
LABELLARGE Large Label
```

**LABELMEDIUM** - Medium label.
```
LABELMEDIUM Medium Label
```

**LABELREGULAR** - Regular label.
```
LABELREGULAR Regular Label
```

**LABELSMALL** - Small label.
```
LABELSMALL Small Label
```

**IMAGE** - Displays an image that is either a Tkinter compatible GIF or PGM.
```
IMAGE /Users/Example/Desktop/MiddleWorksProject/image.gif
```
or
```
IMAGE /Users/Example/Desktop/MiddleWorksProject/image.pgm
```

**FIELD** - Displays a text field and default text if available.
```
FIELD
```
or
```
FIELD Default Text
```

**DIALOGTITLE** - Title of a dialog window.
```
DIALOGTITLE Dialog
```

**DIALOGTEXT** - Text in a dialog window.
```
DIALOGTEXT This is a dialog!
```

**BUTTONDIALOGINFO** - Makes a button that displays an info dialog based on your DIALOGTITLE and your DIALOGTEXT.
```
BUTTONDIALOGINFO Info Button
```

**BUTTONDIALOGERROR** - Makes a button that displays an error dialog based on your DIALOGTITLE and your DIALOGTEXT.
```
BUTTONDIALOGERROR Error Button
```

**BUTTONDIALOGWARNING** - Makes a button that displays a warning dialog based on your DIALOGTITLE and your DIALOGTEXT.
```
BUTTONDIALOGWARNING Warning Button
```

**START** - Starts the program.
```
START
```
