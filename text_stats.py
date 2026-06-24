from collections import Counter
import math as m

def get_char_frequencies(contents):
    return Counter(contents)

def get_probabilities(frequencies):
    total = sum(frequencies.values())
    probabilities = {}
    for char,count in frequencies.items():
        probabilities[char] = count/total
    return probabilities

def calculate_entropy(probabilities):
    entropy = 0
    for i in probabilities.values():
        entropy += -1*(i*m.log2(i))
    return entropy

def find_fixed_bit_length_bits_per_char(frequencies):
    length = len(frequencies)
    bits_per_char = int(m.ceil(m.log2(length)))
    return bits_per_char

def find_total_fixed_bit_file_size(bits_per_char,content):
    total_size = bits_per_char * len(content)
    return total_size
