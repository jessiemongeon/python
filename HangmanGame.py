import random
HANGMAN = (

    """

 ------

|     |

|

|

|

|

|

|

----------

"""

    ,

"""

 ------

|     |

|     0

|

|

|

|

|

----------

"""

   ,

"""

 ------

|     |

|     0

|     +

|

|

|

|

----------

"""

    ,

"""

 ------

|     |

|     0

|    -+

|

|

|

|

----------

"""

    ,

"""

 ------

|     |

|     0

|    -+-

|

|

|

|

----------

"""

    ,

"""

 ------

|     |

|     0

|   /-+-

|

|

|

|

----------

"""

    ,

"""

 ------

|     |

|     0

|   /-+-/

|

|

|

|

----------

"""

    ,

"""

 ------

|     |

|     0

|   /-+-/

|     |

|

|

|

----------

"""

    ,

"""

 ------

|     |

|     0

|   /-+-/

|     |

|     |

|

|

----------

"""

    ,

"""

 ------

|     |

|     0

|   /-+-/

|     |

|     |

|    |

|    |

----------

"""

    ,

"""

 ------

|     |

|     0

|   /-+-/

|     |

|     |

|    | |

|    | |

----------

"""

)



def random_word():
	with open("HangmanWords.txt", 'r') as file:
		words = file.readlines()
	index = random.randint(0, len(words) - 1)
	word = words[index].strip().upper()
	return word

def guess_letter():
	letter = raw_input("Guess a letter: ")
	return letter.strip().upper()

def generate_word_string(word, letters_guessed):
	output = []
	for letter in word:
		if letter in letters_guessed:
			output.append(letter.upper())
		else:
			output.append("_")
	return " ".join(output)


def main():
	WORD = random_word()
	letters_to_guess = set(WORD)
	correct_letters_guessed = set()
	incorrect_letters_guessed = set()
	num_guesses = 0
	print("Welcome to Jessie's Hangman Game!")
	while (len(letters_to_guess) > 0) and num_guesses < 10:
		guess = guess_letter()
		if guess in incorrect_letters_guessed or guess in correct_letters_guessed:
			print("You already guessed that letter.")
			continue
		if guess in letters_to_guess:
			letters_to_guess.remove(guess)
			correct_letters_guessed.add(guess)
		else:
			incorrect_letters_guessed.add(guess)
			num_guesses += 1

		
		word_string = generate_word_string(WORD, correct_letters_guessed)
		print(HANGMAN[len(incorrect_letters_guessed)])
		print(word_string)
		print("You have {} guesses left".format(10 - num_guesses))
		print("You have guessed {} so far".format(list(incorrect_letters_guessed)))	

	if num_guesses < 10:
		print("Congratulations, you win!! You correctly guessed the word {}".format(WORD))
	else:
		print("Sorry, you lose! Your word was {}".format(WORD))


main()	
