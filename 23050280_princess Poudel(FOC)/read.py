def read_land_data(file_path="Land.txt"):
    """
    Reads data from the specified file and parses it into a dictionary.

    Args:
        file_path (str): The path to the file containing land data. Defaults to "Land.txt".

    Returns:
        dict: A dictionary with the parsed land data, where each key is a land ID and each value is a list of attributes.
    """
    d = {}

    with open(file_path, "r") as file:
        for line in file:
            # Remove any trailing newline characters and split the line by commas
            parts = line.strip().split(",")
            
            # The first part is the key (land ID), and the rest are the values
            key = parts[0]
            value = parts[1:]

            # Add the key-value pair to the dictionary
            d[key] = value

    return d
