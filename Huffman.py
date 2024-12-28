class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

def count_frequencies(text):
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

def build_huffman_tree(text):
    freq_counter = count_frequencies(text)
    priority_queue = [Node(char, freq) for char, freq in freq_counter.items()]
    
    priority_queue.sort(key=lambda x: x.freq)
    
    while len(priority_queue) > 1:
        left = priority_queue.pop(0)
        right = priority_queue.pop(0)
        
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        priority_queue.append(merged)
        
        priority_queue.sort(key=lambda x: x.freq)
    
    return priority_queue[0]  

def generate_huffman_codes(node, current_code, codes):
    if node is None:
        return

    if node.char is not None:
        codes[node.char] = current_code
        return

    generate_huffman_codes(node.left, current_code + "0", codes)
    generate_huffman_codes(node.right, current_code + "1", codes)

def huffman_encode(text, codes):
    return ''.join(codes[char] for char in text)

def huffman_decode(encoded_text, tree):
    decoded_text = []
    current_node = tree
    for bit in encoded_text:
        current_node = current_node.left if bit == "0" else current_node.right
        
        if current_node.char is not None:
            decoded_text.append(current_node.char)
            current_node = tree
    
    return ''.join(decoded_text)

if __name__ == "__main__":
    text = "greedy huffman algorithm"
    print(f"Original text: {text}")
    
    root = build_huffman_tree(text)
    
    codes = {}
    generate_huffman_codes(root, "", codes)
    print(f"Huffman Codes: {codes}")
    encoded_text = huffman_encode(text, codes)
    print(f"Encoded text: {encoded_text}")
    decoded_text = huffman_decode(encoded_text, root)
    print(f"Decoded text: {decoded_text}")
