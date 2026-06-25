import matplotlib.pyplot as plt
 
plt.style.use('dark_background')

def label_for(char):
    if char == ' ':
        return "' '"
    if char == '\n':
        return "NL"
    return char
def plot_frequencies(frequencies, filename="frequency_chart.png"):
    sorted_items= frequencies.most_common()
    chars = [label_for(item[0]) for item in sorted_items]
    counts = [item[1]for item in sorted_items]
    plt.figure(figsize=(10,5))
    plt.bar(chars, counts)
    plt.xlabel("Character")
    plt.ylabel("Frequency")
    #plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
def plot_size_comparison(ascii,fixed_length,hoffman,gzip_compressed, filename = "Size comparison"):
    labels = ["Ascii (8-bit)","minimum fixed-length","Huffman","gzip"]
    sizes = [ascii,fixed_length,hoffman,gzip_compressed]
    plt.figure(figsize=(8, 5))
    plt.bar(labels, sizes, color=["#888888","#4a90d9","#50b87f","#946236"],width=0.4)
    plt.ylabel("Size (bits)")
    plt.title("Encoding Size comparison")
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()


