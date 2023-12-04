def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please provide a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def compareTo(s1, s2):
    if not s1 and not s2:
        return 0
    elif not s1:
        return -1
    elif not s2:
        return 1
    else:
        if s1[0] < s2[0]:
            return -1
        elif s1[0] > s2[0]:
            return 1
        else:
            return compareTo(s1[1:], s2[1:])

# Example Usage
if __name__ == "__main__":
    # Fibonacci Sequence
    print("Fibonacci Sequence:")
    for i in range(1, 10):
        print(f"fibonacci({i}): {fibonacci(i)}")

    # Euclid's GCD Algorithm
    print("\nEuclid's GCD Algorithm:")
    print("gcd(48, 18):", gcd(48, 18))
    print("gcd(60, 48):", gcd(60, 48))
    print("gcd(17, 5):", gcd(17, 5))

    # String Comparison
    print("\nString Comparison:")
    print('compareTo("apple", "banana"):', compareTo("apple", "banana"))
    print('compareTo("banana", "apple"):', compareTo("banana", "apple"))
    print('compareTo("apple", "apple"):', compareTo("apple", "apple"))
