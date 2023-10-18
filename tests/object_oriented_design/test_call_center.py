import pytest

from object_oriented_design.call_center import Call, CallCenter, Employee, Level

@pytest.fixture
def employees():
    respondent_1 = Employee(1, Level.Respondent)
    respondent_2 = Employee(2, Level.Respondent)
    
    return [respondent_1, respondent_2]

@pytest.fixture
def call_center(employees):
    return CallCenter(employees=employees)


def test_get_free_employee_of_when_employee_free_then_returns_employee(call_center):
    free = call_center.get_free_employee_of(Level.Respondent)
    assert free.number == 1
    
    
def test_mark_busy_employee_when_marked_then_call_center_employee_is_busy(call_center):
    first_free = call_center.get_free_employee_of(Level.Respondent)
    assert first_free.number == 1
    
    call_center.mark_busy_employee(1)
    
    second_free = call_center.get_free_employee_of(Level.Respondent)
    assert second_free.number == 2
    
    
def test_assign_respondent_when_assigned_then_allocated_to_set(call_center):
    call = Call('Internet no work')
    
    allocated_call = call_center.assign_respondent_of(call, Level.Respondent)
    
    assert allocated_call.allocated_to.number == 1
    
    
def test_can_resolve_query_when_possible_then_returns_true():
    respondent_1 = Employee(1, Level.Respondent)
    
    assert respondent_1.can_resolve_query('Internet no work') is True
    
    
def test_can_resolve_query_when_not_possible_then_returns_false():
    respondent_1 = Employee(1, Level.Respondent)
    
    assert respondent_1.can_resolve_query('Internet no work right now but it used to work real good') is False
    
    
def test_dispatch_call_when_resolveable_then_resolved(call_center):
    call = Call('Internet no work')
    
    call_center.dispatch_call(call)
    
    
def test_dispatch_call_when_not_resolveable_then_not_resolved(call_center):
    call = Call('Internet no work right now but it used to work real good')
    
    call_center.dispatch_call(call)