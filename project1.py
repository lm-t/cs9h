''' Project 1   Cellular Automation by Luis Torres'''
import sys

rule_num = int(sys.argv[1])
step_num = int(sys.argv[2])
width = 2*step_num + 1
height = step_num + 1
def bin8(num):
    '''
    Returns a binary value of lenght 8 from its integer representation.
    It accepts integer inputs and outputs a string.

    >>> bin8(30)
    '00011110'

    '''
    return format(num, '08b')
def rule(digits3):
    '''
    Returns either a value from the rule for 3 digits.
    It accepts a string of three binary digits
    and outputs a binary digit according to the rule.

    >>> rule_num = 30
    >>> rule('101')
    '0'

    '''
    for i in range(0,8):
        if bin8(i)[5:] == digits3:
            return bin8(rule_num)[::-1][i]
def alter(string):
    '''
    Returns altered string with rules.
    It accepts a sting of binary numbers
    and returns a new set of altered binary numbers.
    '''
    newstring = ''
    string = '0' + string + '0'
    for i in range(0, width):
        newstring = newstring + rule(string[i:(i + 3)])
        #print rule(string[i:(i+3)])
    return newstring

def automate(initial):
    '''
    Takes in an initial string of numbers and alters it with the rule.
    It accepts a string of binary numbers and prints out updated strings until
    it reaches the timestep.
    '''
    i = 0
    while i <= step_num:
        print initial
        initial = alter(initial)
        i += 1

print "P1 %s %s" %  (width, height)
# creates the second line
initial = '0'
for i in range(1, width):
    if len(initial) == step_num:
        initial = initial + '1'
    else:
        initial = initial + '0'
automate(initial)
