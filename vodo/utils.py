import re
import os


''' Function called by todoCheckList() function to re-encode
    Todo file with changes that were made by todoCheckList().'''
def todoFileEncoder(file, objKeys, bit):
    with  open(file, bit) as f:
        column_widths = {}
        for key, items in objKeys.items():
            for idx, item in enumerate(items):
                column_widths[idx] = max(column_widths.get(idx, len(item)), len(item))
    
        # Write the formatted data to the file
        for key, items in objKeys.items():
            formattedRow = "\t".join([item.ljust(column_widths[idx]) for idx, item in enumerate(items)])
            f.write(formattedRow + '\n')

        print('done')



''' Function that sets status string'''
def setStatus(stdin, parser, interactiveModeEnabled=False):

    if interactiveModeEnabled:
        return stdin

    match stdin:
        case '1':
            stdin = 'to-be-determined'
                    
        case '2':
            stdin = 'in-progress'

        case '3':
            stdin = 'blocked'

        case _:
            parser.error('--status only takes the following options: [1,2,3]')

    return stdin



''' Function that decodes the formatted TODO file 
    to get the next task ID'''
def counter(file):
    if os.path.exists(file):
        # Checks if the file is empty
        if os.path.getsize(file) == 0:
            return 1

        with open(file, 'r') as f:
            numbers = []
            for line in f:
                line = line.strip()
                if line:
                    # Extracts the first one or two digits from the line
                    digits = re.findall(r'^\d{1,2}', line)
                    if digits:
                        numbers.append(int(digits[0]))

            # Checks if the numbers are consecutive
            for i, n in enumerate(numbers, start=1):
                if n != i:
                    return False

            # Returns the next consecutive number
            return numbers[-1] + 1 if numbers else 1

    else:
        # Returns 1 if the file doesn't exist
        return 1



__all__ = ['todoFileEncoder', 'setStatus', 'counter']
