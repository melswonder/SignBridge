#!/usr/bin/python3

def example_basic_types():
    a_int = 10
    b_float = 3.14
    c_str = "Hello"
    d_bool = True
    e_list = [1, 2, 3]
    f_dict = {"key": "value"}
    g_tuple = (1, 2)
    h_set = {1, 2, 3}
    print(f"int: {a_int}, float: {b_float}, str: {c_str}, bool: {d_bool}")
    print(f"list: {e_list}, dict: {f_dict}, tuple: {g_tuple}, set: {h_set}")

class ExampleClass:
    def __init__(self, value):
        self.value = value
    
    def show_value(self):
        print(f"Value is: {self.value}")

def example_if_else(x):
    if x > 0:
        print("Positive")
    elif x == 0:
        print("Zero")
    else:
        print("Negative")

def example_while(n):
    count = 0
    while count < n:
        print(f"Count: {count}")
        count += 1

def example_for(lst):
    for item in lst:
        print(f"Item: {item}")

def example_do_while(n):
    count = 0
    while True:
        print(f"Do-While Count: {count}")
        count += 1
        if not (count < n):
            break

def example_switch(case):
    switcher = {
        1: "One",
        2: "Two",
        3: "Three"
    }
    print(switcher.get(case, "Default"))

def example_try_except(x, y):
    try:
        result = x / y
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero")

def main():
    example_basic_types()
    obj = ExampleClass(42)
    obj.show_value()
    example_if_else(1)
    example_if_else(0)
    example_if_else(-1)
    example_while(3)
    example_for(["a", "b", "c"])
    example_do_while(3)
    example_switch(2)
    example_switch(5)
    example_try_except(10, 2)
    example_try_except(10, 0)

if __name__ == "__main__":
    main()
