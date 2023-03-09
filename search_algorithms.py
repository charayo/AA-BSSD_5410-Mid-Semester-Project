# Code taken from: https://www.geeksforgeeks.org/binary-search/
# Date Accessed: 03/01/2023
# License: https://www.geeksforgeeks.org/copyright-information/?ref=footer
# Author: Tapesh(tapeshdua420)
# CHANGELOG: changes to variable name: v = array




if __name__ == '__main__':
    v = [1, 3, 4, 5, 6]
    words = [
        "Hi",
        "Hello",
        "Hey",
        "Good morning",
        "Morning",
        "Good afternoon",
        "Afternoon",
        "Evening",
        "Good"
    ]
    To_Find = "good"
    binarySearch(words, To_Find)

    To_Find = "good afternoon"
    binarySearch(v, To_Find)

# This code is contributed by
