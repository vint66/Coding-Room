# Decorator
import functools

def triple(func):
    @functools.wraps(func)
    def wrapper_triple(*args, **kwargs):
        print(f"Tripled {func.__name__!r}")
        value = func(*args, **kwargs)
        return value * 3
    return wrapper_triple

@triple
def knock():
    return "Penny! "

print(knock())


# Decorator with arguments
def tags(tag):
    def decorator(func):
        @functools.wraps(func)
        def wrapper_decorator(*args, **kwargs):
            return f"<{tag}>{func(*args, **kwargs)}</{tag}>"
        return wrapper_decorator
    return decorator

@tags("p")
def get_text(name):
    return "Hello "+name

print(get_text("test"))
