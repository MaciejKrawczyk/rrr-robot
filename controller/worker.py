import time


def worker_process(queue):
    while True:
        if not queue.empty():
            command = queue.get()
            print(f"Processing command: {command}")
            time.sleep(1)  # Simulate a task
            print(f"finished processing command {command}")
        else:
            time.sleep(0.1)  # Reduce CPU usage
