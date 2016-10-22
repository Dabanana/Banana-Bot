class Tictactoe:

	def __init__(self):
		self.board = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
		self.turn = 1
		self.win = 0


	def __str__(self):
		gameboard = []
		for row in self.board:
			for value in row:
				if value == 0:
					gameboard.append(":white_medium_square:")
				elif value == -1:
					gameboard.append(":heavy_multiplication_x:")
				elif value == 1:
					gameboard.append(":o:")
		return "{0[0]} | {0[1]} | {0[2]}\n-----------------\n{0[3]} | {0[4]} | {0[5]}\n-----------------\n{0[6]} | {0[7]} | {0[8]}".format(gameboard)

	def column(self):
		checkcolumn = [0,0,0]
		boardfull = 0
		for row in self.board:
			for (i, value) in enumerate(row):
				checkcolumn[i] += value
				boardfull += abs(value)
		for total in checkcolumn:
			if total == 3:
				self.reset_board()
				self.win += 1
			elif total == -3:
				self.reset_board()
				self.win -= 1
		if boardfull == 9:
			self.win = 2

	def row(self):
		checkrow = [0,0,0]
		for (i,row) in enumerate(self.board):
			for value in row:
				checkrow[i] += value
		for total in checkrow:
			if total == 3:
				self.reset_board()
				self.win += 1
			elif total == -3:
				self.reset_board()
				self.win -= 1

	def diagonal(self):
		new = []
		diagonal = [0,0]
		for row in self.board:
			for column in row:
				new.append(column)
		diagonal[0] = new[0] + new[4] + new[8]
		diagonal[1] = new[2] + new[4] + new[6]
		for total in diagonal:
			if total == 3:
				self.reset_board()
				self.win += 1
			elif total == -3:
				self.reset_board()
				self.win -= 1

	def check(self):
		self.column()
		self.row()
		self.diagonal()
		if self.win == 1:
			return "Naughts' win"
		if self.win == -1:
			return "Crosses' win"
		if self.win == 2:
			return "It's a Draw!"
		else:
			if self.turn == -1:
				return "Crosses' Turn"
			else:
				return "Naughts' Turn"

	def naught(self,column,row):
		if self.turn == -1:
			return "It's not your turn, fuckboy"
		if column > 3 or row > 3:
			return "Enter some better co-ordinates."
		x = column - 1
		y = row - 1
		if self.board[y][x] == 0:
			self.board[y][x] += 1
			self.turn = -1
		return self

	def cross(self,column,row):
		if self.turn == 1:
			return "It's not your turn, fuckboy"
		if column > 3 or row > 3:
			return "Enter some better co-ordinates."
		x = column - 1
		y = row - 1
		if self.board[y][x] == 0:
			self.board[y][x] -= 1
			self.turn = 1
		return self
		self.check()

	def reset_board(self):
		self.board = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
		return
