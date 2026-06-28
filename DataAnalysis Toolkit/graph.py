import matplotlib.pyplot as plt
import seaborn as sns

def graph(df):
    while True:
        print("\nAvailable Columns:")
        print(df.columns.tolist())

        print("""
================ GRAPH MENU ================

1. Scatterplot
2. Barplot
3. Lineplot
4. Histogram
5. Kernel Density Plot
6. Box Plot
7. Violin Plot
8. Heat Map
9. Pair Plot
10. Stacked Area Plot
11. Swarm Plot
12. Facet Grid
13. Back

============================================
""")

        choice = input("Enter the graph you want to make: ").lower().strip()

        try:

            if choice == "scatterplot":
                x = input("Enter X-axis column: ")
                y = input("Enter Y-axis column: ")

                sns.scatterplot(data=df, x=x, y=y)
                plt.title("Scatter Plot")
                plt.show()

            elif choice == "barplot":
                x = input("Enter X-axis column: ")
                y = input("Enter Y-axis column: ")

                sns.barplot(data=df, x=x, y=y)
                plt.title("Bar Plot")
                plt.show()

            elif choice == "lineplot":
                x = input("Enter X-axis column: ")
                y = input("Enter Y-axis column: ")

                sns.lineplot(data=df, x=x, y=y)
                plt.title("Line Plot")
                plt.show()

            elif choice == "histogram":
                x = input("Enter column: ")

                sns.histplot(data=df, x=x, kde=False)
                plt.title("Histogram")
                plt.show()

            elif choice == "kernel density plot":
                x = input("Enter column: ")

                sns.kdeplot(data=df, x=x, fill=True)
                plt.title("Kernel Density Plot")
                plt.show()

            elif choice == "box plot":
                x = input("Enter categorical column (optional, press Enter to skip): ")
                y = input("Enter numerical column: ")

                if x:
                    sns.boxplot(data=df, x=x, y=y)
                else:
                    sns.boxplot(data=df, y=y)

                plt.title("Box Plot")
                plt.show()

            elif choice == "violin plot":
                x = input("Enter categorical column (optional, press Enter to skip): ")
                y = input("Enter numerical column: ")

                if x:
                    sns.violinplot(data=df, x=x, y=y)
                else:
                    sns.violinplot(data=df, y=y)

                plt.title("Violin Plot")
                plt.show()

            elif choice == "heat map":
                sns.heatmap(df.corr(numeric_only=True),
                            annot=True,
                            cmap="coolwarm")
                plt.title("Correlation Heatmap")
                plt.show()

            elif choice == "pair plot":
                sns.pairplot(df)
                plt.show()

            elif choice == "stacked area plot":

                cols = input(
                    "Enter numeric columns separated by commas: ").split(",")

                cols = [c.strip() for c in cols]

                df[cols].plot.area(stacked=True)
                plt.title("Stacked Area Plot")
                plt.show()

            elif choice == "swarm plot":
                x = input("Enter categorical column: ")
                y = input("Enter numerical column: ")

                sns.swarmplot(data=df, x=x, y=y)
                plt.title("Swarm Plot")
                plt.show()

            elif choice == "facet grid":
                row = input("Row variable (press Enter to skip): ")
                col = input("Column variable (press Enter to skip): ")
                x = input("X-axis column: ")
                y = input("Y-axis column: ")

                g = sns.FacetGrid(
                    df,
                    row=row if row else None,
                    col=col if col else None
                )

                g.map_dataframe(sns.scatterplot, x=x, y=y)
                plt.show()

            elif choice == "back":
                return

            else:
                print("Invalid choice.")

        except KeyError:
            print("One or more column names are invalid.")

        except Exception as e:
            print(f"Error: {e}")
