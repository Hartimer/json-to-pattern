import json
import sys
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f',
                        nargs='?',
                        default='[{thread_name:20}] {level:>5} {@timestamp} - {message}',
                        help='Pass a string template. Each token will be replaced with the matching JSON attribute')
    pattern = parser.parse_args().f

    while 1:
        line = sys.stdin.readline()
        if line == '':
            break
        obj = json.loads(line)
        print(pattern.format(**obj))
        sys.stdout.flush()
