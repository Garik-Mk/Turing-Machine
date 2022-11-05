def find_closing(string: str, index: int) -> int:
    pass


def find_all_pairs(string: str) -> list:
    list_of_pairs = []
    
    def find_single_pair(string: str) -> tuple:
        for i in range(len(string)):
            if string[i] in '([{':
                opening = i
                closing = find_closing(string, opening)
                new_string = string[:opening] + string[closing+1:]
                print(string, '->', new_string)
                list_of_pairs.append((opening, closing))
                find_single_pair(new_string)
    
    find_single_pair(string)
    return list_of_pairs


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
    
