'''
Create a singleton decorator in the file *src/decorator.py*, using a class (not nested functions or closures).
```
Hint: we recently talked about a special method called __call__, it can make an
object act as a function.
'''


class SingletonDecorator:
    def __init__(self, cls):
        self._cls = cls
        self._instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = self._cls(*args, **kwargs)
        return self._instance

@SingletonDecorator
class SingletonClass:
    def __init__(self, value):
        self.value = value

# Creating instances of the SingletonClass using the decorator
instance1 = SingletonClass(1)
instance2 = SingletonClass(2)

# Both instances refer to the same object
print(instance1 is instance2)  # Output: True
