from typing import List

def should_i_be_tired(daily_schedule: List[List[str]]) -> bool:
    """Return True if total driving time > 9 hours in the daily schedule."""

if __name__ == "__main__":
    arr = [
        ["7:00-10:30", "Drive"],
        ["10:30-10:45", "Rest"],
        ["10:45-11:45", "Drive"],
        ["11:45-12:15", "Rest"],
        ["12:15-16:45", "Drive"],
        ["16:45-20:15", "Work"]
    ]
    print(should_i_be_tired(arr))
