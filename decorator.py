from time import time, perf_counter

def delta_time(n):
    def count_elapsed_time(f):
       
        def w(*args, **kwargs):
            # Start counting.
            start_time = perf_counter()
            # Take the original function's return value.
            ret = f(*args, **kwargs)
            # Calculate the elapsed time.
            elapsed_time = (perf_counter()) - start_time
            print(n+"--> Tardo: %.8f Seconds."% elapsed_time)
            return ret
        
        return w
    return count_elapsed_time