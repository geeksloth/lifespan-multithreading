from threading import Thread
from time import sleep, process_time, time


class Life (Thread):
	def __init__(self, name, lifespan):
		Thread.__init__(self)
		self.name = name
		self.lifespan = lifespan
		self.age = 0
	def run(self):
		print(self.name + " born")
		while self.age <= self.lifespan:
			sleep(1)
			print("%s: %s" % (self.name, self.age))
			self.age += 1
		print(self.name + " died")

planet = [
	Life("Mosquito", 1), #7
	Life("Housefly", 4), #28
	Life("Butterfly", 2) #14
	]

if __name__ == "__main__":
	tic = process_time()

	for life in planet:
		life.start()

	for life in planet:
		life.join()

	toc = process_time()
	print("main process time: {}".format(toc-tic))
	print("Lifes are dead")