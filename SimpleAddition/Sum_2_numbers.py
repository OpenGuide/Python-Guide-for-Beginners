while True:
    try:
        print("Enter the value of X and press Enter")
        x = float(input('X: '))

        print("Enter the value of Y and press Enter")
        y = float(input('Y: '))

        # X+Y
        print('X+Y: ', x + y)

        print("========== End ==========")

    except ValueError:
        print('Please input an INTEGER...')

