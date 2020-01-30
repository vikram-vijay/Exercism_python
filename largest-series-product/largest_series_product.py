def serie_product(serie):
    product = 1
    for char in serie:
       product *= int(char) 
    return product


def largest_product(series, size):
    if size < 0:
        raise ValueError('size must be a non-negative integer')

    # Generate all combinations based on the size
    combinations = (series[i:size+i] for i in range(0, len(series)-size+1))

    # Generate a product for each combination
    products = (serie_product(combination) for combination in combinations)

    # Return the largest product
    return max(products)