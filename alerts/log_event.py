def log_event(message):
    with open("event_log.txt", "a") as log_file:
        log_file.write(message + "\n")
