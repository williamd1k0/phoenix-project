#-*- encoding: utf-8 -*-


import sys, os.path
import argparse


class PhoenixCode(object):

    def __init__(self, code, value):
        self.code = '{'+code+'}'
        self.value = value

processfile = os.path.realpath(__file__).split('\\')
processfile.pop()
processpath = '\\'.join(processfile)

tablefile = os.path.join(processpath,'charcodes.csv')
codefile = open(tablefile,'r', encoding='utf-8')
_codes = codefile.read().split('\n')

codefile.close()
codes = []

for i in _codes:
    code = i.split(',')
    codes.append(PhoenixCode(code[0],code[1]))

def main(text, output):
    outtext = text
    for code in codes:
        outtext = outtext.replace(code.value, code.code)
    outfile = open(output, 'w', encoding='utf-8')
    outfile.write(outtext)


if __name__ == '__main__':

    parse = argparse.ArgumentParser()
    parse.add_argument('-s','--script', metavar='script-N.txt', help='script file')
    parse.add_argument('-o','--output', metavar='new-script-N.txt', help='script output. Default=[same as input]')

    args = parse.parse_args()

    if args.script is None:
        parse.print_help()
        sys.exit()

    if args.output is None:
        output = args.script
    else:
        output = args.output

    try:
        scriptfile = open(args.script,'r', encoding='utf-8')
        scripttext = scriptfile.read()
        main(scripttext, output)
    except FileNotFoundError:
        print('Error: No such file or directory!')
        sys.exit(2)

