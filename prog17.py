#. Using range(1,101), make three list,one containing all even numbers one containing all odd numbersOne containing only prime numbers.
def is_prime(n):
 if n < 2:
  return False
 for i in range(2, int(n**0.5) + 1):
  if n % i == 0:
   return False
 return True
even_numbers = list(range(2, 101, 2))
odd_numbers = list(range(1, 101, 2))
prime_numbers = [i for i in range(2, 101) if is_prime(i)]
print("List of even numbers from 1 to 100:", even_numbers)
print("List of odd numbers from 1 to 100:", odd_numbers)
print("List of prime numbers from 1 to 100:", prime_numbers)