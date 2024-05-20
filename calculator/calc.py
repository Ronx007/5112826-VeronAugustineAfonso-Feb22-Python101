import argparse

def main():
    parser = argparse.ArgumentParser(description='Perform calculations on a list of numbers.')
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-s', '--sum', action='store_true', help='Calculate the sum of all the following numbers')
    group.add_argument('-a', '--average', action='store_true', help='Calculate the average of all the following numbers')
    group.add_argument('-m', '--min', action='store_true', help='Find the lowest number of all the following numbers')
    group.add_argument('-x', '--max', action='store_true', help='Find the highest number of all the following numbers')
    
    output_group = parser.add_mutually_exclusive_group()
    output_group.add_argument('-f', '--float', action='store_true', help='Output the result as a floating-point number')
    output_group.add_argument('-i', '--int', action='store_true', help='Output the result as an integer')
    
    parser.add_argument('numbers', metavar='N', type=float, nargs='+', help='A list of numbers to operate on')

    args = parser.parse_args()

    if args.sum:
        result = sum(args.numbers)
    elif args.average:
        result = sum(args.numbers) / len(args.numbers)
    elif args.min:
        result = min(args.numbers)
    elif args.max:
        result = max(args.numbers)
    
    if args.float:
        result = float(result)
    elif args.int:
        result = int(result)
    else:
        result = float(result)

    print(result)

if __name__ == '__main__':
    main()
