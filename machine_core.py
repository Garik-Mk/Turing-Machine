#THIS FILE WILL BE REMOVED WHEN GUI WILL BE ADDED
SAVED_TAPE, SAVED_POS, SAVED_L, SAVED_STATES = [], 0, 0, []


class Machine(object):
    def __init__(self) -> None:
        self.__lenght = 10 
        self.tape = ['Λ' for i in range(self.__lenght + 1)] 
        self.position = 0
        self.states = ['p']
        
    def R(self) -> None:
        """Move to right."""
        if self.__lenght <= self.position:
            for i in range(self.__lenght):
                self.tape.append('Λ')
            self.__lenght *= 2
        self.position += 1

    def L(self) -> None:
        """Move to left."""
        if self.position == 0:
            self.position = self.__lenght - 1
            temp = ['Λ' for i in range(self.__lenght)]
            for i in self.tape:
                temp.append(i)
            self.tape = temp
            self.__lenght *= 2
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
    
    def correct_command(self, command: str) -> bool:
        """Checks if command is correct RWMS format"""
        if len(command) < 4:
            return False
        if not command[2] in 'rlnRLN':
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
                self.print_tape() #will be reworked
                try:
                    if command[3:] == '0':
                        return False
                    if not self.run_state(int(command[3:])):
                        return False
                except:
                    return False 
        return False

    def __str__(self) -> str:
        """Print tape and machine position."""
        result = ' '
        for i in self.tape:
            result += i
        result += '\n'
        result += (' ' * (self.position) + ' ᛏ\n')
        return result

    def process_script(self, script: str) -> None:
        ...

    def print_tape(self): # temproray
        result = ' '
        for i in self.tape:
            result += i
        result += '\n'
        result += (' ' * (self.position) + ' ᛏ\n')
        print(result)
    
    def process_command(self, command: str) -> None:
        for i in range(len(command)):

                if command[i] == 'r':
                    self.R()
                
                elif command[i] == 'l':
                    self.L()
                
                elif command[i] == 'w':
                    try:
                        self.write(command[i + 1])
                        command[i + 1] = ' '
                    except IndexError:
                        w = input()
                        if len(w) == 1:
                            self.write(w)
                
                elif command[i] == '/':
                    subcommand = input()
                    subcommand = subcommand.split(' ')
                    
                    if subcommand[0] == 'new':
                        try:
                            self.add_state(*subcommand[1:])
                        except IndexError:
                            print('Please write commands for state.')
                            inp = input()
                            try:
                                self.add_state(inp)
                            except Exception:
                                print('Try again.')
                        except Exception:
                            print("Something went wrong while creating state.")
                    
                    elif subcommand[0] == 'edit':
                        try:
                            self.edit_state(subcommand[1])
                        except IndexError:
                            print('States id must be specified')
                        # except:
                        #     print('Something went wrong during editing')

                    elif subcommand[0] == 'run':
                        try:
                            self.run_state(int(subcommand[1]))
                        except IndexError:
                            self.run_state(1)
                        except Exception:
                            print("Something went wrong with state index.")
                    
                    elif subcommand[0] == 'write':
                        try:
                            self.__write_for_tests__(subcommand[1:])
                        except IndexError:
                            print('Write to tape: ')
                            inp = input()
                            try:
                                self.__write_for_tests__(inp)
                            except Exception:
                                print('Try again.')
                    
                    elif subcommand[0] == 'save':
                        SAVED_L = self.__lenght__
                        SAVED_TAPE[:] = self.tape[:]
                        SAVED_STATES = self.states
                        SAVED_POS = self.position
                    
                    elif subcommand[0] == 'load':
                        self.__lenght__ = SAVED_L
                        self.tape[:] = SAVED_TAPE[:]
                        self.states = SAVED_STATES
                        self.position = SAVED_POS
                    
                    elif subcommand[0] == 'states':
                        for i in range(len(self.states)):
                            print(i, self.states[i])
                    
                    else:
                        print('Wrong command.')

