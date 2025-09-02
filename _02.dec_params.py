#Decorators having parameters
#
def decor(func):
    def wrapper(*args, **kwargs):
        bef = f"before calling func {func.__name__}-validations"
        res = func(*args, **kwargs)
        aft = f"after calling func {func.__name__}- manipulations"
        return bef,res,aft
    return wrapper
@decor
def hello():
    return "from hello function"
print(hello())