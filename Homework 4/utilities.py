def time_representation(time_ms: int) -> str:
    """Converts miliseconds to hours and minutes."""
    time_h = time_ms / (1000 * 60 * 60)
    result_time_h = int(time_h)
    result_time_m = int((time_h - result_time_h) * 60)
    return f"The total time is {result_time_h}h {result_time_m}m"