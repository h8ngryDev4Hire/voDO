import os
from vodo.utils import todoFileEncoder
from vodo.checklist import todoCheckList

''' Function that handles the interactive session'''
def interactiveSession(flags, file):
    print('INTERACTIVE MODE ENABLED')
    NEWFILE = True if not os.path.exists(file) else False 
    

    if NEWFILE:
        print('Writing to new TODO file...')


    
    # Get task data
    flags['TASK']['data'] = input('Task: ')

    # Get status data
    flags['STATUS']['data'] = None

    
    while type(flags['STATUS']['data']) is not str:
        print('Give this task a status.')
        print('Options:', 
            '1) To Be Determined',
            '2) In Progress',
            '3) Blocked')

        user = input('(1/2/3): ')

        match user:
            case '1':
                 flags['STATUS']['data'] = 'to-be-determined'

            case '2':
                 flags['STATUS']['data'] = 'in-progress'

            case '3':
                flags['STATUS']['data'] = 'blocked'

            case _:
                print('Task status must be assigned!')
     

    # Get note data if user opts for it
    print('Would you like to add any additional notes ',
          'to this task?')

    note_options = None

    while note_options is None:
        user = input('(y/n): ')

        match user:
            case 'y':
                note_options = True

            case 'n':
                note_options = False

            case _:
                print('Please choose either y or n....')

    if note_options:
        print('Please enter any additional notes you may have...')

        flags['NOTES']['data'] = input('Notes: ')

    else:
        flags['NOTES']['data'] = 'N/A'

    payload = {
        'headers': [flag['name'] for key,flag in flags.items()],
        'data': [str(flag['data']) for key,flag in flags.items()] 
    }

    if not NEWFILE:
        payload.pop('headers') 
        todoFileEncoder(file, payload, 'a')
    else:
        todoFileEncoder(file, payload, 'w')

    todoCheckList(file)


__all__ = ['interactiveSession']
