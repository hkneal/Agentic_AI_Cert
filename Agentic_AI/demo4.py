# Function to check prime numbers

# The function should handle edge cases like 0, 1, and negative numbers

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to count the number of vowels in each string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels("hello"))  # Expected output: 2

print(count_vowels("Simplilearn"))  # Expected output: 4

print(count_vowels("Python"))  # Expected output: 1

print(count_vowels("AI-powered coding"))  # Expected output: 7