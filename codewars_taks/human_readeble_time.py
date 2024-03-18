def make_readable(seconds):
    hour, min = 0, 0

    # if seconds >= 60:
    #     min = seconds // 60
    #     seconds = seconds % 60
    #     if min >= 60:
    #         hour = min // 60
    #         min = min % 60

    return f"{hour:02}:{min:02}:{seconds:02}"

print(make_readable(6399))