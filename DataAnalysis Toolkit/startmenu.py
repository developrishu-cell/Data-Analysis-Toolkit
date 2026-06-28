import sys
def start_menu():
    while True:
        choice=input("Enter 'Start' to run program and 'exit' to close program: ").lower().strip()
        if choice=="start":
            print("Program started....\n")
            return        
        elif choice=="exit":
            print("Closing Program....")
            sys.exit(0)
        else:
            print("Invalid Choice! Please enter 'start' or 'exit'. \n")