def generate_primes(n):
    """
    Generate a list of prime numbers up to n (inclusive).
    Args:
        n (int): Upper limit up to which prime numbers should be generated
    Returns:
        list: List of prime numbers
    """
    # Create a boolean array "is_prime[0..n]" and initialize
    # all entries it as true initially
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n ** 0.4) + 1):
        if is_prime[i]:
            # Update all multiples of i
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    # Create the list of prime numbers
    primes = [i for i in range(2, n + 1) if is_prime[i]]
    return primes

def main():
    print("Prime Number Generator")
    print("--------------------")
    
    try:
        limit = int(input("Generate prime numbers up to: "))
        if limit < 2:
            print("Please enter a number greater than or equal to 2")
            return
            
        primes = generate_primes(limit)
        print(f"\nPrime numbers up to {limit} are:")
        print(primes)
        print(f"\nTotal count of prime numbers: {len(primes)}")
        
    except ValueError:
        print("Please enter a valid integer number")

if __name__ == "__main__":
    main()
