from collections import deque

# Function to check if two words are only one letter apart
def is_one_letter_apart(word1, word2):
    a=tuple(zip(word1, word2))
    #print(a)

    diff_count = sum(c1 != c2 for c1, c2 in a)

    return diff_count == 1
   
# Function to find the shortest word ladder using BFS
def find_word_ladder(start_word, target_word, word_list):
    word_list = set(word_list)
    queue = deque([(start_word, [start_word])])

    while queue:

    
    
        word, ladder = queue.popleft()
        
        if word == target_word:
            return ladder
        
        for next_word in word_list.copy():  # Make a copy to avoid modifying while iterating
            if is_one_letter_apart(word, next_word):
                word_list.remove(next_word)
                
    
                queue.append((next_word, ladder + [next_word]))
                print(queue)
                
    

# Get user input for start word, target word, and word list
start_word = input("Enter the start word: ")
target_word = input("Enter the target word: ")
word_list = input("Enter a list of words (comma-separated): ").split(",")

# Find the word ladder
ladder = find_word_ladder(start_word, target_word, set(word_list))

# Print the word ladder
if ladder:
    print("Word ladder found:")
    print(' -> '.join(ladder))
else:
    print("No word ladder found.")
