HELP = \
"""
DEAR USER, WELCOME TO THE TURING MACHINE!
=====================================================================

A Turing machine is a mathematical model of computation describing an
abstract machine that manipulates symbols on a strip of tape according
to a table of rules. Despite the model's simplicity, it is capable of
implementing any computer algorithm.

The machine operates on an infinite memory tape divided into discrete
cells, each of which can hold a single symbol drawn from a finite set
of symbols called the alphabet of the machine. It has a "head" that,
at any point in the machine's operation, is positioned over one of
these cells, and a "state" selected from a finite set of states.

At each step of its operation, the head reads the symbol in its cell.
Then, based on the symbol and the machine's own present state, the
machine writes a symbol into the same cell, and moves the head one
step to the left or the right, or halts the computation. The choice
of which replacement symbol to write and which direction to move is
based on a finite table that specifies what to do for each combination
of the current state and the symbol that is read. 

=====================================================================

When machine core file is run, the '$' symbol is waiting for you to
write command. Commands can be written in one line, or splited each
space to a new line.

    readfile file_path - read script file and run it

    help - print help menu

    execute machine_name - machine_name is optional, if no name 
                           specified, simply runs first machine

=====================================================================
Rules are very simple. Machine can execute a few simple commands:
    l - Move head to the left.
    r - Move head to the right.
    n - No move.
    w_- Write value of _ to the tape.
    / - Write an subcommand.
    q - Quit the machine.

---------------------------------------------------------------------

Subcommands are kind of useful when you are creating something besides
machine that can move 3 cells to right and write there 'Hello World!'.

Subcommands are:

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

=====================================================================

States are saved in this format - RWMS, where each letter stands for:
    R - if head reads value of R in current cell
    W - then write W to current cell
    M - move head on the tape (left, right, no-move)
    S - change state to state with index S (For creating loops, state
        can be changed to current)
--------------------------------------------------------------------

As an example of machine usage, let's write a simple algorithm, for
calculating sum of 2 numbers.

Λ means the cell is empty. Let's write two numbers to tape, and '+'
sign between them: 7+4
This means we must write '+' sign, 8 ones on one side of it, and 5
ones on the other side. We write n+1 ones, because 1 means 0.

    ΛΛΛΛΛΛΛΛΛΛΛ11111111+11111ΛΛΛΛΛΛΛΛΛΛΛ
               ᛏ

There is an agreement, to start an finish run of the machine at the
first left non-empty cell. So, let's start creating our states.
For cell creation we must use subcommands, so we must type '/', and
type command to the next line.

    Machine$ /
    new 11r1 +1r1 ΛΛn2

This command creates a new state under the first number, and applies
3 conditions to it. 11r1 means, that if machine sees an 1 on the 
tape, it must leave it unchanged, by simply rewriting it to 1, than
move one position to the left and go to state 1, which means stay in
a loop. We need to add a few more states in the same way, and when
done, use this command to see states table:

    Machine$ /
    states

The output should be:
    0 p
    1 ['11r1', '+1r1', 'ΛΛn2']
    2 ['ΛΛl2', '1Λl3']
    3 ['11l3', 'ΛΛr0']

After creating states, you may run the machine, and the result
should be:
    ΛΛΛΛΛΛΛΛΛΛΛ1111111111111ΛΛΛΛΛΛΛΛΛΛΛΛ
               ᛏ

====================================================================
That's all. Thank you for using our Turing Machine.
                                             
                                             © Garik MKrtchyan 2022

"""


OPENED_MACHINES = {} # {'machine name': machine_object, ...

