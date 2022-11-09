from machine_core import Machine
from misc import open_script

OPENED_MACHINES = {} # {'machine name': machine_object, ...

def execute(M: Machine = Machine()):
    
    saved_tape, saved_pos, saved_L, saved_states = [], 0, 0, []
    print(M)

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
        
        print(M)


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
            f = open('help.txt', 'r')
            lines = f.readlines()
            f.close()
            for line in lines:
                print(line, end='')

        elif command[0] == 'execute':
            execute()

        elif command[0] == 'q':
            quit()