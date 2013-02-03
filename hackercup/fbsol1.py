from collections import Counter
 
def get_beauty(string):
    string = string.lower()
 
    # Remove all characters other than letters
    string = ''.join(x for x in string if 'a' <= x <= 'z' )
 
    # Make a dictionary where the keys are letters and the values are counts
    freq = Counter(string)
 
 
    # Get the values (letter counts) and sort them in descending order
    arr = freq.values()
    arr.sort()
    arr.reverse()
 
    # 26 * (count of most common letter) + (25 * next most common) + ...
    values_and_counts = zip(range(26, 0, -1), arr)
    return sum(value * count for value, count in values_and_counts)