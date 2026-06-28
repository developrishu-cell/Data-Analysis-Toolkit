def data_manipulation(df):

    while True:

        print("""
================ DATA MANIPULATION ================

Data Cleaning
1. Drop Rows
2. Drop Columns
3. Rename Columns
4. Fill Missing Values
5. Drop Missing Values
6. Remove Duplicate Rows
7. Replace Values
8. Change Data Type

Sorting
9. Sort Rows
10. Sort Columns

Filtering
11. Filter Data

Column Operations
12. Add New Column
13. Delete Column
14. Modify Column

Grouping
15. Group By
16. Pivot Table

Export
17. Save Dataset

18. Back

===================================================
""")

        choice = input("Enter your choice: ").strip()

        try:

            # ---------------- DROP ROWS ----------------

            if choice == "1":

                print(df.index.tolist())

                rows = input(
                    "Enter row indices to delete (comma separated): "
                ).split(",")

                rows = [int(i.strip()) for i in rows]

                confirm = input(
                    "Proceed? (yes/no): "
                ).lower().strip()

                if confirm == "yes":
                    df.drop(index=rows, inplace=True)
                    df.reset_index(drop=True, inplace=True)
                    print("Rows deleted successfully.")
                else:
                    print("Operation cancelled.")

            # ---------------- DROP COLUMNS ----------------

            elif choice == "2":

                print(df.columns.tolist())

                cols = input(
                    "Enter columns to delete (comma separated): "
                ).split(",")

                cols = [c.strip() for c in cols]

                confirm = input(
                    "Proceed? (yes/no): "
                ).lower().strip()

                if confirm == "yes":
                    df.drop(columns=cols, inplace=True)
                    print("Columns deleted successfully.")
                else:
                    print("Operation cancelled.")

            # ---------------- RENAME COLUMN ----------------

            elif choice == "3":

                print(df.columns.tolist())

                old = input("Old column name: ")
                new = input("New column name: ")

                confirm = input(
                    "Proceed? (yes/no): "
                ).lower().strip()

                if confirm == "yes":
                    df.rename(columns={old: new}, inplace=True)
                    print("Column renamed successfully.")

            # ---------------- FILL MISSING ----------------

            elif choice == "4":

                print(df.isnull().sum())

                col = input("Column name: ")

                print("""
1. Mean
2. Median
3. Mode
4. Custom Value
""")

                method = input("Choose: ")

                if method == "1":
                    value = df[col].mean()

                elif method == "2":
                    value = df[col].median()

                elif method == "3":
                    value = df[col].mode()[0]

                elif method == "4":
                    value = input("Enter custom value: ")

                else:
                    print("Invalid option.")
                    continue

                confirm = input(
                    "Proceed? (yes/no): "
                ).lower().strip()

                if confirm == "yes":
                    df[col].fillna(value, inplace=True)
                    print("Missing values filled.")

            # ---------------- DROP MISSING ----------------

            elif choice == "5":

                confirm = input(
                    "All rows containing missing values will be removed. Proceed? (yes/no): "
                ).lower().strip()

                if confirm == "yes":
                    df.dropna(inplace=True)
                    df.reset_index(drop=True, inplace=True)
                    print("Rows removed.")

            # ---------------- REMOVE DUPLICATES ----------------

            elif choice == "6":

                print(f"Duplicate Rows: {df.duplicated().sum()}")

                confirm = input(
                    "Proceed? (yes/no): "
                ).lower().strip()

                if confirm == "yes":
                    df.drop_duplicates(inplace=True)
                    df.reset_index(drop=True, inplace=True)
                    print("Duplicates removed.")

            # ---------------- REPLACE VALUES ----------------

            elif choice == "7":

                old = input("Value to replace: ")
                new = input("Replace with: ")

                confirm = input(
                    "Proceed? (yes/no): "
                ).lower().strip()

                if confirm == "yes":
                    df.replace(old, new, inplace=True)
                    print("Replacement completed.")

            # ---------------- CHANGE DATATYPE ----------------

            elif choice == "8":

                print(df.dtypes)

                col = input("Column name: ")
                dtype = input(
                    "Datatype (int,float,str,bool): "
                ).lower()

                mapping = {
                    "int": int,
                    "float": float,
                    "str": str,
                    "bool": bool
                }

                if dtype not in mapping:
                    print("Invalid datatype.")
                    continue

                confirm = input(
                    "Proceed? (yes/no): "
                ).lower().strip()

                if confirm == "yes":
                    df[col] = df[col].astype(mapping[dtype])
                    print("Datatype changed.")

            # ---------------- SORT ROWS ----------------

            elif choice == "9":

                print(df.columns.tolist())

                col = input("Sort by column: ")

                order = input(
                    "Ascending? (yes/no): "
                ).lower()

                ascending = True if order == "yes" else False

                df.sort_values(
                    by=col,
                    ascending=ascending,
                    inplace=True
                )

                print(df.head())

            # ---------------- SORT COLUMNS ----------------

            elif choice == "10":

                order = input(
                    "Ascending? (yes/no): "
                ).lower()

                ascending = True if order == "yes" else False

                df = df.sort_index(
                    axis=1,
                    ascending=ascending
                )

                print(df.columns.tolist())

            # ---------------- FILTER ----------------

            elif choice == "11":

                print(df.columns.tolist())

                col = input("Column: ")

                condition = input(
                    "Condition (>,<,>=,<=,==,!=): "
                )

                value = input("Value: ")

                query = f"`{col}` {condition} @value"

                print(df.query(query))

            # ---------------- ADD COLUMN ----------------

            elif choice == "12":

                name = input("New column name: ")

                value = input(
                    "Default value: "
                )

                df[name] = value

                print("Column added.")

            # ---------------- DELETE COLUMN ----------------

            elif choice == "13":

                print(df.columns.tolist())

                col = input("Column name: ")

                confirm = input(
                    "Proceed? (yes/no): "
                ).lower()

                if confirm == "yes":
                    df.drop(columns=col, inplace=True)
                    print("Column deleted.")

            # ---------------- MODIFY COLUMN ----------------

            elif choice == "14":

                print(df.columns.tolist())

                col = input("Column: ")

                value = input(
                    "Enter new value for all rows: "
                )

                confirm = input(
                    "Proceed? (yes/no): "
                ).lower()

                if confirm == "yes":
                    df[col] = value
                    print("Column updated.")

            # ---------------- GROUP BY ----------------

            elif choice == "15":

                print(df.columns.tolist())

                group_col = input("Group by: ")
                agg_col = input("Aggregate column: ")

                print("""
1. Sum
2. Mean
3. Count
4. Min
5. Max
""")

                option = input("Choose: ")

                if option == "1":
                    print(df.groupby(group_col)[agg_col].sum())

                elif option == "2":
                    print(df.groupby(group_col)[agg_col].mean())

                elif option == "3":
                    print(df.groupby(group_col)[agg_col].count())

                elif option == "4":
                    print(df.groupby(group_col)[agg_col].min())

                elif option == "5":
                    print(df.groupby(group_col)[agg_col].max())

            # ---------------- PIVOT TABLE ----------------

            elif choice == "16":

                index = input("Index column: ")
                values = input("Values column: ")
                columns = input(
                    "Columns (optional): "
                )

                if columns == "":
                    columns = None

                print(
                    df.pivot_table(
                        index=index,
                        values=values,
                        columns=columns,
                        aggfunc="mean"
                    )
                )

            # ---------------- EXPORT ----------------

            elif choice == "17":

                path = input("Enter file name (without extension): ")

                print("""
1. CSV
2. Excel
3. JSON
""")

                fmt = input("Choose format: ")

                if fmt == "1":
                    df.to_csv(path + ".csv", index=False)

                elif fmt == "2":
                    df.to_excel(path + ".xlsx", index=False)

                elif fmt == "3":
                    df.to_json(path + ".json", orient="records")

                print("Dataset saved successfully.")

            # ---------------- BACK ----------------

            elif choice == "18":
                return df

            else:
                print("Invalid Choice!")

        except Exception as e:
            print("Error:", e)
