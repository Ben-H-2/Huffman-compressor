import text_stats as stats
import huffman as huff
import compression as c
import visualiser as v

filepath = "sample_texts/longer_book_excerpt.txt"
with open(filepath, "r") as f:
        contents = f.read()

#print(f"file name is: {filepath}\n")
frequencies = stats.get_char_frequencies(contents)
print(f"frequencies of characters are: {frequencies}\n")
probabilities = stats.get_probabilities(frequencies)
#print(f"probabilities are: {probabilities:.3f}\n")
entropy = stats.calculate_entropy(probabilities)
print(f"Entropy for {filepath} is {entropy:.3f}\n")
bits_per_char = stats.find_fixed_bit_length_bits_per_char(frequencies)
#print(f"bits per character when fixed bit length: {bits_per_char}")
total_fixed_bit_size = stats.find_total_fixed_bit_file_size(bits_per_char,contents)
print(f"size of file with mininum width encoding: {c.format_bits_to_bytes(total_fixed_bit_size)}")
root = huff.create_huffman_tree(frequencies)
codes = huff.generate_codes(root)
#print(f"\nthe bit string for each char is: {codes}")
encoded_file = huff.build_file(contents,codes)
ascii_size_of_file = stats.find_total_fixed_bit_file_size(8,contents)
gzip_size = c.gzip_compression_size_bits(contents)
print(f"ascii size of file would be: {c.format_bits_to_bytes(ascii_size_of_file)}")
print(f"size of huffman-compressed file is: {c.format_bits_to_bytes(len(encoded_file))}")
v.plot_frequencies(frequencies)
v.plot_size_comparison(ascii_size_of_file,total_fixed_bit_size,gzip_size,len(encoded_file))