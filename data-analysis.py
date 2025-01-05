
# Load dataset

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"




import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
try:
    # Load dataset
    filename = input("Enter the CSV file name (including .csv extension): ")
    data = pd.read_csv(url)

    # Display the first few rows
    print("\nFirst 5 rows of the dataset:")
    print(data.head())

    # Display data types and check for missing values
    print("\nDataset Information:")
    print(data.info())

    print("\nSummary of Missing Values:")
    print(data.isnull().sum())

    # Clean the dataset by filling or dropping missing values
    data = data.fillna(data.mean(numeric_only=True))
    print("\nMissing values handled. Updated dataset:")
    print(data.isnull().sum())
except FileNotFoundError:
    print("Error: The file was not found. Please check the file name and try again.")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

# Task 2: Basic Data Analysis
try:
    # Compute basic statistics
    print("\nBasic Statistics of Numerical Columns:")
    print(data.describe())

    # Group by a categorical column and compute mean of a numerical column
    categorical_column = input("Enter the name of a categorical column to group by: ")
    numerical_column = input("Enter the name of a numerical column to compute the mean for: ")

    if categorical_column in data.columns and numerical_column in data.columns:
        grouped = data.groupby(categorical_column)[numerical_column].mean()
        print(f"\nMean of {numerical_column} grouped by {categorical_column}:")
        print(grouped)
    else:
        print("Error: One or both columns do not exist in the dataset.")
        exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()


# Task 3: Data Visualization
try:
    # Set Seaborn style
    sns.set_theme(style="whitegrid")

    # Line chart
    if 'Date' in data.columns:
        data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
        if data['Date'].notnull().any():
            data = data.sort_values('Date')
            plt.figure(figsize=(10, 6))
            sns.lineplot(x='Date', y=numerical_column, data=data)
            plt.title(f"Trend of {numerical_column} Over Time")
            plt.xlabel("Date")
            plt.ylabel(numerical_column)
            plt.show()

    # Bar chart
    plt.figure(figsize=(10, 6))
    grouped.plot(kind='bar', color='skyblue')
    plt.title(f"Average {numerical_column} by {categorical_column}")
    plt.xlabel(categorical_column)
    plt.ylabel(f"Average {numerical_column}")
    plt.show()

    # Histogram
    plt.figure(figsize=(10, 6))
    sns.histplot(data[numerical_column], kde=True, bins=30, color='purple')
    plt.title(f"Distribution of {numerical_column}")
    plt.xlabel(numerical_column)
    plt.ylabel("Frequency")
    plt.show()

    # Scatter plot
    numerical_column_2 = input("Enter another numerical column for scatter plot: ")
    if numerical_column_2 in data.columns:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=numerical_column, y=numerical_column_2, data=data, color='orange')
        plt.title(f"Scatter Plot of {numerical_column} vs {numerical_column_2}")
        plt.xlabel(numerical_column)
        plt.ylabel(numerical_column_2)
        plt.show()
    else:
        print(f"Error: {numerical_column_2} does not exist in the dataset.")
except Exception as e:
    print(f"An error occurred during visualization: {e}")
