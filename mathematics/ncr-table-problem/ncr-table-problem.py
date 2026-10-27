def solve(n):
    modulo = 1000000000
    result = []
    original_result = []

    result.append(1)
    original_result.append(1)
    for i in range(n):
        last = original_result[-1]
        if n > 0: 
            numerator = (last * (n-i))
            denominator = (i + 1)
            new_value = numerator // denominator
            original_result.append(new_value)
            final_value = new_value % modulo
            result.append(final_value)
    return result

def main():
    arr = solve(819)
    for x in arr:
        print (x)

main()