#!/usr/bin/env python

########################################################################
#                                                                      #
# This script was written by Thomas Heavey in 2016.                    #
#        theavey@bu.edu     thomasjheavey@gmail.com                    #
#                                                                      #
# Copyright 2016 Thomas J. Heavey IV                                   #
#                                                                      #
# Licensed under the Apache License, Version 2.0 (the "License");      #
# you may not use this file except in compliance with the License.     #
# You may obtain a copy of the License at                              #
#                                                                      #
#    http://www.apache.org/licenses/LICENSE-2.0                        #
#                                                                      #
# Unless required by applicable law or agreed to in writing, software  #
# distributed under the License is distributed on an "AS IS" BASIS,    #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or      #
# implied.                                                             #
# See the License for the specific language governing permissions and  #
# limitations under the License.                                       #
#                                                                      #
########################################################################


def calc_and_display(correct_value, section):
    try:
        their_value = float(input('Their value: '))
    except ValueError:
        # Go back to the menu if anything other than a number is entered
        return None
    percent_error = abs(their_value - correct_value) / correct_value
    grade = 26 - round(percent_error * 100.0 / 2)
    if grade < 0:
        grade = 0
    # Molarity x volume x (mg / mol)
    true_10mL = correct_value * 0.010 * 63546.0
    their_10mL = their_value * 0.010 * 63546.0
    print('\n\nTrue value: {:.4f}'.format(correct_value))
    print('\npercent error: {:.0%}'.format(percent_error))
    print('\ngrade: {}\n'.format(grade))
    print('Their value in 10 mL: {:.2f} mg.'.format(their_10mL))
    print('True value in 10 mL: {:.2f} mg.\n'.format(true_10mL))
    if section == 1:
        # This section all used the same unknown, so just loop through again
        calc_and_display(correct_value, 1)
    return None


def control():
    while True:
        key = input(" '0' for L1\n '1' for L2 #1\n "
                    "'2' for L2 #2\n 'exit' to exit\n Choice: ")
        if key == '0':
            calc_and_display(0.0181659, 1)
        elif key == '1':
            calc_and_display(0.02264, 2)
        elif key == '2':
            calc_and_display(0.01767, 2)
        elif key == 'exit':
            break
        else:
            print("Enter 'exit' to quit. Try input again.")

if __name__ == "__main__":
    control()
