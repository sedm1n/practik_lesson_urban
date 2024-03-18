def min_value(digits):
    digits=sorted(set(digits))

    return int("".join(str(sim) for sim in digits))


print(min_value([4, 8, 1, 4]))