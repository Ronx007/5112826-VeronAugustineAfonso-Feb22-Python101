import argparse
import configparser
import os

def read_numbers_from_file(filename):
    """
    Read numbers from a specified file, one number per line.

    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(delete=False, mode='w') as f:
    ...     _ = f.write("1.0\\n2.0\\n3.5\\n")
    >>> read_numbers_from_file(f.name)
    [1.0, 2.0, 3.5]
    >>> os.remove(f.name)
    """
    with open(filename, 'r') as file:
        numbers = [float(line.strip()) for line in file if line.strip()]
    return numbers

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    default_format = config.get('Output', 'format', fallback='float')
    default_operation = config.get('Operation', 'default', fallback=None)
    input_file = config.get('Input', 'file', fallback=None)

    parser = argparse.ArgumentParser(description='Perform calculations on a list of numbers.')
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-s', '--sum', action='store_true', help='Calculate the sum of all the following numbers')
    group.add_argument('-a', '--average', action='store_true', help='Calculate the average of all the following numbers')
    group.add_argument('-m', '--min', action='store_true', help='Find the lowest number of all the following numbers')
    group.add_argument('-x', '--max', action='store_true', help='Find the highest number of all the following numbers')
    
    output_group = parser.add_mutually_exclusive_group()
    output_group.add_argument('-f', '--float', action='store_true', help='Output the result as a floating-point number')
    output_group.add_argument('-i', '--int', action='store_true', help='Output the result as an integer')
    
    parser.add_argument('numbers', metavar='N', type=float, nargs='*', help='A list of numbers to operate on')

    args = parser.parse_args()

    numbers = args.numbers
    if not numbers and input_file:
        numbers = read_numbers_from_file(input_file)
    if not numbers:
        parser.error('No numbers provided to operate on.')

    if args.sum:
        operation = 'sum'
    elif args.average:
        operation = 'average'
    elif args.min:
        operation = 'min'
    elif args.max:
        operation = 'max'
    else:
        operation = default_operation
    
    if not operation:
        parser.error('No operation specified.')

    if operation == 'sum':
        result = sum(numbers)
    elif operation == 'average':
        result = sum(numbers) / len(numbers)
    elif operation == 'min':
        result = min(numbers)
    elif operation == 'max':
        result = max(numbers)
    
    if args.float:
        result = float(result)
    elif args.int:
        result = int(result)
    else:
        result = int(result) if default_format == 'integer' else float(result)

    print(result)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    main()
