def before_and_after(func):
    def wrapper(*args, **kwargs):
        print("Текст, который будет выведен до вызова функции")
        result = func(*args, **kwargs)
        print("Текст, который будет выведен после вызова функции")
        return result
    return wrapper

@before_and_after
def some_function():
    print("Текст из функции")

some_function()