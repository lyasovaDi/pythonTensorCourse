import datetime


def func_log(file_log='log.txt'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(file_log, 'a') as f:
                f.write(f"{func.__name__} вызвана {datetime.now().strftime('%d.%m %H:%M:%S')}\n")
            return func(*args, **kwargs)

        return wrapper

    return decorator

