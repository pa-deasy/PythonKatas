def select_stations(stations: dict[str, set[str]], states_needed: set[str]) -> set[str]:
    selected_stations: set[str] = set()
    
    while states_needed:
        best_station = None
        states_covered = set()
        
        for station, states in stations.items():
            covered = states_needed & states
        
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
            
        states_needed -= states_covered
        selected_stations.add(best_station)
        
    return selected_stations
