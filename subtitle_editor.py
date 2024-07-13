import argparse

parser = argparse.ArgumentParser()
parser.add_argument("src_filename", help="Source file name.", type=str)
parser.add_argument("-d", "--dest", help="Name of the new file.", type=str, default=None)
parser.add_argument("offset", help="Offset value in terms of seconds.", type=int)

args = parser.parse_args()

offsetVal = args.offset

filename = args.src_filename
if args.dest:
    new_filename = args.dest
elif "." in filename:
    new_filename = filename.replace(".", "_new.")
else:
    new_filename = filename + '_new'

src = open(filename, "r")
dest = open(new_filename, "w")


def increment(s1: str):
    ts = s1.split(":")
    h: int = int(ts[0])
    m: int = int(ts[1])
    s: float = float(ts[2].replace(',', '.'))

    s += offsetVal
    if s >= 60:
        m += 1
        s -= 60

    if m >= 60:
        h += 1
        m -= 60

    return f'{h:02d}:{m:02d}:{s:5.3f}'


for line in src:
    if "-->" in line:
        a = line.split(" --> ")
        dest.write(increment(a[0]) + ' --> ' + increment(a[1]) + "\n")
    else:
        dest.write(line)

src.close()
dest.close()
