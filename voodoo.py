#!/usr/bin/env python3

import argparse
import time
import re
import os



TAB_SPACING = 3


    

def main():
    target = 'TODO'
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    text = ""
    HEADING = ""
    NEWLINE = "\n"
    ID = counter(target)
    statuses = ['1', '2', '3']

    parser = argparse.ArgumentParser(
        description='VOODOO! ')
    parser.add_argument(
            'user_input', type=str, help='', metavar='task')
    
    parser.add_argument(
            '-s, --status', type=str, choices=statuses, required=True, dest='status', metavar='status message', 
            help='status of Todo Task. Available Options = { 1: to-be-determined, 2: in-progress, 3: blocked }')

    parser.add_argument(
            '-d, --delete-preexisting', action='store_true', dest='delete',
            help='deletes TODO file if it exists in the current working directory')

    parser.add_argument(
            '-n, --notes', type=str, metavar='extra notes', dest='notes', 
            help="Add a note on todo task for better context.")

    parser.add_argument(
            '-i, --interactive', nargs='?', metavar='interactive', dest='interact',
            help="Spawns an interactive session.")
    

    args = parser.parse_args()

    if args.status:
        if not isinstance(args.status, str):
            parser.error('TODO task status must be a string and' 
                        'specified using the -s or --status flags')

        else:
            match args.status:
               case '1': 
                   args.status = 'to-be-determined'
               case '2': 
                   args.status = 'in-progress'
               case '3':
                   args.status = 'blocked'



    if not ID or not isinstance(ID, int):
        parser.error('TODO File might\'ve been corrupted or tamperred with. '
                     'Please remove the file or specify the -d,--delete-existing flag to force deletion.')
    if args.delete:
        if os.path.exists(target):
            os.remove(target)

    flags ={
        'ID': {
            'name': 'ID',
            'data': ID,
            'status': True,
        }, 
        'TASK': {
            'name': 'TASK',
            'data': args.user_input,
            'status': True,
        }, 
        'TIME': {
            'name': 'TIME',
            'data': timestamp,
            'status': True,
        },
        'STATUS':  {
            'name': 'STATUS',
            'data': args.status,
            'status': True,
        },
        'NOTES':  {
            'name': 'NOTES',
            'data': args.notes,
            'status': True,
        }

    }

    # Iterates over flags dict to determine which flags will be appended
    # to the headers of the file
    columnWidth = {}



    for name,active in flags.items():
        if active['data'] is None:
            text += 'N/A' + '\t' + '\t' + '\t'


        elif active['status'] is True and type(active['status']) is bool:
            text += str(active['data']) + '\t' + '\t' + '\t'

        else:
            text += 'N/A' + '\t' + '\t' + '\t'

        HEADING += active['name'] + "\t" + '\t' + '\t'

    if not os.path.exists(target):
        print('No TODO file located. Generating new one...')


        # Creates new TODO file
        with open(target, 'w') as newfile:
            newfile.write(HEADING)
            newfile.write(NEWLINE)
            newfile.write(text)
            
            print('TODO file created in ' + os.getcwd() + '/' + target)


    else:

        # Works on preexisting TODO file
        with open(target, 'a') as file:
            file.write(NEWLINE)
            file.write(text)

        print('TODO file updated')

        todoCheckList(target)



''' Function called by todoCheckList() function to re-encode
    Todo file with changes that were made by todoCheckList().'''
def todoFileEncoder(file, objKeys):
    if os.path.exists(file):
        with  open(file, 'w') as f:
            column_widths = {}
            for key, items in objKeys.items():
                for idx, item in enumerate(items):
                    column_widths[idx] = max(column_widths.get(idx, len(item)), len(item))
    
            # Write the formatted data to the file
            for key, items in objKeys.items():
                formattedRow = "\t".join([item.ljust(column_widths[idx]) for idx, item in enumerate(items)])
                f.write(formattedRow + '\n')



            print('done')



''' Function that checks grabs each TODO task and asks
    user if updates have been made to task.'''
def todoCheckList(file):
    checklist = {}

    if os.path.exists(file):
        with open(file, 'r') as f:
            count = 0
    
            for line in f:
                lists = []
                count += 1
                entries = line.strip().split('\t')
    
                for entry in entries:
                    if entry != '':
                        regex = re.sub(r'\s+', ' ', entry.strip())

                        lists.append(regex)
                    
    
                    checklist[str(count)] = lists
   

        for key,items in checklist.items():
            
            if len(items) == 0:
                checklist.pop(key)
                break


            elif key == '1' or items[3] == 'COMPLETED':
               pass 
    
            else:


                # Step 1: Confirm if updates were made on task
                step1 = {
                    'done': False,
                    'response': None,
                }
    
                print(f'Task ID {items[0]}:')
                print(f'TODO: {items[1]}')
                print(f'Status: {items[3]}.')
                print(f'Have you made any updates on this task?')
    
                while step1['done'] is False:
                   user = input('(y/n):')
    
                   match user:
                       case 'y':
                            step1['response'] = True
                            step1['done'] = True
                       case 'n':
                           step1['response'] = False
                           step1['done'] = True
                       case _:
                           print('Please choose either \'y\' or \'n\'.')
    
    
                # Step 2: 
                step2 = {
                    'done': False,
                    'response': None,
                    'previous': step1['response']
                }
    
                
                print('Is this task done?')
                    
                while step2['done'] is False:
                    user = input('(y/n):')
    
                    match user:
                        case 'y':
                           step2['done'] = True
                           items[3] = 'COMPLETED'
                           step2['response'] = True
    
    
                        case 'n':
                            step2['done'] = True
                            step2['response'] = False
    
                        case _:
                            print('Please choose either \'y\' or \'n\'.')
    
                # Step 3:
                step3 = {
                    'done': False,
                    'response': None,
                    'previous': step2['response']
                }
    
                if not step3['previous']:
                    print('Do you wish to update this task\'s notes?')
    
                    while step3['done'] is False:
                        user = input('(y/n):')
    
                        match user:
                            case 'y':
                                updateNotes = input('Enter your new notes here... \n')
                                step3['done'] = True
                                items[4] = updateNotes
    
                            case 'n':
                                step3['done'] = True
    
                            case _:
                               print('Please choose either \'y\' or \'n\'.') 
    
                else:
                    pass
    

        todoFileEncoder(file, checklist)



''' Function that decodes the formatted TODO file 
    to get the next task ID'''
def counter(file):
    numbers = []
    count = 0

    if os.path.exists(file):
        with open(file, 'r') as f:
            for line in f:
                if line.strip():
                    if len(numbers) == 0:
                        if line[0].isdigit():
                            numbers.append(int(line[0]))

                    elif len(numbers) >= 10:
                        if line[0].isdigit() and line[1].isdigit():
                            numbers.append(int(line[0] + line[1]))

                    else:
                        if line[0].isdigit():
                            numbers.append(int(line[0]))

        for n in numbers:
            count += 1
            if n != count:
                return False

    else:
        return 1


    return numbers[-1] + 1




if __name__ == '__main__':
    main()  # Remove


    #todoCheckList('TODO')
    #todoFileEncoder('TODO', obj)

    




