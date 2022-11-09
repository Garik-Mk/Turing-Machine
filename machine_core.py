

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
                self.print_tape()
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
        print('')
        print(' ', end='')
        for i in self.tape:
            print(i, end='')
        print()
        print(' ' * (self.position), 'ᛏ')
        return ''


