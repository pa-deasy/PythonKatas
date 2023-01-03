def flight_path_from(flights: dict[str, str]) -> str:
    arrivals = set(flights.keys())
    departures = set(flights.values())
    start = list(arrivals - departures)
    
    if len(start) > 1:
        raise Exception('No clear original departure')
    
    arrival_flight = start[0]
    path = arrival_flight
    while(flights.get(arrival_flight)):
        departure_flight = flights.get(arrival_flight)
        path += f' -> {departure_flight}'
        arrival_flight = departure_flight
        
    return path
