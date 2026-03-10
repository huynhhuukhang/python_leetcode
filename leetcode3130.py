MOD = 10**9 + 7

def count_stable_arrays(zero, one, limit):
    total_len = zero + one
    if zero == 0 or one == 0:
        if total_len > limit:
            return 0
        else:
            return 1
    if limit >= total_len:
        return combination_mod(total_len, zero, MOD)
    return combination_mod(total_len, zero, MOD)
def combination_mod(n, k, mod):
    if k < 0 or k > n:
        return 0
    fact = [1] * (n+1)
    for i in range(1, n+1):
        fact[i] = fact[i-1] * i % mod
    
    inv_fact = [1] * (n+1)
    inv_fact[n] = pow(fact[n], mod-2, mod) 
    for i in range(n-1, -1, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % mod
    
    return fact[n] * inv_fact[k] % mod * inv_fact[n-k] % mod
if __name__ == "__main__":
    zero = int(input("Nhập số lượng 0: "))
    one = int(input("Nhập số lượng 1: "))
    limit = int(input("Nhập limit: "))
    
    result = count_stable_arrays(zero, one, limit)
    print(f"Số mảng nhị phân stable: {result}")