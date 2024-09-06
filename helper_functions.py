import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Function to retrieve Conservation Status of Species in a new dataframe
def get_species_conservation_status(dataframe, conservation_status):

    species_conservation_status = dataframe[dataframe['conservation_status'] == conservation_status].reset_index()
    return species_conservation_status

# Function to get aggregate statistics for a dataframe
def get_aggregates(dataframe, column_name, column_formal, type):

    mean = dataframe[column_name].mean()
    median = dataframe[column_name].median()
    mode = dataframe[column_name].mode()[0]
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

# Plot an histogram to see distributions
def plot_hist(dataframe, column_name, aggregates, xlabel, ylabel, title):

    counts, bins = np.histogram(dataframe[column_name])

    count = 0

    count = 0
    for index in counts:
        if count < index:
            count = index


    plt.hist(dataframe[column_name])
    plt.vlines(x = aggregates[0], ymin = 0, ymax = count, color = 'red', linestyles = 'dotted')
    plt.vlines(x = aggregates[1], ymin = 0, ymax = count, color = 'green', linestyles = 'dotted')
    plt.vlines(x = aggregates[2], ymin = 0, ymax = count, color = 'black', linestyles = 'dotted')
    plt.legend(['Mean', 'Median', 'Mode'])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
    plt.clf()