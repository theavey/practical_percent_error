#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('input', type=float, help='input value to calculate percent error from')

args = parser.parse_args()

correct_value = 0.0181659
percent_error = abs(args.input - correct_value) / correct_value

grade = 26 - round(percent_error * 100.0 / 2)
if grade < 0:
    grade = 0

print('percent error: {:.2%}'.format(percent_error))
print('grade: {}'.format(grade))

