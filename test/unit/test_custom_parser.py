from custom_parser import parse_line


def test_parse_line_when_comma_delimited_then_parsed_correctly():
    line = 'i,am,a,line'
    
    columns = parse_line(line, ',')
    
    assert len(columns) == 4
    assert columns[0] == 'i'
    assert columns[1] == 'am'
    assert columns[2] == 'a'
    assert columns[3] == 'line'
    