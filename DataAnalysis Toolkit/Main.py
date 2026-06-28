import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from startmenu import start_menu
from graph import graph
from datamanipulation import data_manipulation
from createdataframe import create_dataframe
from datavisualisation import data_visualisation

def main_menu(df):
    while True:
        print("""
==================== MAIN MENU ====================

1. Graph
2. Data Visualisation
3. Data Manipulation
4. Load Another File
5. Exit

===================================================
""")

        choice = input("Choose an option: ").lower().strip()

        if choice == "graph":
            graph(df)

        elif choice == "data visualisation":
            data_visualisation(df)

        elif choice == "data manipulation":
            data_manipulation(df)

        elif choice == "load another file":
            return "load"

        elif choice == "exit":
            return "exit"

        else:
            print("Invalid choice! Please try again.\n")


def main():
    while True:
        start_menu()

        while True:
            try:
                file_path = input("Paste the path of the data here: ")
                df = create_dataframe(file_path)
                print("Dataset loaded successfully!\n")
                break
            except Exception as e:
                print(f"Error: {e}\nPlease try again.\n")

        action = main_menu(df)

        if action == "load":
            continue      # Goes back to Start Menu


        elif action == "exit":
            print("Closing Program...")
            sys.exit()




if __name__=="__main__":
    main()