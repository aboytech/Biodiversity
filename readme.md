# Biodiversity Project

This dataset comes from the United States National Parks and gathers information from different species living in those parks and what their conservation status are.

## Variables

- **Category:** if it's a *Vascular Plant*, *Nonvascular Plant*, *Bird*, *Amphibian*, *Reptile*, *Mammal* or *Fish*.
- **Scientific Name:** each species scientific name.
- **Common Name:** each species common name.
- **Conservation Status:** whether that species is *Endangered*, *Threatened*, *Of Concern*, *In Recover* or *Not in Danger*.
- **Park Name:** *Bryce Natioanl Park*, *Yellowstone National Park*, *Great Smoky Mountains National Park* or *Yosemite National Park*.
- **Observations:** how many observations each species has.

## Missing Data

When merging this dataset, I found that **96%** of conservation status rows of the total dataset **(25,601 rows)** where missing. It wouldn't be safe to delete all those values, eventhough it was *almost a 100% of missing values*, because I wanted to explore further the relationship between each conservation status.

In order to know which technique I will address for these values, I explored the observations for each conservation status, and also analyze how many of these values where missing for each National Park. 

Finally, I addressed it as **Structurally Missing Data** because each Park had the same amount of missing values, and their observations where far above the mean of every other subset of the original dataframe. So I came to the conclusion that all those missing values were **Species not in Danger**.