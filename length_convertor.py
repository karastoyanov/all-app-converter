def calculate(left, right, value):
    l = left
    r = right
    v = float(value)
    if l == 'Meter':
        if r == 'Meter':
            result = v * 1
        elif r == 'Kilometer':
            result = v * 0.001
        elif r == 'Centimeter':
            result = v * 100
        elif r == 'Millimeter':
            result = v * 1000
        elif r == 'Micrometer':
            result = v * 1000000
        elif r == 'Nanometer':
            result = v * 1000000000
        elif r == 'Mile':
            result = v * 0.0006213689
        elif r == 'Yard':
            result = v * 1.0936132983
        elif r == 'Foot':
            result = v * 3.280839895
        elif r == 'Inch':
            result = v * 39.37007874
        elif r == 'Light Year':
            result = v * 1.057008707E-16
    elif l == 'Kilometer':
        if r == 'Meter':
            result = v * 1000
        elif r == 'Kilometer':
            result = v * 1
        elif r == 'Centimeter':
            result = v * 100000
        elif r == 'Millimeter':
            result = v * 1000000
        elif r == 'Micrometer':
            result = v * 1000000000
        elif r == 'Nanometer':
            result = v * 1000000000000
        elif r == 'Mile':
            result = v * 0.6213688756
        elif r == 'Yard':
            result = v * 1093.6132983
        elif r == 'Foot':
            result = v * 3280.839895
        elif r == 'Inch':
            result = v * 39370.07874
        elif r == 'Light Year':
            result = v * 1.057008707E-13
    elif l == 'Centimeter':
        if r == 'Meter':
            result = v * 0.01
        elif r == 'Kilometer':
            result = v * 0.00001
        elif r == 'Centimeter':
            result = v * 1
        elif r == 'Millimeter':
            result = v * 10
        elif r == 'Micrometer':
            result = v * 10000
        elif r == 'Nanometer':
            result = v * 10000000
        elif r == 'Mile':
            result = v * 0.0000062137
        elif r == 'Yard':
            result = v * 0.010936133
        elif r == 'Foot':
            result = v * 0.032808399
        elif r == 'Inch':
            result = v * 0.3937007874
        elif r == 'Light Year':
            result = v * 1.057008707E-18
    elif l == 'Millimeter':
        if r == 'Meter':
            result = v * 0.001
        elif r == 'Kilometer':
            result = v * 0.000001
        elif r == 'Centimeter':
            result = v * 0.1
        elif r == 'Millimeter':
            result = v * 1
        elif r == 'Micrometer':
            result = v * 1000
        elif r == 'Nanometer':
            result = v * 1000000
        elif r == 'Mile':
            result = v * 6.213688756E-7
        elif r == 'Yard':
            result = v * 0.0010936133
        elif r == 'Foot':
            result = v * 0.0032808399
        elif r == 'Inch':
            result = v * 0.0393700787
        elif r == 'Light Year':
            result = v * 1.057008707E-19
    elif l == 'Micrometer':
        if r == 'Meter':
            result = v * 0.000001
        elif r == 'Kilometer':
            result = v * 9.999999999E-10
        elif r == 'Centimeter':
            result = v * 0.0001
        elif r == 'Millimeter':
            result = v * 0.001
        elif r == 'Micrometer':
            result = v * 1
        elif r == 'Nanometer':
            result = v * 1000
        elif r == 'Mile':
            result = v * 6.213688756E-10
        elif r == 'Yard':
            result = v * 0.0000010936
        elif r == 'Foot':
            result = v * 0.0000032808
        elif r == 'Inch':
            result = v * 0.0000393701
        elif r == 'Light Year':
            result = v * 1.057008707E-22
    elif l == 'Nanometer':
        if r == 'Meter':
            result = v * 1.E-9
        elif r == 'Kilometer':
            result = v * 1.E-12
        elif r == 'Centimeter':
            result = v * 1.E-7
        elif r == 'Millimeter':
            result = v * 0.000001
        elif r == 'Micrometer':
            result = v * 0.001
        elif r == 'Nanometer':
            result == v * 1
        elif r == 'Mile':
            result = v * 6.213688756E-13
        elif r == 'Yard':
            result = v * 1.093613298E-9
        elif r == 'Foot':
            result = v * 3.280839895E-9
        elif r == 'Inch':
            result = v * 3.937007874E-8
        elif r == 'Light Year':
            result = v * 1.057008707E-25
    elif l == 'Mile':
        if r == 'Meter':
            result = v * 1609.35
        elif r == 'Kilometer':
            result = v * 1.60935
        elif r == 'Centimeter':
            result = v * 160935
        elif r == 'Millimeter':
            result = v * 1609350
        elif r == 'Micrometer':
            result = v * 1609350000
        elif r == 'Nanometer':
            result = v * 1609350000000
        elif r == 'Mile':
            result = v * 1
        elif r == 'Yard':
            result = v * 1760.0065617
        elif r == 'Foot':
            result = v * 5280.019685
        elif r == 'Inch':
            result = v * 63360.23622
        elif r == 'Light Year':
            result = v * 1.701096963E-13
    elif l == 'Yard':
        if r == 'Meter':
            result = v * 0.9144
        elif r == 'Kilometer':
            result = v * 0.0009144
        elif r == 'Centimeter':
            result = v * 91.44
        elif r == 'Millimeter':
            result = v * 914.4
        elif r == 'Micrometer':
            result = v * 914400
        elif r == 'Nanometer':
            result = v * 914400000
        elif r == 'Mile':
            result = v * 0.0005681797
        elif r == 'Yard':
            result = v * 1
        elif r == 'Foot':
            result = v * 3
        elif r == 'Inch':
            result = v * 36
        elif r == 'Light Year':
            result = v * 9.665287622E-17
    elif l == 'Foot':
        if r == 'Meter':
            result = v * 0.3048
        elif r == 'Kilometer':
            result = v * 0.0003048
        elif r == 'Centimeter':
            result = v * 30.48
        elif r == 'Millimeter':
            result = v * 304.8
        elif r == 'Micrometer':
            result = v * 304800
        elif r == 'Nanometer':
            result = v * 304800000
        elif r == 'Mile':
            result = v * 0.0001893932
        elif r == 'Yard':
            result = v * 0.3333333333
        elif r == 'Foot':
            result = v * 1
        elif r == 'Inch':
            result = v * 12
        elif r == 'Light Year':
            result = v * 3.22176254E-17
    elif l == 'Inch':
        if r == 'Meter':
            result = v * 0.0254
        elif r == 'Kilometer':
            result = v * 0.0000254
        elif r == 'Centimeter':
            result = v * 2.54
        elif r == 'Millimeter':
            result = v * 25.4
        elif r == 'Micrometer':
            result = v * 25400
        elif r == 'Nanometer':
            result = v * 25400000
        elif r == 'Mile':
            result = v * 0.0000157828
        elif r == 'Yard':
            result = v * 0.0277777778
        elif r == 'Foot':
            result = v * 0.0833333333
        elif r == 'Inch':
            result = v * 1
        elif r == 'Light Year':
            result = v * 2.684802117E-18
    elif l == 'Light Year':
        if r == 'Meter':
            result = v * 9460660000000000
        elif r == 'Kilometer':
            result = v * 9460660000000
        elif r == 'Centimeter':
            result = v * 946066000000000000
        elif r == 'Millimeter':
            result = v * 9460660000000000000
        elif r == 'Micrometer':
            result = v * 9.46066E+21
        elif r == 'Nanometer':
            result = v * 9.460659999E+24
        elif r == 'Mile':
            result = v * 5878559666946
        elif r == 'Yard':
            result = v * 10346303587051618
        elif r == 'Foot':
            result = v * 31038910761154856
        elif r == 'Inch':
            result = v * 372466929133858300
        elif r == 'Light Year':
            result = v * 1
       
    return f'{result:.3f}'

