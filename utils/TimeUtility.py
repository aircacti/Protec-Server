import time

class TimeUtility:
    @staticmethod
    def current_time_ms() -> int:
        """
        Returns current time in milliseconds since Unix epoch.
        """
        return int(time.time() * 1000)
