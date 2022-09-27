def calculate(left, right, value):
    l = left
    r = right
    v = int(value)
    if l == 'Celsius':
        if r == 'Celsius':
            result = v * 1
        elif r == 'Kelvin':
            result = v + 273.15
        elif r == 'Fahrenheit':
            result = (v * 9/5) + 32
    elif l == 'Kelvin':
        if r == 'Celsius':
            result = v - 273.15
        elif r == 'Kelvin':
            result = v * 1
        elif r == 'Fahrenheit':
            result = (v - 273.15) * 9/5 + 32
    elif l == 'Fahrenheit':
        if r == 'Celsius':
            result = (v - 32) * 5/9
        elif r == 'Kelvin':
            result = (v - 32) * 5/9 + 273.15
        elif r == 'Fahrenheit':
            result = v * 1
            
    return result