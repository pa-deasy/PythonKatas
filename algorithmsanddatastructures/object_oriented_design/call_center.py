from dataclasses import dataclass
from enum import Enum, IntEnum
from time import sleep
from typing import List, Optional


# 7.2 - Call Center: Imagine you have a call center with three levels of employees: respondent, manager and director.
# An incoming telephone call must be first allocated to a respondent who is free. If the respondent can't handle the call, he or she must escalate the call to a manager.
# If a manager is not free or not able to handle it, then the call should be escalated to a director.
# Design the classes and data structures for this problem. Implement a method dispatchCall() which assigns a call to the first available employee.
class Level(IntEnum):
    Respondent = 0
    Manager = 1
    Director = 2


class Employee:
    number: int
    level: Level
    busy: bool
    
    def __init__(self, number: int, level: Level) -> None:
        self.number = number
        self.level = level
        self.busy = False
        
    def can_resolve_query(self, query: str) -> bool:
        return len(query) <= 20
    
    
@dataclass
class Call:
    query: str
    resolved: str = False
    allocated_to: Optional[Employee] = None
    
    
class CallCenter:
    employees: List[Employee]
    max_level = 2
    
    def __init__(self, employees: List[Employee]) -> None:
        self.employees = employees
    
    def dispatch_call(self, call: Call) -> None:
        level_counter = 0
        
        while not call.resolved:
            level = Level(level_counter)
            call = self.assign_respondent_of(call, level)
            
            if level_counter > self.max_level:
                break
            elif call.allocated_to and call.allocated_to.can_resolve_query(call.query):
                call.resolved = True
            else:
                level_counter += 1
                call.allocated_to = None
            
        
    def get_free_employee_of(self, level: Level) -> Optional[Employee]:
        free = [e for e in self.employees if e.level == level and e.busy is False]
        return free.pop(0) if free else None
    
    def mark_busy_employee(self, employee_number: int) -> None:
        for e in self.employees:
            if e.number == employee_number:
                e.busy = True
    
    def assign_respondent_of(self, call: Call, level: Level) -> Call:
        max_tries = 2
        try_counter = 0
        while call.allocated_to is None and try_counter < max_tries:
            respondent = self.get_free_employee_of(level)
            if not respondent:
                sleep(1)
                try_counter += 1
                continue
            
            self.mark_busy_employee(respondent.number)
            call.allocated_to = respondent
            
        return call
        
        