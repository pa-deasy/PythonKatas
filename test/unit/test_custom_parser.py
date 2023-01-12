from custom_parser import ParserArgs, parse_line


def test_parse_line_when_comma_delimited_then_parsed_correctly():
    line = 'i,am,a,line'
    
    parser_args = ParserArgs(delimiter=',', header_included=False)
    
    columns = parse_line(line, parser_args)
    columns = parse_line(line, parser_args)
    
    assert len(columns) == 4
    assert columns[0] == 'i'
    assert columns[1] == 'am'
    assert columns[2] == 'a'
    assert columns[3] == 'line'
    