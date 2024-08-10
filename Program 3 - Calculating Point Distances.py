# written by Santosh Ramesh
# last modified October 26th, 2021

# worked with Junsu Lee and Tanya Bihari to understand abstract program logical structure 

import heapq # Hint: use Python's priority queue class, heapq.

class Node:
    def __init__(self, count, children):
        self.count    = count
        self.children = children
        
    def is_leaf(self):
        return False
        
    def __lt__(self, other):
        return self.count < other.count
    def __eq__(self, other):
        return self.count == other.count
        
class LeafNode(Node):
    def __init__(self, symbol, count):
        super().__init__(count, [])
        self.symbol = symbol
        
    def is_leaf(self):
        return True
class HuffmanCode:
    def __init__(self, F):
        self.C = dict()
        self.T = None

        alphabet = []
        heapq.heapify(alphabet)

        # setting self.T
        for i in F:
            new_leaf = LeafNode(i, F[i])
            heapq.heappush(alphabet, new_leaf)
            # print(new_leaf.symbol, " ", new_leaf.count)
        
        while(len(alphabet) > 1):
            node_one = heapq.heappop(alphabet)
            node_two = heapq.heappop(alphabet)

            total = node_one.count + node_two.count
            new_node = Node(total, (node_one, node_two))

            heapq.heappush(alphabet, new_node)
        
        self.T = heapq.heappop(alphabet)        

        # setting self.C
        alphabet = []
        alphabet.append(self.T)
        coder = ['']

        # DFS algorithm to assign codes for each character symbol
        while len(alphabet) != 0:
            current = alphabet.pop()
            alphabet_code = coder.pop()

            if current.is_leaf():
                self.C[current.symbol] = alphabet_code
            else:
                alphabet.append(current.children[0])                
                alphabet.append(current.children[1])

                coder.append(alphabet_code + '0')
                coder.append(alphabet_code + '1')
        
    def encode(self, m):
        """
        Uses self.C to encode a binary message.
.    
        Parameters:
            m: A plaintext message.
        
        Returns:
            The binary encoding of the plaintext message obtained using self.C.
        """

        encoded = ""
        for i in m:
            encoded = encoded + self.C[i]

        return encoded

    def decode(self, c):
        """
        Uses self.T to decode a binary message c = encode(m).
.    
        Parameters:
            c: A message encoded in binary using self.encode.
        
        Returns:
            The original plaintext message m decoded using self.T.
        """

        decoded = ""
        counter = 0
        current = self.T 

        while (len(c) > counter):
            value = c[counter]
            counter = counter + 1

            if value == "0":
                current = current.children[0]
            elif value == "1":
                current = current.children[1]
            
            if current.is_leaf() == True:
                decoded = decoded + current.symbol
                current = self.T

        return decoded
        
def get_frequencies(s):
    """
    Computes a frequency table for the input string "s".
    
    Parameters:
        s: A string.
        
    Returns:
        A frequency table F such that F[c] = (# of occurrences of c in s).
    """
    F = dict()
    
    for char in s:
        if char in F:
            F[char] += 1
        else:
            F[char] = 1       
    return F

# testing code functionality
message = "oregon state rules"
F = {'F': 1, 'o': 92, 'u': 21, 'r': 79, ' ': 275, 's': 43, 'c': 31, 'e': 165, 'a': 102, 'n': 76, 'd': 58, 'v': 24, 'y': 10, 'g': 27, 'f': 26, 't': 124, 'h': 80, 'b': 13, 'i': 65, ',': 22, 'w': 26, 'L': 1, 'p': 15, 'l': 41, 'm': 13, 'q': 1, '.': 10, '\n': 4, 'N': 1, 'W': 2, '-': 15, 'I': 3, 'B': 1, 'T': 2, 'k': 3, 'G': 1}
test = HuffmanCode(F)

print("encoding dictionary: ", "\n", F)
print("\n")
print(message)
print(test.encode(message))
print(test.decode(test.encode(message)))