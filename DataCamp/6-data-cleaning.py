from datetime import datetime

def transform_case(input_string):
    """
    Lowercase string fields
    """
    return input_string.lower()
  
def update_date_of_sale(date_input):
    """
    Updates date format from DD/MM/YYYY to YYYY-MM-DD
    """
    current_format = datetime.strptime(date_input, "%d/%m/%Y")
    new_format = current_format.strftime("%Y-%m-%d")
    return new_format

def update_price(price_input):
    """
    Returns price as an integer by removing:
    - "€" and "," symbol
    - Converting to float first then to integer
    """
    # Replace € with an empty string
    price_input = price_input.replace("€", "")
    # Replace comma with an empty string
    price_input = price_input.replace(",", "")
    # Convert to float
    price_input = float(price_input)
    # Return price_input as integer
    return int(price_input)
  
def update_description(description_input):
    """
    Simplifies the description field for future analysis. Returns:
    - "new" if string contains "new" substring
    - "second-hand" if string contains "second-hand" substring
    """
    description_input = transform_case(description_input)
    # Check description and return "new" or "second-hand"
    if "new" in description_input:
        return "new"
    elif "second-hand" in description_input:
        return "second-hand"
    return description_input