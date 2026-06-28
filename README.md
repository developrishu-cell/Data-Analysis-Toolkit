# Data Analysis Toolkit (Python)

A beginner-friendly command-line data analysis toolkit built with **Python**, **Pandas**, **Matplotlib**, and **Seaborn**.

This project allows users to load datasets from multiple file formats, perform common data manipulation operations, explore datasets, and generate visualizations through a menu-driven interface.

> **Note:** This project is still under development. I plan to continue improving and adding new features as I learn more about data analysis and Python.

---

## Features

### Dataset Loading

Supports loading datasets from:

* CSV
* Excel (.xlsx, .xls)
* JSON
* Parquet
* HTML Tables
* XML

---

### Data Exploration

* View first or last records
* Display selected rows and columns
* View DataFrame shape
* Show column names
* Display data types
* Summary statistics
* Missing value analysis
* Duplicate row detection
* Unique values
* Value counts
* Correlation matrix
* Memory usage
* Random sampling

---

### Data Manipulation

* Drop rows
* Drop columns
* Rename columns
* Fill missing values
* Remove missing values
* Remove duplicates
* Replace values
* Change data types
* Sort rows
* Sort columns
* Filter data
* Add new columns
* Delete columns
* Modify existing columns
* Group By operations
* Pivot Tables
* Export cleaned dataset

---

### Data Visualization

Generate visualizations including:

* Scatter Plot
* Bar Plot
* Line Plot
* Histogram
* Kernel Density Plot
* Box Plot
* Violin Plot
* Heatmap
* Pair Plot
* Stacked Area Plot
* Swarm Plot
* Facet Grid

---

## Project Structure

```
DataAnalysisToolkit/
│
├── DataAnalysisProgram.py      # Main program
├── createdataframe.py          # Dataset loader
├── datamanipulation.py         # Data cleaning & manipulation
├── datavisualisation.py        # Data exploration
├── graph.py                    # Graph generation
├── startmenu.py                # Start menu
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/your-username/DataAnalysisToolkit.git
```

Move into the project directory

```bash
cd DataAnalysisToolkit
```

Install the required libraries

```bash
pip install pandas matplotlib seaborn openpyxl pyarrow lxml
```

---

## Running the Project

Run the main program

```bash
python DataAnalysisProgram.py
```

Follow the on-screen menu to:

1. Load a dataset
2. Explore the data
3. Manipulate the dataset
4. Create visualizations

---

## Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn

---

## Future Improvements

Some improvements I plan to add in future updates:

* Better input validation
* More visualization options
* Statistical analysis tools
* Machine learning integration
* Export graphs as images
* Better user interface
* Logging support
* Improved project documentation

---

## Learning Purpose

This project was created as part of my Python and Data Analysis learning journey. The goal was to practice working with Pandas, data manipulation, and data visualization by building a complete menu-driven application.

Feedback and suggestions are always welcome.

---

## Author

**Rishu Ranjan Choudhary**

Learning Python • Data Analysis • Machine Learning
