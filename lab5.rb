puts rand(1..100)

def gcd(a, b)
    if b == 0
        return Tuple(1, 0, a)
    end
    y, x, g = gcd(b, a % b)
    return Tuple(x, y - a / b * x, g)
end 

def module(a, m)
    x, y, g = gcd(a, m)
    if g != 1
        return "Error"
    end
    x = (x % m + m) % m
    return x
end

def bin_pow(a, n, m)
    result = 1

    while n > 0
        if n & 1
            result *= a 
            result %= m
            n -= 1
        else
            a *= a
            a %= m 
            n >>= 1
        end
    end 
    return result
end

def generate_key(q)
    while true
        t = 4 * (q + 1) - 1
        r = rand(1...t)
        p = q * R + 1
        if bin_pow(2, q * r, p) != 1 or bin_pow(2, r, p) == 1
            next 
        else
            break 
        end
    end 

    while true
        x = rand(1...(p - 1))
        g = bin_pow(x, r, p)
        if g == 1
            next 
        else
            break
        end
    end 

    d = rand(1...(q - 1))
    e = bin_pow(g, d, p)
end
