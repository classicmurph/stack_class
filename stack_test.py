from stack import *
from nose.tools import raises
import random


def test_creating_new_stack_is_empty():
    stack = Stack(0)
    assert stack.is_empty()

def test_creating_new_stack_has_capacity():
    stack = Stack(2)
    assert stack.capacity == 2

@raises(InvalidCapacityError)
def test_creating_new_stack_with_neg_capacity_raises_error():
    stack = Stack(-1)

def test_push_adds_item():
    stack = Stack(100)
    stack.push(5)
    assert not stack.is_empty()

@raises(StackOverflowError)
def test_push_over_capacity_raises_error():
    stack = Stack(0)
    assert stack.push('10')

def test_pop_removes_item():
    stack = Stack(100)
    stack.push(5)
    stack.pop()
    assert stack.is_empty()

@raises(StackUnderflowError)
def test_pop_on_empty_stack_raises_error():
    stack = Stack(0)
    assert stack.pop()

def test_stack_can_return_length():
    stack = Stack(100)
    for _ in range(10):
        stack.push(random.randint)
    assert stack.length() == 10

def test_peek_returns_stack_values():
    stack = Stack(100)
    for _ in range(3):
        stack.push(0)
    assert stack.peek() == [0, 0 , 0]

def test_peek_on_empty_stack_returns_none():
    stack = Stack(1)
    assert not stack.peek()

def test_find_returns_correct_value():
    stack = Stack(3)
    stack.push(1)
    stack.push('five')
    stack.push([])
    assert stack.find('five') == 'five'
    assert stack.length() == 2
