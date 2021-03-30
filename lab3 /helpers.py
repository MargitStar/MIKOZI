def get_sequence(a, c):
    length = (2 ** len(a)) - 1
    result = []

    a_copy = a.copy()
    for _ in range(length):
        result.append(a_copy[-1])

        r = 0
        for j in range(len(c)):
            r += a_copy[j] * c[j]
        r %= 2

        for j in range(len(a_copy) - 1, 0, -1):
            a_copy[j] = a_copy[j - 1]
        a_copy[0] = r

    return result


def get_geffe(n, s1, s2, s3):
    result = []
    for i in range(n):
        s1_i = s1[i % len(s1)]
        s2_i = s2[i % len(s2)]
        s3_i = s3[i % len(s3)]
        gamma = (s1_i & s2_i) ^ ((s1_i ^ 1) & s3_i)
        gamma %= 2
        result.append(gamma)
    return result
