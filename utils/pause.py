import time

def pause(interval, task, message_done=None):
    max_length = 0

    for i in range(interval, 0, -1):
        log_message = f"Waiting for the page to {task}: {i} seconds remaining"
        print(log_message, end="\r")

        if len(log_message) > max_length:
            max_length = len(log_message)

        time.sleep(1)
    
    # Print the message after the countdown with at least more than LENGTH of the message counntdown
    print(" " * max_length, end="\r")
    if message_done:
        print(message_done)
    else:
        print(f"Page {task} completed")
