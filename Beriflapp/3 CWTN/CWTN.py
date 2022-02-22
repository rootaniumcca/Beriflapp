# Convert words to numbers.

Beriflapp = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

# Initializing string
Beriflapp_str = "zero zero seven"
  
# Printing original string
print("The original string is : " + Beriflapp_str)
  
# Convert numeric words to numbers
# Using join() + split()
res = ''.join(Beriflapp[ele] for ele in Beriflapp_str.split())
  
# Printing result 
print("The string after performing replace : " + res) 