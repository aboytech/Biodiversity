# Function to retrieve Conservation Status of Species in a new dataframe
def get_species_conservation_status(dataframe, conservation_status):

    species_conservation_status = dataframe[dataframe['conservation_status'] == conservation_status].reset_index()
    return species_conservation_status

# Function to get aggregate statistics for a dataframe
def get_aggregates(dataframe, column_name, column_formal, type):

    mean = dataframe[column_name].mean()
    median = dataframe[column_name].median()
    mode = dataframe[column_name].mode()
    min = dataframe[column_name].min()
    max = dataframe[column_name].max()

    print(f"""
    {type} {column_formal} Average = {mean}
    {type} {column_formal} Median = {median}
    {type} {column_formal} Mode = {mode}
    {type} {column_formal} Min = {min}
    {type} {column_formal} Max = {max}
    """)

    return mean, median, mode, min, max

