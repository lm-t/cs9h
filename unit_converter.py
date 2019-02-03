'Project 2a: Unit Converter'

print '''\n\t\tUnit Converter by Luis Torres
You can convert Distances , Weights , and Volumes to one another,
but only within units of the same category, which are shown below.'''
print "Input your measurements to convert in the following format '1 ft in m'."
print '''\n Distances: ft cm mm mi m yd km in
 Weights: lb mg kg oz g
 Volumes: floz qt cup mL L gal pint\n'''
distances_m = {'m': 1.0, 'cm': 0.01, 'mm': 0.001, 'km': 1000, 'in': 0.0254, 'ft': 0.3048, 'yd': 0.9144, 'mi': 1609.34}
weights_kg = {'kg': 1.0, 'g': 0.001, 'mg': 0.000001, 'oz': 0.0283495, 'lb': 0.453592}
volumes_L = {'L': 1.0, 'mL': 0.001, 'gal': 3.78541, 'pint': 0.473176, 'qt': 946353, 'cup': 0.236588, 'floz': 0.0295735}
def conversions(amount, conv_from, conv_to):
    """Returns converted amount from conv_from to conv_to.
    >>> conversions(120, 'mL', 'L')
    0.12
    >>> conversions(150, 'lb', 'kg')
    68.0388
    """
    if conv_from in distances_m:
        return (distances_m[conv_from] / distances_m[conv_to]) * amount
    elif conv_from in weights_kg:
        return (weights_kg[conv_from] / weights_kg[conv_to]) * amount
    else:
        return (volumes_L[conv_from] / volumes_L[conv_to]) * amount
def user_input():
    """Takes input from the user and returns the converted amount. It keeps on repeating until the user wants to quit"""
    string = raw_input("What would you like to convert?, type 'q' to quit: ")
    if 'q' in string:
        return None
    elif ' in ' not in string or len(string.split(' ')) != 4:
        print "format unclear, please follow the format '1 ft in m'"
        return user_input()
    else:
        input = string.split(' ')
        amount = float(input[0])
        conv_from = input[1]
        conv_to = input[3]
        conv_num = conversions(amount, conv_from, conv_to)
        if '.' in input[0]:
            print "%f %s = %f %s" % (amount, conv_from, conv_num, conv_to)
        else:
            print "%d %s = %f %s" % (amount, conv_from, conv_num, conv_to)
        return user_input()
user_input()
