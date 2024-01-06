'''
alphabet = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'
    }
'''

def digital_decipher(m, k):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    result = ""
    key = str(k)
    key = [int(digit) for digit in key]
    
    return result

f = digital_decipher([20, 12, 18, 30, 21], 1939)
g = digital_decipher([14, 30, 11, 1, 20, 17, 18, 18], 1990)
h = digital_decipher([6, 4, 1, 3, 9, 20], 100)

print(f)
print(g)
print(h)

...
