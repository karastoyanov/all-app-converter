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
        if r == 'Square Meter':
            result = v / 1E-6
        elif r == 'Square Kilometer':
            result = v / 1.E+12
        elif r == 'Square Centimeter':
            result = v / 100
        elif r == 'Square Millimeter':
            result = v * 1
        elif r == 'Square Micrometer':
            result = v / 1E+6
        elif r == 'Hectare':
            result = v / 1E-10
        elif r == 'Square Mile':
            result = v / 2.59E+12
        elif r == 'Square Yard':
            result = v / 836100
        elif r == 'Square Foot':
            result = v / 92900
        elif r == 'Square Inch':
            result = v / 645.2
        elif r == 'Acre':
            result = v / 4.047E+9
    elif l == 'Square Micrometer':
        if r == 'Square Meter':
            result = v / 1E+12
        elif r == 'Square Kilometer':
            result = v / 1E+18
        elif r == 'Square Centimeter':
            result = v / 1E+8
        elif r == 'Square Millimeter':
            result = v / 1E+6
        elif r == 'Square Micrometer':
            result = v * 1
        elif r == 'Hectare':
            result = v / 1E+16
        elif r == 'Square Mile':
            result = v / 2.59E+18
        elif r == 'Square Yard':
            result = v / 8.361E+11
        elif r == 'Square Foot':
            result = v / 9.29E+10
        elif r == 'Square Inch':
            result = v / 6.452E+8
        elif r == 'Acre':
            result = v / 4.047E+15
    elif l == 'Hectare':
        if r == 'Square Meter':
            result = v * 1000
        elif r == 'Square Kilometer':
            result = v / 100
        elif r == 'Square Centimeter':
            result = v * 1E+8
        elif r == 'Square Millimeter':
            result = v * 1E+10
        elif r == 'Square Micrometer':
            result = v * 1E+16
        elif r == 'Hectare':
            result = v
        elif r == 'Square Mile':
            result = v / 259
        elif r == 'Square Yard':
            result = v * 11960
        elif r == 'Square Foot':
            result = v * 107600
        elif r == 'Square Inch':
            result = v * 1.55E+7
        elif r == 'Acre':
            result = v * 2.471 
    elif l == 'Square Mile':
        if r == 'Square Meter':
            result = v * 2.59E+6
        elif r == 'Square Kilometer':
            result = v * 2.59
        elif r == 'Square Centimeter':
            result = v * 2.59E+10
        elif r == 'Square Millimeter':
            result = v * 2.59E+12
        elif r == 'Square Micrometer':
            result = v * 2.59E+18
        elif r == 'Hectare':
            result = v * 259
        elif r == 'Square Mile':
            result = v
        elif r == 'Square Yard':
            result = v * 3.098E+6
        elif r == 'Square Foot':
            result = v * 2.788E+7
        elif r == 'Square Inch':
            result = v * 4.014E+9
        elif r == 'Acre':
            result = v * 640
    elif l == 'Square Yard':
        if r == 'Square Meter':
            result = v / 1.196
        elif r == 'Square Kilometer':
            result = v / 1.196E+6
        elif r == 'Square Centimeter':
            result = v * 8361
        elif r == 'Square Millimeter':
            result = v * 836100
        elif r == 'Square Micrometer':
            result = v * 8.361E+11
        elif r == 'Hectare':
            result = v / 11960
        elif r == 'Square Mile':
            result = v / 3.098E+6
        elif r == 'Square Yard':
            result = v
        elif r == 'Square Foot':
            result = v * 9
        elif r == 'Square Inch':
            result = v * 1296
        elif r == 'Acre':
            result = v / 4840
    elif l == 'Square Foot':
        if r == 'Square Meter':
            result = v / 10.764
        elif r == 'Square Kilometer':
            result = v / 1.076E+7
        elif r == 'Square Centimeter':
            result = v * 929
        elif r == 'Square Millimeter':
            result = v * 92900
        elif r == 'Square Micrometer':
            result = v * 9.29E+10
        elif r == 'Hectare':
            result = v / 107600
        elif r == 'Square Mile':
            result = v / 2.788E+7
        elif r == 'Square Yard':
            result = v / 9
        elif r == 'Square Foot':
            result = v
        elif r == 'Square Inch':
            result = v * 144
        elif r == 'Acre':
            result = v / 43560
    elif l == 'Square Inch':
        if r == 'Square Meter':
            result = v / 1550
        elif r == 'Square Kilometer':
            result = v / 1.55E+9
        elif r == 'Square Centimeter':
            result = v * 6.452
        elif r == 'Square Millimeter':
            result = v * 645.2
        elif r == 'Square Micrometer':
            result = v * 6.452E+8
        elif r == 'Hectare':
            result = v / 1.55E+7
        elif r == 'Square Mile':
            result = v / 4.014E+9
        elif r == 'Square Yard':
            result = v / 1296
        elif r == 'Square Foot':
            result = v / 144
        elif r == 'Square Inch':
            result = v
        elif r == 'Acre':
            result = v / 6.273E+6
    elif l == 'Acre':
        if r == 'Square Meter':
            result = v * 4047
        elif r == 'Square Kilometer':
            result = v / 247.1
        elif r == 'Square Centimeter':
            result = v * 4.047E+7
        elif r == 'Square Millimeter':
            result = v * 4.047E+9
        elif r == 'Square Micrometer':
            result = v * 4.047E+15
        elif r == 'Hectare':
            result = v / 2.471
        elif r == 'Square Mile':
            result = v / 640
        elif r == 'Square Yard':
            result = v * 4840
        elif r == 'Square Foot':
            result = v * 43560
        elif r == 'Square Inch':
            result = v * 6.273E+6
        elif r == 'Acre':
            result = v 
    
    return result