# this is to display bowling game score for the players which are entered in the dynamic list
from random import randint


class BowlingGame(object):
	"""this class will contain all the methods related to bowing game"""
	def __init__(self):
		self.total_pins = 10

	def rolling(self):
		return randint(0, self.total_pins)

	def get_score(self):
		results = []
		for roll in range(10):
			if self.strike(self.rolling()):
				results.append(self.strike_score())

			if self.spare(self.rolling()):
				results.append(self.spare_score())

		return results

	def strike(self, roll_score):
		return roll_score == self.total_pins

	def spare(self, roll_score):
		return roll_score != self.total_pins

	def strike_score(self):
		return 10 + self.rolling() + self.rolling()

	def spare_score(self):
		return self.rolling() + self.rolling()


bowling_object = BowlingGame()
players = ['Same', 'Oneof'] # list of player, can be extended.
for player in players:
	score = bowling_object.get_score()
	print "Score Details of %s" %player
	print "Framewise score ", score
	print "Total score is of is ", sum(score)
