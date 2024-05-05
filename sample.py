import pandas as pd

def load_and_analyze_data(data_file):
    # Load the dataset
    data = pd.read_csv(data_file)
    
    # Perform basic analysis
    summary = data.describe()
    
    # Print summary statistics
    print(summary)

if __name__ == "__main__":
    data_file = "dataset.csv"
    load_and_analyze_data(data_file)

