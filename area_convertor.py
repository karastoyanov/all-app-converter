def calculate(left, right, value):
    l = left
    r = right
    v = int(value)
    if l == 'Square Meter':
        if r == 'Square Meter':
            result = v * 1
        elif r == 'Square Kilometer':
            result = v * 0.000001
        elif r == 'Square Centimeter':
            result = v * 10000
        elif r == 'Square Millimeter':
            result = v * 1000000
        elif r == 'Square Micrometer':
            result = v * 1000000000000
        elif r == 'Hectare':
            result = v * 0.0001
        elif r == 'Square Mile':
            result = v / 2.59E+6
        elif r == 'Square Yard':
            result = v * 1.196
        elif r == 'Square Foot':
            result = v * 10.764
        elif r == 'Square Inch':
            result = v * 1550
        elif r == 'Acre':
            result = v / 4047
    elif l == 'Square Kilometer':
        if r == 'Square Meter':
            result = v * 1000000
        elif r == 'Square Kilometer':
            result = v * 1
        elif r == 'Square Centimeter':
            result = v * 10000000000
        elif r == 'Square Millimeter':
            result = v * 1000000000000
        elif r == 'Square Micrometer':
            result = v * 1000000000000000000
        elif r == 'Hectare':
            result = v * 100
        elif r == 'Square Mile':
            result = v / 2.59
        elif r == 'Square Yard':
            result = v * 1.196E+6
        elif r == 'Square Foot':
            result = v * 1.076E+7
        elif r == 'Square Inch':
            result = v * 1.55E+9
        elif r == 'Acre':
            result = v * 247.10
    elif l == 'Square Centimeter':
        if r == 'Square Meter':
            result = v * 0.0001
        elif r == 'Square Kilometer':
            result = v * 1.E-10
        elif r == 'Square Centimeter':
            result = v * 1
        elif r == 'Square Millimeter':
            result = v * 100
        elif r == 'Square Micrometer':
            result = v * 100000000
        elif r == 'Hectare':
            result = v / 1E+8
        elif r == 'Square Mile':
            result = v / 2.59E+10
        elif r == 'Square Yard':
            result = v / 8361
        elif r == 'Square Foot':
            result = v / 929
        elif r == 'Square Inch':
            result = v / 6.452
        elif r == 'Acre':
            result = v / 4.047E+7
    elif l == 'Square Millimeter':
        #TO DO
        pass
    
    
    return result