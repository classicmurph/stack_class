# stack_class

This is my implementation of a Stack class in Python, for the purposes of practicing TDD.

The stack class supports the following methods:

* capacity
* len()
* is_empty()
* push(value)
* pop()
* peek()
* find()


Additionally, the following errors must be raised:

* Throw a Stack Overflow error if you try push pasts it's capacity.
* Throw a Stack Underflow error if you try pop an empty stack.
* Throw an Invalid Capacity if you try create a stack with a negative capacity.
* An empty Stack must either throw an Empty error or return None when you peek() into it.

find() will return None or -1 when you try find a value in the stack that does not exist.
