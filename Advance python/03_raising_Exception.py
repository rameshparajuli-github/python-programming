def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("Invalid ")     # Showing error use of raising
a=increment('dnajsfd2342')
print(a)

