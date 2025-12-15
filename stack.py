stack = []
def menu():
    print('Operations:')
    print('1. Push')
    print('2. Pop')
    print('3. Peek')
    print('4. Size')
    print('5. Display')
    print('6. Quit')

def main():
    while True:
        menu()
        choice = int(input('Enter your option (1-6)'))
        if choice == 1:
            if len(stack) == 8:
                print('Stack is full')
            else:
                item = input('Enter an item to push: ')
                stack.append(item)
        elif choice == 2:
            if len(stack) == 0:
                print('Stack is already empty')
            else:
                print(f'Removing item {stack[-1]} from list')
                stack.pop()
        elif choice == 3:
             print(f'The top of the stack is {stack[-1]}')
        elif choice == 4:
            print(f'The Stack has {len(stack)} items')
        elif choice == 5:
            print(stack)
        elif choice == 6:
            break
        else:
            print('Pick a number of 1-6')
main()
