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
    
    
    return (command_string)

    
