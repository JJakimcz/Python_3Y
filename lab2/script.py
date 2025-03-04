def prime_selector(numbers):
    for x in numbers:
        for i in range(2, x):
            if x % i == 0:
                break
            else:
                print(x)
                break

def round_numbers(numbers, threshold):
    for x in numbers:
        if x < threshold:
            print(round())
        else:
            print(x)

def longest_increasing_subsequence(sequence):
    temp = num(1)
    for num in sequence:
        temp_sequence = []
        if num > temp:
            temp_sequence.append(num)
            temp = num
        else:
            temp_sequence = []
            temp = num



def is_balanced(expression):
    return

def transposition_cipher(text, key):
    return

def fibonacci_generator(n):
    return

def most_frequent_element(data):
    return

def readability_score(text):
    return

def unique_permutations(text):
    return

def group_words_by_lenght(words):
    return

