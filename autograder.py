	# Autograder

# This will attempt to perform intended tasks for SortedList, using Sortables.
# For each task, the autograder will:
#  - Define some expected behavior for some use case
#  - Perform the use case
#  - Award "points" if the result is as expected
#  - Either not award points (not too bad) or cause an error (pretty bad) if the result is not as expected
#    NOTE: Exception handling here could manage these errors, but it can be helpful to see them as well!

# This is a script to do the tests and print out what's happening
def singleTest(desc, target, val, pts):
	print("AUTOGRADER: " + desc)
	print(" - Expected Value: " + str(target))
	print(" - Observed Value: " + str(val))
	score = 0
	if (val == target):
		score = 25
		pts = pts + 25
	print("POINTS: This section: " + str(score).zfill(2) + "/05 Total: " + str(pts).zfill(3) + "/100\n")	
	return pts

points = 0

print("\n --- AUTOGRADER: ShortestDistance ---\n")
from graph import Graph
g = Graph()
g.fromCSV("west.csv")

print("\nAUTOGRADER: ShortestDistance checking: 50 pts\n")
points = singleTest("Seattle to Phoenix", 27, g.shortestDistance(g.getVertex("Seattle"),g.getVertex("Phoenix")), points)
points = singleTest("Checking Vancouver to Juarez", 37, g.shortestDistance(g.getVertex("Vancouver"),g.getVertex("Juarez")), points)

print("\nAUTOGRADER: Complexity checking: 50 pts\n")
from time import time
t = time()
g.shortestDistance(g.getVertex("Seattle"),g.getVertex("Phoenix"))
t = time() - t
points = singleTest("Should run in under .01s", True, t < .01, points)
t = time()
g.shortestDistance(g.getVertex("Vancouver"),g.getVertex("Juarez"))
t = time() - t
points = singleTest("Should run in under .01s", True, t < .01, points)