import os
import sys


def tree(directory, padding):
    print(padding[:-1] + '+--' + os.path.basename(directory) + '/')
    padding = padding + ' '

    files = []
    if os.path.isdir(directory):
        files = os.listdir(directory)
    file_count = 0

    for i, file in enumerate(sorted(files)):
        path = directory + '/' + file
        if os.path.isdir(path):
            tree(path, padding + '|  ')
        else:
            file_count += 1

    print(f'{padding}File count: {file_count}')


def main():
    if len(sys.argv) != 2 or sys.argv[1] in {'-h', '--help'}:
        print('Usage: file-counter <directory>')
        sys.exit(1)

    dir_path = sys.argv[1]
    if not os.path.isdir(dir_path):
        print(f'Error: "{dir_path}" is not a directory.')
        sys.exit(1)

    tree(dir_path, '')


if __name__ == "__main__":
    main()
