import time

with open("testing.txt", "a") as test:
	for x in range(0, 5):
		test.write(time.strftime("%c") + '\n')
test.close()
	
