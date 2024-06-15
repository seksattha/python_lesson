def fact(n):
    f = 1
    if n != 0:
        for i in range(1, n + 1):
            f = f * i
    else:
        f = 1

    return f

def permut(n, k):
    return fact(n) / fact(n - k)

def combi(n, k):
    return fact(n) / (fact(k) * fact(n - k))

if __name__ == '__main__':
    result_fact = fact(5)
    print(f"Factorial of 5: {result_fact}")

    result_permut = permut(3, 5)
    print(f"Permutations of 3 out of 5: {result_permut}")

    result_combi = combi(3, 5)
    print(f"Combinations of 3 out of 5: {result_combi}")
