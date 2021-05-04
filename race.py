import turtle
import time
import random
import sys

class text:
	def __init__(self):
		self.text = turtle.Turtle()
		self.font = ("Arial", 20, "normal")
		self.text.color("brown")

	def write_message(self, message, to_console = True):
		self.text.write(message, False, align = "center", font = self.font)
		if to_console:
			print (message)

	def set_pos(self, x, y):
		self.text.penup()
		self.text.setpos(x, y)
		self.text.pendown()

class line:
	def __init__(self):
		self.line = turtle.Turtle()
		self.line.shape("classic")
		self.line.color("blue")
		self.line.pensize(5)

	def draw_finish_line(self, start, length):
		self.line.penup()
		self.line.right(90)
		x,y = start
		self.line.setpos(x,y)
		self.line.pendown()
		self.line.forward(length)

class Racer:
	def __init__(self, color, shape, pos_x, pos_y):
		self.racer = turtle.Turtle()
		self.racer.color(color)
		self.racer.shape(shape)
		self.pos_x, self.pos_y = pos_x, pos_y

	def advance(self):
		self.racer.forward(random.randrange(1, 15))

	def set_initial_pos(self):
		self.racer.penup()
		self.racer.setpos(self.pos_x, self.pos_y)
		self.racer.pendown()

	def get_pos(self):
		return self.racer.pos()

class Race:
	WIN_W = 800
	WIN_H = 800
	FINISH_LINE_DISTANCE = 30
	RACER_COLORS = ['yellow', 'red', 'blue', 'green', 'gray', 'orange', 'brown', 'black', 'light blue', 'pink']

	def __init__(self):
		self.racers = []
		self.colors = []
		self.winners = []
		self.num_of_racers = 0
		self.has_winners = False

	def get_num_of_racers(self):
		racers = 0
		while True:
			if sys.version_info[0] == 2:
				racers = raw_input('Please enter the number of racers (2 - 10): ')
			else:
				racers = input('Please enter the number of racers (2 - 10): ')
			if racers.isdigit():
				racers = int(racers)
			else:
				print('No-numeric input was inserted, please try again.')
				continue

			if 2 <= racers <= 10:
				self.num_of_racers = racers
				random.shuffle(Race.RACER_COLORS)
				self.colors = Race.RACER_COLORS[:self.num_of_racers]
				break
			else:
				print('Number should be in range 2-10. Try Again.')

	def create_racers(self):
		y_space = Race.WIN_H // (self.num_of_racers + 1)
		for i, color in enumerate(self.colors):
			racer = Racer(color, 'turtle', -Race.WIN_W//2 + 20, -Race.WIN_H//2 + (i + 1) * y_space)
			self.racers.append(racer)

	def init_race(self):
		self.get_num_of_racers()
		self.create_racers()
		self.screen = turtle.Screen()
		self.screen.setup(Race.WIN_W, Race.WIN_H)
		self.screen.title('Race Screen')
		finish_line = line()
		finish_line_start_position = (Race.WIN_W//2 - Race.FINISH_LINE_DISTANCE, Race.WIN_H//2)
		finish_line.draw_finish_line(finish_line_start_position, Race.WIN_H)
		for racer in self.racers:
			racer.set_initial_pos()

	def finish_race(self):
		end_text = text()
		pos_h = Race.WIN_H//2 - 100
		end_text.set_pos(0,pos_h)
		message = "Race ended"
		end_text.write_message(message)
		for racer in self.winners:
			pos_h -= 30
			end_text.set_pos(0, pos_h)
			message = "We have a winner: " + self.colors[self.racers.index(racer)]
			end_text.write_message(message)
		time.sleep(4)

	def run_race(self):
		while self.has_winners == False:
			for racer in self.racers:
				x,y = racer.get_pos()
				if x > Race.WIN_W // 2 - Race.FINISH_LINE_DISTANCE:
					self.winners.append(racer)
					self.has_winners = True

			if not self.has_winners:
				for racer in self.racers:
					racer.advance()

if __name__ == '__main__':
	race = Race()
	race.init_race()
	race.run_race()
	race.finish_race()
	quit()
