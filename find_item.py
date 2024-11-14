def find_78001st_item(data):
    """
    Efficiently retrieves the 78,001st item in a given dataset.
    
    Parameters:
    - data: list or array-like dataset with at least 100,000 entries
    
    Returns:
    - The 78,001st item if it exists, else None
    """
    # Check if dataset has enough items
    if len(data) < 78001:
        return None  # Not enough items in the dataset
    
    # Return the 78,001st item (indexing is 0-based in Python)
    return data[78000]

# Example usage
# Assuming 'dataset' is an array or list with 100,000 or more items
dataset = list(range(1, 1000000))  # Example dataset
result = find_78001st_item(dataset)
print(result)
