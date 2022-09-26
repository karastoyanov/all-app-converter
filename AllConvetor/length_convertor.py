from PyQt5.QtWidgets import QApplication
# import lenght_page

def calculate(left, right, value):
    l = left
    r = right
    v = int(value)
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
            result == v * 39.37007874
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
        elif r == 'Foor':
            result = v * 3280.839895
        elif r == 'Inch':
            result = v * 39370.07874
        elif r == 'Light Year':
            result = v * 1.057008707E-13
    elif l == 'Centimeter':
        if r == 'Meter':
            result = v * 0.01
        elif r == 'Kilomter':
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
            result == v * 0.3937007874
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
        
    return result





# app = QApplication([])
# k = lenght_page.LengthMenu()
# app.exec_()
# # left_side = k.left_side.currentText()
# # right_side = k.right_side.currentText()
# # value = k.value.text()



# # print(left_side, right_side)
# # print(value)
# # calculate(left_side, right_side, int(value))