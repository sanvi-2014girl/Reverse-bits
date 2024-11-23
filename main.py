def reverse_bits(num):
    reversed_num = 0
    bit_size = num.bit_length()
    for i in range(bit_size):
        reversed_num <<= 1
        reversed_num |= (num & 1)
        num >>= 1
    return reversed_num
num = int(input("Enter a number: "))
reversed_num = reverse_bits(num)
print(f"Original number: {num}")
print(f"Reversed number: {reversed_num}")