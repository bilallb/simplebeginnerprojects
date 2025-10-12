"""
Importing libraries needed
"""
import pandas as pd
"""
getting the csv file and load it properly
"""
FILENAME = 'empty_file.csv'
dataframe = pd.read_csv(FILENAME)
def load_file():
    """
    Loads the csv file
    :return:
    objects: dataframe
    """
    try:
        if dataframe.empty:
            print('File is empty')
            return pd.DataFrame(columns=['Name', 'Email'])
        return dataframe
    except FileNotFoundError:
        print("File not found")
        return pd.DataFrame(columns=['Name', 'Email'])
    except pd.errors.EmptyDataError:
        print('File is empty [no data]')
        return pd.DataFrame(columns=['Name', 'Email'])

