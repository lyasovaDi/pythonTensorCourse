import datetime

file_log = "log.txt"


def func_log(func):
    def wrapper():
        with open(file_log, 'a') as f:
            f.write(f"{func.__name__} caused by {datetime.datetime.now().strftime('%d.%m %H:%M:%S')}\n")
        return func

    return wrapper()


@func_log
def print_hello():
    print("hello")
