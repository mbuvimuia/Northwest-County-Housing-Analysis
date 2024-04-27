import pandas as pd

def dataset_info(csv_path):
    try:
        import pandas as pd
        df = pd.read_csv(csv_path)
        print ("\nDimensionality of the dataset is as follows:\n ")
        print(df.shape)       
        print("\nThe columns contained in this dataset are : \n")
        print(df.columns)
        print("\nData types of features: \n")
        print(df.dtypes)
       
       
    except FileNotFoundError:
        print("File not found. Please provide a valid path to the CSV file.")