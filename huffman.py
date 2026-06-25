import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other): #allows heapq to compare them without error
        return self.freq < other.freq

def create_huffman_tree(frequencies):
    heap = []
    for char, freq in frequencies.items():
        node = Node(char, freq)
        heapq.heappush(heap,node)

    while len(heap) > 1:
        left = heapq.heappop(heap) #removes it from the list 
        right = heapq.heappop(heap)

        parent = Node(None, left.freq+right.freq) #combines the 2 deleted nodes into 1 and readds it
        parent.left = left
        parent.right = right

        heapq.heappush(heap, parent)

    return heap[0]

def generate_codes(node, current_code = "", codes = None):
    if codes is None:
        codes = {} 
    if node.char is not None:
        codes[node.char] = current_code #terminates branch if the leaf is a character
        return codes
    generate_codes(node.left, current_code + "0", codes) #branches out left and right otherwise
    generate_codes(node.right, current_code + "1", codes)

    return codes

def build_file(text,codes):
    content = ""
    for char in text:
        content += codes[char]
    return content