class Graph:

	def __init__(self):
		self.setv = set()
		self.sete = set()
		
	def addEdge(self,v1,v2,e,c):
		self.sete.add(self.Edge(e,v1,v2,c))
	
	def addVertex(self,n):
		self.setv.add(self.Vertex(n))

	def getVertex(self,n):
		names = [[v.name,v] for v in self.setv]
		for i in names:
			if i[0] == n:
				return i[1]
		
	def fromCSV(self,file):  
		for line in open(file,"r"):
			[v1,v2,e,c] = line[:-1].split(", ")
			self.addVertex(v1)
			self.addVertex(v2)
			self.addEdge(self.getVertex(v1),self.getVertex(v2),e,int(c))
			
	class Vertex: # vertexes

		def __repr__(self):
			return "VERTEX: " + self.name
		def __str__(self):
			return "VERTEX: " + self.name
		def __eq__(self,other):
			return self.name == other.name

		def __init__(self, n):
			self.name = str(n)
			
		def __hash__(self):
			return hash(self.__str__())
			
	class Edge: # edges

		def __repr__(self):
			lst = list(self.vrts)
			return "EDGE: " + self.name + " from " + str(lst[0]) + " to " + str(lst[1])
		def __str__(self):
			return self.__repr__()

		def __init__(self, n, v1, v2, c):
			self.name = n
			self.vrts = {v1,v2}
			self.cost = c
			
		def __hash__(self):
			return hash(self.__str__())
		