data = []

def menu():
    print('Menu:')
    print('1. Add an item')
    print('2. Mark as done')
    print('3. View items')
    print('4. Exit')

def add_item():
    item = input('What is to be done? ')
    data.append(item)
    print('Item added:', item)

def mark_done():
    item = input('What is to be marked as done? ')
    if item in data:
        data.remove(item)
        print('Item removed:', item)
    else:
        print('Item does not exist in the list')

def view_items():
    if data:
        print('List of to-do items:')
        for index, item in enumerate(data, start=1):
            print(f'{index}. {item}')
    else:
        print('No items in the list')

    
def good_bye():
    print('Goodbye')

# Mapping user choices to functions
choices = {
    '1': add_item,
    '2': mark_done,
    '3': view_items,
    '4': good_bye
}

def main():
    while True:
        menu()
        user_choice = input('Enter your choice (1-4): ')
        if user_choice in choices:
            if user_choice == '4':
                choices[user_choice]()
                break
            choices[user_choice]()
        else:
            print('Invalid choice. Please enter a number between 1 and 4.')

main()
