import pandas as pd

def analyze_and_display_data(data_file):
    # Load the dataset
    data = pd.read_csv(data_file)
    
    # Perform statistical analysis
    summary = data.describe()
    
    # Display statistical summary
    print(summary)

if __name__ == "__main__":
    data_file = "dataset.csv"
    analyze_and_display_data(data_file)

