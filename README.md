WELCOME TO THE TURING MACHINE!
=====================================================================

------

A Turing machine is a mathematical model of computation describing an abstract machine that manipulates symbols on a strip of tape according to a table of rules. Despite the model's simplicity, it is capable of implementing any computer algorithm.

The machine operates on an infinite memory tape divided into discrete cells, each of which can hold a single symbol drawn from a finite set of symbols called the alphabet of the machine. It has a "head" that, at any point in the machine's operation, is positioned over one of these cells, and a "state" selected from a finite set of states.

At each step of its operation, the head reads the symbol in its cell. Then, based on the symbol and the machine's own present state, the machine writes a symbol into the same cell, and moves the head one step to the left or the right, or halts the computation. The choice of which replacement symbol to write and which direction to move is based on a finite table that specifies what to do for each combination of the current state and the symbol that is read. 

Here you can see the machine in work and add comments and suggestions:

https://colab.research.google.com/drive/1_-8lqQaUkW_NdKAfO6ogdZR4V8PJdNEe?usp=sharing

------

When machine core file is run, the '$' symbol is waiting for you to
write command. Commands can be written in one line, or splited each
space to a new line.

```
    readfile file_path - read script file and run it

    help - print help menu

    execute machine_name - machine_name is optional, if no name 
                           specified, simply runs first machine
    q - quit
```
------

Rules are very simple. Machine can execute a few simple commands:

```
    l - Move head to the left.
    r - Move head to the right.
    n - No move.
    w_- Write value of _ to the tape.
    / - Write an subcommand.
    q - Quit the machine.
```

---------------------------------------------------------------------

Subcommands are kind of useful when you are creating something besides machine that can move 3 cells to right and write there 'Hello World!'.

Subcommands are:


    help - print help
    
    states - print table of all states in machine
        note: 0 state is exit state, don't try to overwrite it
    
    save - save machine's tape and table of states to memory
        note: there can be only 1 saved machine
    
    load - loads saved machine
    
    reset - reset to empty tape and empties table of states
    
    new - create new state, for details see above
    
    edit - edit states commands, index of state must be specified
    
    run - run specified state. If no state is specified, simply
          runs first state in table
    
    write - THIS IS NOT turing machine command, it is just used for
            pre-writing on tape something, for further using

States are saved in this format - RWMS, where each letter stands for:
    R - if head reads value of R in current cell
    W - then write W to current cell
    M - move head on the tape (left, right, no-move)
    S - change state to state with index S (For creating loops, state can be changed to current)

As an example of machine usage, let's write a simple algorithm, for calculating sum of 2 numbers.

Λ means the cell is empty. Let's write two numbers to tape, and '+' sign between them: 

7+4

This means we must write '+' sign, 8 ones on one side of it, and 5 ones on the other side. We write n+1 ones, because 1 means 0.

    ΛΛΛΛΛΛΛΛΛΛΛ11111111+11111ΛΛΛΛΛΛΛΛΛΛΛ
               ᛏ

There is an agreement, to start an finish run of the machine at the first left non-empty cell. So, let's start creating our states. For cell creation we must use subcommands, so we must type '/', and type command to the next line.

    Machine$ /
    new 11r1 +1r1 ΛΛn2

This command creates a new state under the first number, and applies 3 conditions to it. 11r1 means, that if machine sees an 1 on the  tape, it must leave it unchanged, by simply rewriting it to 1, than move one position to the left and go to state 1, which means stay in a loop. We need to add a few more states in the same way, and when done, use this command to see states table:

    Machine$ /
    states

The output should be:

```
   0 p
   1 ['11r1', '+1r1', 'ΛΛn2']
   2 ['ΛΛl2', '1Λl3']
   3 ['11l3', 'ΛΛr0']
```

After creating states, you may run the machine, and the result
should be:

```
    ΛΛΛΛΛΛΛΛΛΛΛ1111111111111ΛΛΛΛΛΛΛΛΛΛΛΛ
               ᛏ
```

TODO list
 > Make program for reading files in RWMS format. [Still in progress :D]
 > Minor changes in code, to match PEP8.
 > Gyodel numeration implementation.
That's all. Thank you for using our Turing Machine.                

© Garik MKrtchyan 2022

Contacts:
    mail: garikmkrtychan277353@gmail.com
    tg: https://t.me/V1king_V
    

