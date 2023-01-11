from dataclasses import dataclass
from typing import Optional
from console import print_message, print_message_and_get_input
from input_mapping import DEFAULT_DELIMITER, DEFAULT_HEADER_INCLUDED, file_location_is_valid, header_included_is_valid, map_delimiter


@dataclass
class InputArgs:
    file_location: str
    delimiter: str
    header_included: str


def run(input_args: Optional[InputArgs] = None) -> None:
    if not input_args:
        input_args = _get_input_args()
    
    file = open(input_args.file_location, 'r')
        
    for line in file:
        print_message(line)
    
    
def _get_input_args() -> InputArgs:
    file_location = _get_file_location()   
    while not file_location_is_valid(file_location):
        print_message('File location is not valid')
        file_location = _get_file_location()
       
    delimiter = _get_delimiter()
    
    header_included = _get_header_included()
    while not header_included_is_valid(header_included):
        print_message('Please enter true or false for header included')
        header_included = _get_header_included()
    
    return InputArgs(file_location=file_location, delimiter=delimiter, header_included=header_included)


def _get_file_location() -> str:
    return print_message_and_get_input('File location: ')


def _get_delimiter() -> str:
    return print_message_and_get_input(f'Line delimiter(default {DEFAULT_DELIMITER}): ')


def _get_header_included() -> str:
    return print_message_and_get_input(f'Header included(default {DEFAULT_HEADER_INCLUDED}): ')


if __name__ == "__main__":
    run()
