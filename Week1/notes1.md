# Week 1 C

C. Source Code. Machine Code. Compiler. Correctness, Design, Style. Visual Studio Code. Syntax Highlighting. Escape Sequences. Header Files. Libraries. Manual Pages. Types. Conditionals. Variables. Loops. Linux. Graphical User Interface (GUI). Command-Line Interface (CLI). Constants. Comments. Pseudocode. Operators. Integer Overflow. Floating-Point Imprecision.

[![Harvard CS 50 Lecture One](http://img.youtube.com/vi/ywg7cW0Txs4/0.jpg)](http://www.youtube.com/watch?v=ywg7cW0Txs4)
- https://www.youtube.com/live/ywg7cW0Txs4

___

## Lecture 1

- Welcome!
- Hello World
- Functions
- Variables
- Conditionals
- Loops
- Linux and the Command Line
- Mario
- Comments
- Abstraction
- Operators and Types
- Summing Up


___

## Welcome!

- In our previous session, we learned about Scratch, a visual programming language.
- Indeed, all the essential programming concepts presented in Scratch will be utilized as you learn how to program any programming language.
- Recall that machines only understand binary. Where humans write source code, a list of instructions for the computer that is human readable, machines only understand what we can now call machine code. This machine code is a pattern of ones and zeros that produces a desired effect.
- It turns out that we can convert source code into machine code using a very special piece of software called a compiler. Today, we will be introducing you to a compiler that will allow you to convert source code in the programming language C into machine code.
- Today, in addition to learning about how to code, you will be learning about how to write good code.
- Code can be evaluated upon three axes. 
1. First, correctness refers to “does the code run as intended?” 
2. Second, design refers to “how well is the code designed?” 
3. Finally, style refers to “how aesthetically pleasing and consistent is the code?”


## Hello World

- The compiler that is utilized for this course is Visual Studio Code, affectionately referred to as, which can be accessed via that same url, or simply as *VS Code*.
- One of the most important reasons we utilize VS Code is that it has all the software required for the course already pre-loaded on it. This course and the instructions herein were designed with VS Code in mind. Best always to utilize VS Code for assignments in this course.
- You can open VS Code at cs50.dev.
- The compiler can be divided into a number of regions:
- ![image](https://github.com/danielmassita/Harvard-CS50/assets/111195175/d901c1f6-9e5e-40ad-8526-f12c1f292484)
- Notice that there is a file explorer on the left side where you can find your files. Further, notice that there is a region in the middle called a text editor where you can edit your program. Finally, there is a command line interface, known as a CLI, command line, or terminal window where we can send commands to the computer in the cloud.
- We can build your first program in C by typing code hello.c into the terminal window. Notice that we deliberately lowercased the entire filename and included the .c extension. Then, in the text editor that appears, write code as follows:
```c
// A program that says hello to the world 
#include <stdio.h>

int main(void)
{
    printf("hello, world\n");
}
```
- Note that every single character above serves a purpose. If you type it incorrectly, the program will not run.
- Clicking back in the terminal window, you can compile your code by executing make hello. Notice that we are omitting .c. make is a compiler that will look for our hello.c file and turn it into a program called hello. If executing this command results in no errors, you can proceed. If not, double-check your code to ensure it matches the above.
- Now, type ./hello and your program will execute saying hello, world.
- Now, open the file explorer on the left. You will notice that there is now both a file called hello.c and another file called hello. hello.c is able to be read by the compiler: It’s where your code is stored. hello is an executable file that you can run, but cannot be read by the compiler.
- Let’s look at our code more carefully:
```c
#include <stdio.h>

int main(void)
{
    printf("hello, world\n");
}
```
- Notice that our code is highlighted using syntax highlighting.



