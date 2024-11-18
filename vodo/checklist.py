import os
import re
import sys
from vodo.utils import todoFileEncoder

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


            elif key == '1' or items[3] == 'COMPLETED' or items[3] == 'CANCELLED':
               pass 
    
            else:
                # checklist wizard steps
                # Step 1 Confirms if there were any changes made on task
                step1 = {
                    'done': False,
                    'response': None,
                }
                # Step 2 asks if task was completed if changes were made
                step2 = {
                    'done': False,
                    'response': None,
                    'previous': step1['response'],
                    'completed': False,
                }
                # Step 3 asks for change in task status if not completed yet
                step3 = {
                    'done': False,
                    'response': None,
                    'previous': step2['response'],
                    'cancelled': False
                }
                # Step 4 asks to update notes if either not completed yet or asks
                # for a reason on why task was cancelled
                step4 = {
                    'done': False,
                    'response': None,
                    'previous': step3['response']
                }





                # Step 1: Confirm if updates were made on task    
                print(f'Task ID {items[0]}:')
                print(f'TODO: {items[1]}')
                print(f'Status: {items[3]}.')
                print(f'Have you made any updates on this task?')
    
                while step1['done'] is False:
                   user = input('(y/n/q):')
    
                   match user:
                       case 'y':
                            step1['response'] = True
                            step1['done'] = True
                       case 'n':
                           step1['response'] = False
                           step1['done'] = True
                       case 'q':
                           sys.exit()
                       case _:
                           print('Please choose from the given options.')
    
    
                # Step 2: Ask if task is completed
                if step1['response']:
                    print('Is this task done?')
                        
                    while step2['done'] is False:
                        user = input('(y/n/q):')
    
                        match user:
                            case 'y':
                               step2['done'] = True
                               items[3] = 'COMPLETED'
                               step2['response'] = True
                               step2['completed'] = True
    
    
                            case 'n':
                                step2['done'] = True
                                step2['response'] = False
                            case 'q':
                                sys.exit()
                            case _:
                                print('Please choose from the given options.')
    
                # Step 3: Ask to update status if task not completed
                if not step2['response']:
                    print('Would you like to update this task\'s status?')
                    print('Options:', 
                          '1) To Be Determined',
                          '2) In Progress',
                          '3) Blocked',
                          '4) CANCELLED')
                    
                    while step3['done'] is False:
                        user = input('(1/2/3/4/n/q):')

                        match user:
                            case '1':
                                step3['done'] = True
                                items[3] = 'to-be-determined'
        
                            case '2':
                                step3['done'] = True
                                items[3] = 'in-progress'
                        
                            case '3':
                                step3['done'] = True
                                items[3] = 'blocked'

                            case '4':
                                step3['done'] = True
                                items[3] = 'CANCELLED'
                                step3['cancelled'] = True
                        
                            case 'n':
                                step3['done'] = True
                            case 'q':
                                sys.exit()
                            case _:
                                print('Please choose from the provided options.')


                # Step 4:  Ask to update notes
                if not step2['completed']:
                    if step3['cancelled']:
                        print('Do you wish to add a reason for why task was cancelled?')
                    else:
                        print('Do you wish to update this task\'s notes?')
    
                    while step4['done'] is False:
                        user = input('(y/n/q):')
    
                        match user:
                            case 'y':
                                updateNotes = input('Enter your new notes here... \n')
                                step4['done'] = True
                                items[4] = updateNotes
    
                            case 'n':
                                step4['done'] = True
                            case 'q':
                                sys.exit()
                            case _:
                               print('Please choose from the provided options.') 

        todoFileEncoder(file, checklist, 'w')



__all__ = ['todoCheckList']
