from dataclasses import dataclass


@dataclass
class ParserArgs:
    delimiter: str
    header_included: bool
    

def parse_line(line: str, parser_args: ParserArgs) -> list[str]:
    fields = line.split(parser_args.delimiter)
    
    return fields
    