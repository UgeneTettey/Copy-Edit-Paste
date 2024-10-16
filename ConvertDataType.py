#  Function to convert data types of columns to specified types

"""create a dictionary of the desired convertions. The columns as the keys and correct datatypes as values.
The function converts the datatypes of the columns as specified in the dictionary"""



# Dictionary to define the changes
column_datatypes = {
    'column_name': data_type

}


# Function to convert columns to specified data types
def change_columns_datatypes(data, column_datatypes):
    for column, datatype in column_datatypes.items():
        if column in data.columns:
            try:
                data[column] = data[column].astype(datatype)
            except ValueError as e:
                print(f"Error converting column {column}: {e}")
    return data

# Convert the DataFrame
df = change_columns_datatypes(df, column_datatypes)
