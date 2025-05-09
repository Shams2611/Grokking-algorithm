"""
The call stack

Each function call goes on the stack.
Returns pop off the stack.
"""

def greet(name):
    print(f"Hello {name}!")
    greet2(name)
    print("Getting ready to say bye...")
    bye()


def greet2(name):
    print(f"How are you, {name}?")


def bye():
    print("Goodbye!")


# trace the call stack
print("Watch the order of prints:")
greet("Alice")

# stack grows with each call
# then shrinks as functions return
