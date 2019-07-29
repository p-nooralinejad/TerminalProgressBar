from progressBar import progressBar
from time import sleep
import sys
import os

progress = progressBar(tot_items = 30, name = "Epoch progress")

t = [30,25,60,70,10]

for j in range(5):
	for i in range(t[j]):
		progress.signal_job_done()
		sleep(0.25)
	print("EPOCH FINISHED !!!")
	if j + 1< 5:
		progress.reset(t[j + 1])
