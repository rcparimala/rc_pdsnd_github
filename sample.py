import pandas as pd

def analyze_data(data_file):
    # Load the dataset
    data = pd.read_csv(data_file)
    
    # Perform some analysis
    summary = data.describe()
    
    # Print summary statistics
    print(summary)

if __name__ == "__main__":
    data_file = "dataset.csv"
    analyze_data(data_file)

