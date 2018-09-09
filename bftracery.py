import json
import argparse
from collections import OrderedDict


parser = argparse.ArgumentParser(description='Compile Boolfuck code to Tracery.')
parser.add_argument('source', type=str,
                    help='the Boolfuck source to compile')
parser.add_argument('--input', metavar='i', type=str,
                    help='optional input data file for the program')

args = parser.parse_args()
with open(args.source) as source_file:
    source = source_file.read()
if input in args:
    with open(args.input) as input_file:
        input = input_file.read()
else:
    input = ""
instruction_map = {
    "+": "+",
    ",": "`",
    ";": ";",
    "<": "<",
    ">": ">",
    "[": "(",
    "]": ")",
}
tracery_instructions = ''.join ('[instrs_upper:{}]'.format(instruction_map[i]) for i in reversed(source))
tracery_input = ''.join('[input:{}]'.format(i) for i in reversed(input))
tracery_init = "[run_next:]" + tracery_instructions + tracery_input
with open("boolfuck.json") as tracery_source:
    tracery = json.load(tracery_source, object_pairs_hook=OrderedDict)
tracery['init'] = tracery_init
with open(args.source+'.json', 'w') as output:
    json.dump(tracery, output, indent='\t')
