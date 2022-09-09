import argparse
from convert_base.from_python import convert

def convert_from_cmdline():
    parser = argparse.ArgumentParser(prog ='convert',
                                     description ='Convert from any base to another base')
    parser.add_argument('number', metavar ='number', type=str, nargs=1, help= 'The number to convert')
    parser.add_argument('fbase', metavar ='fbase', type=int, nargs=1, help= 'The base to convert from')
    parser.add_argument('tbase', metavar ='tbase', type=int, nargs=1, help= 'The base to convert to')
    parser.add_argument('-g', dest='group', type=int, nargs='?', const=4, default=0, help= 'Group the digits?')
    args = parser.parse_args()
    try:
        c = convert(args.number[0], args.fbase[0], args.tbase[0])
        if args.group <= 0:
            print(c)
        else:
            i = 0
            r = ''
            for d in reversed(c):
                r += d
                i += 1
                if i == args.group:
                    i = 0
                    r += ' '
            r = ''.join(reversed(r))
            if r.startswith(' '):
                print(r[1:])
            else:
                l, *m = r.split()
                print(l.zfill(args.group), *m)
        return 0
    except ValueError as e:
        print('An error occurred:', e)
        return 1
