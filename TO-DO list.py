user='random'
data=[]

def menu():
    print('menu:')
    print('1.Add an item')
    print('2.Mark as done')
    print('3.View items')
    print('4.Exit')

while user !='4':
    menu()
    user = input('Enter your choice:')

    if user=='1':
        item = input('What is to be done?')
        data.append(item)
    
    elif user == '2':
        item = input('What is to be marked as done?')
        if item in data:
            data.remove(item)
            print('Item removed', item)
        else:
            print('Item does not exist in the list')
    
    elif user == '3':
        print('List to-do items')
        for item in data:
            print(item)
    
    elif user == '4':
        print('Goodbye')
    
    else:
        print('Please enter one of 1, 2, 3 or 4')


