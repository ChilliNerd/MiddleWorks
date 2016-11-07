#
# MiddleWorks Shell
# Version 1.0
#
# Licensed under the MIT license
#
# Created by matthewgallant on 11/3/16
#
# (c) 2016 Matthew Gallant
#

import sys
from Tkinter import Tk, Label, Button

print("\nMiddleWorks Shell\nAn interactive shell for MiddleWorks\nVersion 1.0\nLicensed under the MIT license\n(c) 2016 Matthew Gallant\n")

loop_num = 0

while(loop_num == 0):
    x1 = raw_input("> ")

    title = "Untitled MiddleWorks Application"

    if x1.startswith("title"):
        print("\nSet Window Title:")
        title_var = raw_input("> ")
        print("\nWindow Title Set To: " + title_var + "\n")

    if x1.startswith("size"):
        print("\nX Value:")
        size_var_x = raw_input("> ")
        print("Y Value")
        size_var_y = raw_input("> ")
        print("\nWindow Size Set To: " + size_var_x + "x" + size_var_y + "\n")

    if x1.startswith("loc"):
        print("\nX Value:")
        loc_var_x = raw_input("> ")
        print("Y Value")
        loc_var_y = raw_input("> ")
        print("\nWindow Location Set To: " + loc_var_x + "+" + loc_var_y + "\n")

    class WindowWorks:
        def __init__(self, master):
            self.master = master
            master.title(title_var)

    if x1.startswith("windowinit"):
        root = Tk()
        root.geometry(size_var_x + "x" + size_var_y + "+" + loc_var_x + "+" + loc_var_y)
        my_gui = WindowWorks(root)
        root.mainloop()
        print("\n")

    if x1.startswith("exit"):
        exit()