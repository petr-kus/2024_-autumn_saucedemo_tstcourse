import time
import logging

class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.time()
        logging.info("Timer started")
        return self.start_time

    def stop(self):
        self.end_time = time.time()
        logging.info("Timer stopped")
        return self.end_time

    def get_duration(self):
        if self.start_time is None or self.end_time is None:
            raise ValueError("Timer must be started and stopped first")
        duration = self.end_time - self.start_time
        logging.info(f"Duration: {duration:.2f} seconds")
        return duration

    def verify_duration(self, max_seconds):
        duration = self.get_duration()
        assert duration <= max_seconds, f"Operation took too long: {duration:.2f} seconds (maximum allowed: {max_seconds} seconds)"
