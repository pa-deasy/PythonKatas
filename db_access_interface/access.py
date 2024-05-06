from typing import Protocol


class ReadAccess(Protocol):
    def read(self) -> str:
        ...
        

class WriteAccess(Protocol):
    def write(self, object: str) -> str:
        ...

 
class DeleteAccess(Protocol):
    def delete(self, id: int) -> str:
        ...
        

class ReadOnlyUser:
    def read(self) -> str:
        return 'Read only read'
    

class AdminUser:
    def read(self) -> str:
        return 'Admin read'
    
    def write(self, object: str) -> str:
        return f'Admin write {object}'
    

class SuperUser:
    def read(self) -> str:
        return 'Super read'
    
    def write(self, object: str) -> str:
        return f'Super write {object}'
    
    def delete(self, id: int) -> str:
        return f'Super delete {id}'
    
    
class DB:
    def read(self, read_access: ReadAccess) -> str:
        return read_access.read()
    
    def write(self, write_access: WriteAccess, object: str) -> str:
        return write_access.write(object)
        
    def delete(self, delete_access: DeleteAccess, id: int) -> str:
        return delete_access.delete(id)