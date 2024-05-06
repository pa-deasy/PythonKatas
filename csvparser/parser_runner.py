from typing import Optional
from console import print_message
from custom_parser import ParserArgs, parse_line
from input_mapping import map_delimiter, map_header_included
from user_interaction import InputArgs, get_input_args


def run(input_args: Optional[InputArgs] = None) -> None:
    if not input_args:
        input_args = get_input_args()
        
    parser_args = ParserArgs(
        delimiter=map_delimiter(input_args.delimiter),
        header_included=map_header_included(input_args.header_included)
    )
    
    file = open(input_args.file_location, 'r')
    
    for line in file:
        fields = parse_line(line, parser_args)
        print_message(fields)
    

if __name__ == "__main__":
    run()
