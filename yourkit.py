import csv
from argparse import ArgumentParser


def read_csv(path):
    with open(path) as f:
        rows = csv.DictReader(f)
        return {row['searge']: row['name'] for row in rows}


def read_yourkit(path):
    with open(path, 'rb') as f:
        return bytearray(f.read())


def write_yourkit(snapshot, path):
    with open(path, 'wb') as f:
        f.write(snapshot)


def parse_args():
    args = ArgumentParser('Yourkit Snapshot MCP Mappings Converter')
    args.add_argument('methods', help='the methods.csv file')
    args.add_argument('snapshot', help='the original snapshot file')
    args.add_argument('new_snapshot', help='the path where the converted snapshot should be written to')
    return args.parse_args()


def main():
    args = parse_args()
    methods = read_csv(args.methods)
    snapshot = read_yourkit(args.snapshot)
    start = 0
    while True:
        index = snapshot.find(b'func_', start)
        if index == -1:
            break
        raw_int = snapshot[index - 1:index]
        length = int.from_bytes(raw_int, 'big', signed=False)
        raw_bytes = snapshot[index:index + length]
        func_name = raw_bytes.decode()
        if func_name in methods:
            new_name = methods[func_name]
            snapshot[index - 1:index] = len(new_name).to_bytes(1, 'big', signed=False)
            snapshot[index:index + len(func_name)] = new_name.encode()
        start = index + 1
    write_yourkit(snapshot, args.new_snapshot)


if __name__ == '__main__':
    main()
