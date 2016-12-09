#!/usr/bin/python


def calc_and_display_l1(correct_value):
    try:
        while True:
            their_value = float(input('Their value: '))
            percent_error = abs(their_value - correct_value) / correct_value
            grade = 26 - round(percent_error * 100.0 / 2)
            if grade < 0:
                grade = 0
            print('percent error: {:.2%}'.format(percent_error))
            print('grade: {}'.format(grade))
    except ValueError:
        return None


def calc_and_display_l2(correct_value):
    try:
        their_value = float(input('Their value: '))
        percent_error = abs(their_value - correct_value) / correct_value
        grade = 26 - round(percent_error * 100.0 / 2)
        if grade < 0:
            grade = 0
        print('percent error: {:.2%}'.format(percent_error))
        print('grade: {}'.format(grade))
    except ValueError:
        print('Invalid input. Retry entering a number.')
        calc_and_display_l2()


def control():
    while True:
        key = input("'0' for L1, '1' for L2 \#1, '2' for L2 \#2, 'exit' to exit: ")
        if key == '0':
            calc_and_display_l1(0.0181659)
        elif key == '1':
            calc_and_display_l2()
        elif key == '2':
            calc_and_display_l2()
        elif key == 'exit':
            break
        else:
            print("Enter 'exit' to quit. Try input again.")

if __name__ == "__main__":
    control()
