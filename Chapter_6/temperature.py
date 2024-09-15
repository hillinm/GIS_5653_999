celsius = input("What is the temperature in celsius? ")

def convert_cel_to_far(celsius):
    """Converts the temperature inputted in as celsius to fahrenheit"""
    fahrenheit = float(celsius) * 9/5 + 32
    return f"The temperature in fahrenheit is {fahrenheit}\u00B0F"

print(convert_cel_to_far(celsius))

fahrenheit = input("What is the temperature in fahrenheit? ")

def convert_far_to_cel(fahrenheit):
    """Converts the temperature inputted in as fahrenheit to celsius"""
    celsius = (float(fahrenheit) - 32) * 5/9
    return f"The temperature in celsius is {celsius}\u00B0C"

print(convert_far_to_cel(fahrenheit))