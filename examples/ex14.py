"""
Example to convert a CSV file into a JSON file
"""
import time
import json


def main():
    filename = input('Enter filename: ')
    if not filename.endswith('.csv'):
        raise FileNotFoundError('Need a CSV file!')

    new_filename = f'{filename[:-4]}_{time.time()}.json'
    with open(filename, encoding='utf-8') as f:
        header = f.readline().strip().split(',')
        # customers = []
        # for line in f:
        #   data = line.strip().split(','))
        #   d = dict(zip(header, data)
        #   customers.append(d)
        customers = [
            dict(zip(header, line.strip().split(',')))
            for line in f
        ]

    with open(new_filename, 'w') as f:
        json.dump(customers, f, indent=3)
        print(f'JSON data written to file {new_filename}')


if __name__ == '__main__':
    main()
