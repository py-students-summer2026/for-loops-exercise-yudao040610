def calculate_infections(starting_number_infections, reproduction_rate, num_days):
    current = starting_number_infections
    
    for _ in range(num_days):
        current = current * reproduction_rate
    
    return round(current)
