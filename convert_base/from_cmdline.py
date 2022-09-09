import argparse
from convert_base.from_python import convert

def convert_from_cmdline():
    parser = argparse.ArgumentParser(prog ='convert',
                                     description ='Convert from any base to another base')
    parser.add_argument('number', metavar ='number', type=str, nargs=1, help= 'The number to convert')
    parser.add_argument('fbase', metavar ='fbase', type=int, nargs=1, help= 'The base to convert from')
    parser.add_argument('tbase', metavar ='tbase', type=int, nargs=1, help= 'The base to convert to')
    args = parser.parse_args()
    try:
        print(convert(args.number[0], args.fbase[0], args.tbase[0]))
        return 0
    except ValueError as e:
        print('An error occurred:', e)
        return 1
