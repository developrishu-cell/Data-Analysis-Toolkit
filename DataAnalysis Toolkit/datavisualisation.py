def data_visualisation(df):
    

    while True:

        print("""
=================== DATA VISUALISATION ===================

1. View first n records
2. View last n records
3. View first n columns
4. View last n columns
5. View a specific row (index)
6. View a specific column
7. View multiple columns
8. View rows between two indices
9. View selected rows and columns
10. Display DataFrame shape
11. Display total rows
12. Display total columns
13. Display column names
14. Display index
15. Display data types
16. Display DataFrame information
17. Display summary statistics
18. Display missing values
19. Display duplicate rows
20. Display unique values of a column
21. Display number of unique values
22. Display value counts
23. Random sample of rows
24. Display correlation matrix
25. Display memory usage
26. Check if DataFrame contains null values
27. Back

==========================================================
""")

        choice = input("Enter your choice: ").strip()

        try:

            if choice == "1":
                n = int(input("Enter number of records: "))
                print(df.head(n))

            elif choice == "2":
                n = int(input("Enter number of records: "))
                print(df.tail(n))

            elif choice == "3":
                n = int(input("Enter number of columns: "))
                print(df.iloc[:, :n])

            elif choice == "4":
                n = int(input("Enter number of columns: "))
                print(df.iloc[:, -n:])

            elif choice == "5":
                idx = int(input("Enter row index: "))
                print(df.iloc[idx])

            elif choice == "6":
                col = input("Enter column name: ")
                print(df[col])

            elif choice == "7":
                cols = input("Enter column names separated by commas: ").split(",")
                cols = [c.strip() for c in cols]
                print(df[cols])

            elif choice == "8":
                start = int(input("Start index: "))
                end = int(input("End index: "))
                print(df.iloc[start:end])

            elif choice == "9":
                start = int(input("Start row index: "))
                end = int(input("End row index: "))
                cols = input("Enter column names separated by commas: ").split(",")
                cols = [c.strip() for c in cols]

                print(df.loc[start:end, cols])

            elif choice == "10":
                print("Shape:", df.shape)

            elif choice == "11":
                print("Total Rows:", df.shape[0])

            elif choice == "12":
                print("Total Columns:", df.shape[1])

            elif choice == "13":
                print(df.columns.tolist())

            elif choice == "14":
                print(df.index)

            elif choice == "15":
                print(df.dtypes)

            elif choice == "16":
                df.info()

            elif choice == "17":
                print(df.describe(include="all"))

            elif choice == "18":
                print(df.isnull().sum())

            elif choice == "19":
                print(df[df.duplicated()])

            elif choice == "20":
                col = input("Enter column name: ")
                print(df[col].unique())

            elif choice == "21":
                col = input("Enter column name: ")
                print(df[col].nunique())

            elif choice == "22":
                col = input("Enter column name: ")
                print(df[col].value_counts())

            elif choice == "23":
                n = int(input("Enter sample size: "))
                print(df.sample(n))

            elif choice == "24":
                print(df.corr(numeric_only=True))

            elif choice == "25":
                print(df.memory_usage(deep=True))

            elif choice == "26":
                print(df.isnull().values.any())

            elif choice == "27":
                return

            else:
                print("Invalid Choice.")

        except KeyError:
            print("Column not found.")

        except IndexError:
            print("Index out of range.")

        except ValueError:
            print("Invalid input.")

        except Exception as e:
            print(f"Unexpected Error: {e}")
