# Function to retrieve Conservation Status of Species in a new dataframe
def get_species_conservation_status(dataframe, conservation_status):
    species_conservation_status = dataframe[dataframe['conservation_status'] == conservation_status].reset_index()
    return species_conservation_status