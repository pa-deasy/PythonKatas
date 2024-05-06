from access import DB, AdminUser, ReadOnlyUser, SuperUser
import pytest


@pytest.fixture
def db():
    return DB()


def test_db_when_read_only_user_then_can_read(db):
    user = ReadOnlyUser()
    
    assert db.read(user) == 'Read only read'
    
    
def test_db_when_admin_user_then_can_read_and_write(db):
    user = AdminUser()
    
    assert db.read(user) == 'Admin read'
    assert db.write(user, 'entity') == 'Admin write entity'
    

def test_db_when_super_user_then_can_read_and_write_and_delete(db):
    user = SuperUser()
    
    assert db.read(user) == 'Super read'
    assert db.write(user, 'entity') == 'Super write entity'
    assert db.delete(user, 101) == 'Super delete 101'