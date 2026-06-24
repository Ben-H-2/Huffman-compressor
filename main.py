import text_stats as stats

filepath = "sample_texts/repetitive_text.txt"
with open(filepath, "r") as f:
        contents = f.read()

print(f"file name is: {filepath}\n")
frequencies = stats.get_char_frequencies(contents)
print(f"frequencies of characters are: {frequencies}\n")
probabilities = stats.get_probabilities(frequencies)
#print(f"probabilities are: {probabilities:.3f}\n")
entropy = stats.calculate_entropy(probabilities)
print(f"Entropy for {filepath} is {entropy:.3f}\n")
bits_per_char = stats.find_fixed_bit_length_bits_per_char(frequencies)
print(f"bits per character when fixed bit length: {bits_per_char}")
total_fixed_bit_size = stats.find_total_fixed_bit_file_size(bits_per_char,contents)
print(f"therefore total bit size would be: {total_fixed_bit_size}")