from object_oriented_design.parking_lot import ParkingLot, Vehicle, Size


def test_available_spaces_when_spaces_available_then_returns_correct_count():
    parking_lot = ParkingLot(stall_count=10)
    
    assert parking_lot.available_spaces() == 10
    
    
def test_park_in_when_available_then_sets_occupied():
    parking_lot = ParkingLot(stall_count=10)
    vehicle = Vehicle(plate='YCS358', size=Size.Small)
    
    assert parking_lot.stalls[1].occupied is False
    parking_lot.park_in(1, vehicle)
    assert parking_lot.stalls[1].occupied is True
    assert parking_lot.stalls[1].vehicle.plate == vehicle.plate
    
    
def test_park_in_when_available_but_too_small_then_does_not_set_occupied():
    parking_lot = ParkingLot(stall_count=10)
    vehicle = Vehicle(plate='YCS358', size=Size.Large)
    
    assert parking_lot.stalls[1].occupied is False
    parking_lot.park_in(1, vehicle)
    assert parking_lot.stalls[1].occupied is False
    

def test_leave_from_when_available_then_sets_occupied():
    parking_lot = ParkingLot(stall_count=10)
    vehicle = Vehicle(plate='YCS358', size=Size.Small)
    
    assert parking_lot.stalls[1].occupied is False
    parking_lot.park_in(1, vehicle)
    assert parking_lot.stalls[1].occupied is True
    leaving = parking_lot.leave_from(1)
    assert leaving.plate == vehicle.plate
    assert parking_lot.stalls[1].occupied is False