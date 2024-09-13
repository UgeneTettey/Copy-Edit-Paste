#  Function to convert data types of columns to specified types

"""This function requires additional code where user creates a dictionary of the desired convertions.
The columns as the keys and corrected datatypes as values."""


def convert_columns_to_datatypes(data,column_datatypes):
    for column, datatype in column_datatypes.items():
        if column in data.columns:
            data[column]=data[column].astype(datatype)
    return data