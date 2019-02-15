import argparse
import sys


def exit(message):
    print(message)
    sys.exit()


def process_line(data, command):
    if command and command[0] in ['v', 'vt', 'vn', 'f']:
        data.setdefault(command[0], []).append(command[1:])


def process_obj(filename):
    data = {}
    try:
        lines = open(filename, 'r').readlines()
        for line in lines:
            process_line(data, filter(lambda _: _, line.strip().split(' ')))
    except Exception as error:
        exit(error)
    print data.keys()


def generate_mz(filename, obj):
    pass


def convert2mz(param):
    obj = process_obj(param.input)
    generate_mz(param.output, obj)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    parser.add_argument('-o', '--output')
    convert2mz(parser.parse_args())
