#Will be reworked, GUI will be added soon
from machine_core import Machine
from misc import open_script

OPENED_MACHINES = {} # {'machine name': machine_object, ...

def execute(M: Machine = Machine()):

    while True:
        print(M)
        command = input('Machine$ ')
        if command == 'q':
            break
        command = [i for i in command.lower()]
        M.process_command(command)    
        

if __name__ == '__main__':
    while True:
        command = input('$ ')
        command = command.split(' ')
        
        if command[0] == 'readfile':
            try:
                open_script(command[1])
            except IndexError:
                print('Path to script file: ')
                inp = input()
                open_script(inp)
        
        elif command[0] == 'help':
            f = open('help.txt', 'r')
            lines = f.readlines()
            f.close()
            for line in lines:
                print(line, end='')

        elif command[0] == 'execute':
            execute()

        elif command[0] == 'q':
            quit()