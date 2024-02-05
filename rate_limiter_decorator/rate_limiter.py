from typing import Any, Callable


class RateLimiter:
    limit: int
    invocations :int
    
    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.invocations = 0
        
    def __call__(self, func: Callable) -> Any:
        def wrapper(*args: Any, **kwds: Any) -> Any:
            if self.invocations < self.limit:
                self.invocations += 1
                return func(*args, **kwds)
            else:
                return 'Limit Reached'
        return wrapper


@RateLimiter(3)
def get_dummie_data() -> str:
    return 'Dummie Response'