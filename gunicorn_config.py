import multiprocessing

bind = "0.0.0.0:5861"
workers = multiprocessing.cpu_count() * 2 + 1
