def get_maximum_width_of_vehicles(widths: list[int], access_points: list[list[int]]) -> list[int]:
    vehicle_widths: list[int] = []
    
    for access_point in access_points:
        entry = access_point[0]
        exit = access_point[1] + 1
        segment_widths = widths[entry:exit]
        vehicle_widths.append(min(segment_widths))
        
    return vehicle_widths
