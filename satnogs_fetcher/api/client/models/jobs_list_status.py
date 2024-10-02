from enum import Enum


class JobsListStatus(str, Enum):
    BAD = "bad"
    FAILED = "failed"
    FUTURE = "future"
    GOOD = "good"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)