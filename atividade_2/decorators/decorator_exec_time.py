import time
import functools

def decorator_exec_time(f):
    """
        Captura o tempo de execucao de uma dada funcao.
    """
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        f(*args, **kwargs)
        end_time = time.time()
        print(f"Tempo de execucao de {f.__name__} = {round(end_time - start_time, 2)}s")
        
    return wrapper