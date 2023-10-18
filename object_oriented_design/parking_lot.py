from dataclasses import dataclass
from enum import IntEnum
import random
from typing import Dict, List, Optional


# 7.4 - Parking Lot: Design a parking lot using object oriented principles.
class Size(IntEnum):
    Small = 0
    Regular = 1
    Large = 2
    

@dataclass
class Vehicle:
    plate: str
    size: Size


@dataclass
class Stall:
    number: int
    size: Size
    occupied: bool = False
    vehicle: Optional[Vehicle] = None


class ParkingLot:
    stalls = Dict[int, Stall]
    
    def __init__(self, stall_count: int) -> None:
        self.stalls = {}
        for n in range(1, stall_count + 1):
            if n <= stall_count / 3:
                size_int = 0
            elif n <= (stall_count / 3) * 2:
                size_int = 1
            else:
                size_int = 2
                
            size = Size(size_int)
            self.stalls[n] = Stall(number=n, size=size)
            
    def available_spaces(self) -> int:
        return len([s for s in self.stalls.values() if s.occupied is False])
    
    def park_in(self, stall_number: int, vehicle: Vehicle) -> None:
        stall = self.stalls[stall_number]
        
        if stall.occupied:
            print(f'Stall {stall_number} is occupied')
        elif int(stall.size) < int(vehicle.size):
            print(f'Stall {stall_number} is too small')
        else:
            stall.occupied = True
            stall.vehicle = vehicle
            self.stalls[stall_number] = stall
            
    def leave_from(self, stall_number: int) -> Optional[Vehicle]:
        stall = self.stalls[stall_number]
        
        if not stall.occupied:
            print(f'Stall {stall_number} is not occupied')
            return None
        else:
            vehicle = stall.vehicle
            stall.occupied = False
            stall.vehicle = None
            self.stalls[stall_number] = stall
            return vehicle
        