import os


test = os.getenv('TEST')


if __name__ == '__main__':
    if test == 'OK':
        print("All tests passed!")

    if test == 'FAILED':
        print('this line does not work!')
