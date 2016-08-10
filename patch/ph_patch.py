#-*- encoding: utf-8 -*-


import os, sys, subprocess
from colorama import Fore


__version__ = '1.0.0'
__app__ = 'Phoenix Patcher'


XDELTA = os.path.join(os.path.dirname(os.path.realpath(__file__)),'xdelta.exe')

def main(mode, args):
    if mode == 'create':
        create(args.original, args.hacked, args.date, args.output)
    elif mode == 'patch':
        patch(args.original, args.patch, args.output)


def create(original, hacked, _date=False, output=''):
    cmd = XDELTA+' -s "{0}" "{1}" "{2}"'
    
    if output is None:
        output = ''
    
    if _date:
        from datetime import datetime as dt
        date = str(dt.today())
        date = date.replace(' ', '.').replace(':', '-')[:19]
        output = original[:-4]+'@'+date+'.dt'
    
    subprocess.call(cmd.format(original, hacked, output))


def patch(original, _patch, output=''):
    cmd = XDELTA+' -d -s "{0}" "{1}" "{2}"'
    
    if output is None:
        output = original+'-patched.nds'
    
    if output[-4:] != '.nds':
        output += '.nds'
    
    subprocess.call(cmd.format(original, _patch, output))
    

def print_versioninfo():
    print(__app__+' - v'+__version__)


def objection(argument):
    obj = Fore.RED+'Objection!'+Fore.RESET
    print(obj+' '+argument)
    

if __name__ == '__main__':
    
    import argparse
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-v', '--version', action='store_true', help='Show version info and exit')
    parser.add_argument('-c', '--create', action='store_true', help='Set if you want to create a new patch')
    parser.add_argument('-a', '--apply', action='store_true', help='Set if you want to patch a NDS')
    parser.add_argument('-d', '--date', action='store_true', help='Stamp date-time in patch filename')
    parser.add_argument('-O', '--original', metavar='<original>.nds', help='Original NDS file')
    parser.add_argument('-H', '--hacked', metavar='<hacked>.nds', help='Hacked NDS file')
    parser.add_argument('-p', '--patch', metavar='<patchfile>.dt', help='Patch file to apply')
    parser.add_argument('-o', '--output', metavar='<game-patch>|<patched-game>', help='Output file|dir')
    
    args = parser.parse_args()

    if args.version:
        print_versioninfo()

    elif args.create:
        if args.original is None:
            objection('Set an input file (--original)')
        elif args.hacked is None:
            objection('Set a hacked file (--hacked)')
        elif args.output is None and not args.date:
            objection('Set an output file|dir (--output)')
        else:
            try:
                main('create', args)
            except Exception as e:
                objection(str(e))
        
    elif args.apply:
        if args.original is None:
            objection('Set an input file (--original)')
        elif args.patch is None:
            objection('Set a patch file (--patch)')
        else:
            try:
                main('patch', args)
            except Exception as e:
                objection(str(e))
        
    else:
        parser.print_help()
        sys.exit()