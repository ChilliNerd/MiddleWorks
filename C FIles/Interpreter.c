/*

MiddleWorks
Version 1.0

Licensed under the MIT license

Created by matthewgallant on 11/3/16

(c) 2016 Matthew Gallant

*/

#include <unistd.h>
#include <stdio.h>

int main(int argc, char **argv) {

    char *pythonIntrepreter="python"; // resolved using your PATH environment variable
    char *calledPython="/Users/Example/MiddleWorks/Interpreter.py"; // explicit path necessary, not resolved using your PATH environment variable
    char *pythonArgs[]={pythonIntrepreter,calledPython,"/Users/Example/MiddleWorks/Demo.mw", NULL};
    execvp(pythonIntrepreter,pythonArgs);

    // if we get here it misfired
    perror("Python execution");
}