import sys
import random

playingGame = True

while playingGame:

	answer = random.randint(0,100)
	print("I am thinking of a random number")

	print("Please type in a number")
	attempt = sys.stdin.readline()
	attempt = int(attempt)

	if answer == attempt:
		print("Correct!")
	if attempt < answer:
		print("This is too small")
	if attempt > answer:
		print("This is too large")

	# TODO: Only set playingGame = False when
	# the user guesses correctly.
	playingGame = False

	