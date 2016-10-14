admins = {'Python':'Pass123@'}

dayDict = {'sun':[],
           'mon':[],
           'tue':[],
           'wed':[],
           'thur':[],
           'fri':[],
           'sat':[]
           }

def add_event():
    dayToEnter = input('What Day would you wish to add Event?: ')
    eventToEnter = input('Event: ') 

    if dayToEnter in dayDict:
        print('Adding Event...')
        dayDict[dayToEnter].append(eventToEnter)
    else:
        print("Day doesn't exist")


def removeEvent():
    removeDay = input('Which day would you wish to remove your Event? :')
    eventToRemove = input('Which event do you want to remove?:(Events starts from 0)')
    if eventToRemove in dayDict:
        print('removing event...')
        dayDict[removeDay].remove(eventToRemove)

def view_event():
    viewEvent = input('Please input day to view Events: ')
    

    if viewEvent in dayDict:
        print(dayDict[viewEvent])


def main():
    print("""
    Welcome To My Calendar App
		
    Choose a number:

    [1]- Add Event
    [2]- Remove Event
    [3]- View Event
    [4]- Exit
    """)

    action = input('What would you want to do today? (Enter a number) ')

    if action == '1':
        add_event()
    elif action == '2':
        removeEvent()
    elif action == '3':
        view_event()
    elif action == '4':
        exit()
    else:
        print('No valid choice was given, try again')

login = input('Username: ')
passw = input('Password: ')

if login in admins:
    if admins[login]== passw:
        print('Welcome,',login)
	
        while True:
            main()
    else:
        print('Invalid password, will detonate in 5 sec')
else:
    print('Invalid username, calling the FBI to report this!')
