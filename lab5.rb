require 'digest'

def gcd(a, b)
    if b == 0
        return 1, 0, a
    end
    y, x, g = gcd(b, a % b)
    return x, y - a / b * x, g
end 

def my_module(a, m)
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
        if n & 1 == 1
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
        p_ = q * r + 1
        if bin_pow(2, q * r, p_) != 1 or bin_pow(2, r, p_) == 1
            next 
        else
            break 
        end
    end 

    while true
        x = rand(1...(p_ - 1))
        g = bin_pow(x, r, p_)
        if g == 1
            next 
        else
            break
        end
    end 

    d = rand(1...(q - 1))
    e = bin_pow(g, d, p_)
    return p_, q, g, e, d
end


def sign(p_, q, g, d, message)
    m = Digest::SHA256.hexdigest message
    m = Integer(m, 16)
    k = rand(1...(q - 1))
    r = bin_pow(g, k, p_)
    s = my_module(k, q) * ((m - d * r ) % q + q) % q 
    return r, s
end

def verify(p_, q, g, e, r, s, message)
    if r == 0 and r >= p_ or s >= q
        return false
    end 

    m = Digest::SHA256.hexdigest message
    m = Integer(m, 16)

    if (bin_pow(e, r, p_) * bin_pow(r,s,p_)) % p_ != bin_pow(g, m, p_)
        return false
    end 

    return true
end



q = 71377667593522809398065817488727894625089268662066515584888587607032916396479
message = "Я, Маргарита Бобкова, люблю МиКОЗИ"

# puts sign(message)

p_, q, g, e, d = generate_key(q)
r, s = sign(p_, q, g, d, message)
puts verify(p_, q, g, e, r, s, message)