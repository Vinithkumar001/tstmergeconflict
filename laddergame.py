import queue
def word_ladder(start_word, target_word, dictionary):


  q = queue.Queue()
  print(q)
  q.put(start_word)
  
  visited = set()
  visited.add(start_word)

  while not q.empty():
    current_word = q.get()
    if current_word == target_word:
      return [current_word]

    for next_word in dictionary.copy():  # Make a copy to avoid modifying while iterating
            if is_one_letter_apart(word, next_word):
                dictionary.remove(next_word)
                queue.append((next_word, ladder + [next_word]))

    

  return []


def main():
  start_word = input("Enter the start word: ")
  target_word = input("Enter the target word: ")
  dictionary = input("Enter the dictionary: ").split(",")

  word_ladder_list = word_ladder(start_word, target_word, dictionary)
  if word_ladder_list:
    print("The shortest word ladder from {} to {} is:".format(start_word, target_word))
    for word in word_ladder_list:
      print(word)
  else:
    print("There is no word ladder from {} to {}.".format(start_word, target_word))
main()
