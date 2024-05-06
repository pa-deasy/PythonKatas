from os import path


DEFAULT_DELIMITER = ','
DEFAULT_HEADER_INCLUDED = True


def file_location_is_valid(file_location: str) -> bool:
    return path.isfile(file_location)


def map_delimiter(delimiter: str) -> str:
    if delimiter:
        return delimiter
    
    else:
        return DEFAULT_DELIMITER

def header_included_is_valid(header_included: str) -> bool:
    if not header_included or header_included.lower() in ['true', 'false']:
        return True
    else:
        return False


def map_header_included(header_included: str) -> bool:
    if header_included.lower() == 'true':
        return True
    elif not header_included:
        return DEFAULT_HEADER_INCLUDED
    else:
        return False