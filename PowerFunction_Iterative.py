#!/usr/bin/python

def powerCalculation(number, power):
    if number == 0 or number == 1:
        return number
    
    if power == 0:
        return 1

    result = 1
    sqr = number * number
    for i in range(power//2):
        result = result * sqr
    
    if power%2 == 1:
        result = sqr * number

    print result

def main():
    number = int(raw_input('Enter a number...'))
    power = int(raw_input('Enter power...'))
    powerCalculation(number, power)

if __name__ == '__main__':
    main()
