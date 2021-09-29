import shutil
import os
import sys
import curses

def send(seq: str):
	sys.stdout.write(seq)
	sys.stdout.flush()

class terminalWriter:
	ROWS=0
	COLS = 0
	
	def __init__(self):
		self.COLS, self.ROWS = shutil.get_terminal_size()
	
	def get_current_position(self):
		return 0

	def write_progress_bar(self, value):
		send("%s\033[2A" % value)

	def write(self, x: int, y: int, value):
		send("\033[%s;%sH%s" % (y, x, value))

	def clear(self):
		send("\033c")

	def move_cursor(self,x,y):
		send("\033[%d;%dH" % (y, x))

	def get_rows(self):
		return self.ROWS;

	def get_columns(self):
		return self.COLS;

	def done(self):
		send("")