class Machine(object):
    def __init__(self) -> None:
        self.__lenght__ = 10 
        self.tape = ['Λ' for i in range(self.__lenght__ + 1)]
        self.position = 0
        self.states = ['p']
        
    def R(self) -> None:
        """Move to right."""
        if self.__lenght__ <= self.position:
            for i in range(self.__lenght__):
                self.tape.append('Λ')
            self.__lenght__ *= 2
        self.position += 1

    def L(self) -> None:
        """Move to left."""
        if self.position == 0:
            self.position = self.__lenght__ - 1
            temp = ['Λ' for i in range(self.__lenght__)]
            for i in self.tape:
                temp.append(i)
            self.tape = temp
            self.__lenght__ *= 2
        else:
            self.position -= 1
        
    def write(self, value) -> None:
        """Write value in current position."""
        value = str(value)
        if len(value) != 1:
            raise ValueError
        self.tape[self.position] = value
    
    def __write_for_tests__(self, value) -> None:
        """Writes value to right. Used only for testing"""

        temp = ''
        for i in value:
            temp += i
        value = temp
        
        for i in value:
            self.write(i)
            self.R()
        for i in range(len(value)):
            self.L()
    
    def read(self) -> str:
        """Read value of current position."""
        return self.tape[self.position]

    def print_tape(self) -> None:
        """Print tape and machine position."""
        print('')
        print(' ', end='')
        for i in self.tape:
            print(i, end='')
        print()
        print(' ' * (self.position), 'ᛏ')
    
    def correct_command(self, command: str) -> bool:
        """Checks if command is correct RWMS format"""
        if len(command) < 4:
            return False
        if not command[2] in 'rlmRLM':
            return False
        return True

    def add_state(self, *args) -> None:
        """Adds new state to states list."""
        commands_list = list(args)
        for i in range(len(commands_list)):
            if not self.correct_command(commands_list[i]):
                print('Incorrect command')
                return 0
        self.states.append(commands_list)
    
    def edit_state(self, state_id = None) -> int:
        """Edit specified states commands."""
        if state_id is None:
            print('State id must be specified.')
            return 0
        
        inp = input('Input new commands :\n')
        commands_list = inp.split(' ')
        for i in range(len(commands_list)):
            if not self.correct_command(commands_list[i]):
                print('Incorrect command')
                return 0
        self.states[int(state_id)] = commands_list

    def run_state(self, state_id = 0) -> bool:
        """Runs state with id."""
        if state_id == 0:
            return False

        for command in self.states[state_id]:
            while command[0] == self.read():
                print('state:', state_id, 'command:', command)
                self.write(command[1])
                if command[2].lower() == 'r':
                    self.R()
                elif command[2].lower() == 'l':
                    self.L()
                self.print_tape()
                try:
                    if command[3:] == '0':
                        return False
                    if not self.run_state(int(command[3:])):
                        return False
                except:
                    return False 
        return False


def open_script(file_path: str) -> None:
    """Read script file and apply it's commands to machine."""
    if not file_path.endswith('.rwms'):
        return False
    
    f = open(file_path, 'r')
    lines = f.readlines()
    command_string = ''
    
    for i in range(len(lines)):
        command_string += lines[i]
    command_string = command_string.replace(' ', '').replace('\n', '')
    
    print(command_string)


def execute(M: Machine = Machine()):
    
    saved_tape, saved_pos, saved_L, saved_states = [], 0, 0, []
    M.print_tape()

    while True:
        
        command = input('Machine$ ')
        low_command = [i for i in command.lower()]
        
        for i in range(len(low_command)):

            if low_command[i] == 'r':
                M.R()
            
            elif low_command[i] == 'l':
                M.L()
            
            elif low_command[i] == 'w':
                try:
                    M.write(command[i + 1])
                    low_command[i + 1] = ' '
                except IndexError:
                    w = input()
                    if len(w) == 1:
                        M.write(w)
            
            elif low_command[i] == '/':
                subcommand = input()
                subcommand = subcommand.split(' ')
                
                if subcommand[0] == 'new':
                    try:
                        M.add_state(*subcommand[1:])
                    except IndexError:
                        print('Please write commands for state.')
                        inp = input()
                        try:
                            M.add_state(inp)
                        except Exception:
                            print('Try again.')
                    except Exception:
                        print("Something went wrong while creating state.")
                
                elif subcommand[0] == 'edit':
                    try:
                        M.edit_state(subcommand[1])
                    except IndexError:
                        print('States id must be specified')
                    # except:
                    #     print('Something went wrong during editing')

                elif subcommand[0] == 'run':
                    try:
                        M.run_state(int(subcommand[1]))
                    except IndexError:
                        M.run_state(0)
                    except Exception:
                        print("Something went wrong with state index.")
                
                elif subcommand[0] == 'write':
                    try:
                        M.__write_for_tests__(subcommand[1:])
                    except IndexError:
                        print('Write to tape: ')
                        inp = input()
                        try:
                            M.__write_for_tests__(inp)
                        except Exception:
                            print('Try again.')
                
                elif subcommand[0] == 'save':
                    saved_L = M.__lenght__
                    saved_tape[:] = M.tape[:]
                    saved_states = M.states
                    saved_pos = M.position
                
                elif subcommand[0] == 'load':
                    M.__lenght__ = saved_L
                    M.tape[:] = saved_tape[:]
                    M.states = saved_states
                    M.position = saved_pos
                
                elif subcommand[0] == 'reset':
                    M = Machine()
                
                elif subcommand[0] == 'states':
                    for i in range(len(M.states)):
                        print(i, M.states[i])
                
                else:
                    print('Wrong command.')
            
            elif low_command[i] == 'q':
                quit()
        
        M.print_tape()

if __name__ == '__main__':
    while True:
        command = input('$ ')
        command = command.split(' ')
        
        if command[0] == 'readfile':
            open_script('script.rwms')
        # try:
        #     M.open(subcommand[1])
        # except IndexError:
        #     print('Path to script file: ')
        #     inp = input()
        #     try:
        #         M.open(inp)
        #     except:
        #         print('Try again.')
        
        elif command[0] == 'help':
            print(HELP)

        elif command[0] == 'execute':
            execute()
 