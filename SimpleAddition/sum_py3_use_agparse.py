import argparse


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser('Enter two numbers and see the sum of these numbers')

    PARSER.add_argument("-nf", "--first_number", type=float,
                        help="enter the first number")
    PARSER.add_argument("-ns", "--second_number", type=float,
                        help="enter the second number")

    ARGS = PARSER.parse_args()

    FIRST_NUM = ARGS.first_number
    SECOND_NUM = ARGS.second_number

    print('The sum of {0} and {1} is {2}'.format(FIRST_NUM, SECOND_NUM, FIRST_NUM+SECOND_NUM))
