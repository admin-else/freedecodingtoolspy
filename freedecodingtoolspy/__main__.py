import argparse
import os
import freedecodingtoolspy

def decode(fname, output, replace):
    if replace:
        output = fname
    with open(fname) as f:
        contents = f.read()
    contents = freedecodingtoolspy.decode(contents)
    if output:
        with open(output, "w") as f:
            f.write(contents)
    else:
        print(contents)


def main():
    parser = argparse.ArgumentParser(prog="python -mfreedecoingtoolspy", description='A script to deobfuscate Python files.')
    parser.add_argument('-o', '--output', metavar='FILENAME', 
                        help='Output file (if not provided, it will print to stdout).')
    parser.add_argument('-r', '--replace', action='store_true', 
                        help='Replace the file with deobfuscated code.')
    parser.add_argument('-v', '--version', action='store_true', 
                        help='Print version information.')
    parser.add_argument('file', help="Specify a file or folder to deobuscate.")
    args = parser.parse_args()
    
    if args.output and args.replace:
        print("Cant have output and replace.")
        exit(1)

    if os.path.isdir(args.file):
        for root, _, files in os.walk(args.file):
            for file in files:
                if not file.endswith('.py'):
                    continue
                file = os.path.join(root, file)
                decode(file, args.output, replace=args.replace)
    else:
        decode(args.file, args.output, args.replace)


if __name__=="__main__":
    main()
