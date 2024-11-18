#!/usr/bin/env python3
import argparse
import time
import os
import subprocess

from vodo.utils import todoFileEncoder, setStatus, counter
from vodo.updates import *
from vodo.interact import interactiveSession
from vodo.checklist import todoCheckList



TAB_SPACING = 3
parser = argparse.ArgumentParser(
        description='voDO! ')

    

def main():
    target = 'TODO'
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    text = ""
    HEADING = ""
    NEWLINE = "\n"
    ID = counter(target)
    statuses = ['1', '2', '3', '4']



    interactive = parser.add_mutually_exclusive_group() 
    
    interactive.add_argument(
        '-i, --interactive', action='store_true', dest='interactive', 
        help="Spawns an interactive session.")

    parser.add_argument(
            'user_input', type=str, help='', metavar='task', nargs="?") 
    
    parser.add_argument(
            '-s, --status', type=str, choices=statuses, dest='status', metavar='status message', nargs="?", 
            help='status of Todo Task. Available Options = { 1: to-be-determined, 2: in-progress, 3: blocked, 4:cancelled }')

    parser.add_argument(
            '-d, --delete-preexisting', action='store_true', dest='delete',
            help='deletes TODO file if it exists in the current working directory')

    parser.add_argument(
            '-n, --notes', type=str, metavar='extra notes', dest='notes', 
            help="Add a note on todo task for better context.")    

    args = parser.parse_args()
    
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
            'data': setStatus(args.status, parser, interactiveModeEnabled=args.interactive),
            'status': True,
        },
        'NOTES':  {
            'name': 'NOTES',
            'data': args.notes,
            'status': True,
        }

    }


    # Jumps to interactiveSession()
    if args.interactive:
        return interactiveSession(flags, target)


    if not args.interactive:
        if not args.status:
            if not args.user_input:
                parser.error("the following arguments are required: task, -s, --status")
            else:
                parser.error('the following argumens are required: -s, --status')



    # Checks if file decoding was successful
    if not ID or not isinstance(ID, int):
        parser.error('TODO File might\'ve been corrupted or tamperred with. '
                     'Please remove the file or specify the -d,--delete-existing flag to force deletion.')
    if args.delete:
        if os.path.exists(target):
            os.remove(target)


    
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

        subprocess.run([ "cat", "./TODO" ])


if __name__ == '__main__':
    main()  
