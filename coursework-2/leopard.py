import csv

class Leopard:
	def __init__(self, csvfile):
		self.csvfile = csvfile
		self.headerlist = []
		self.datalist = []
		self.rowcount = 0 
		self.columncount = 0 
		self.dimension = 0
		self.csvarray = []
		self.occurences = 0
		self.missingcount = 0
		self.columnindex = 0

	def get_header(self):
		try:
			with open(leopard.csvfile) as file:
				reader = csv.reader(file)
				self.headerlist = next(reader)
			return self.headerlist
		except FileNotFoundError:
			return None
	
	def get_dimension(self):
		try:
			with open(leopard.csvfile) as file:
				reader = csv.reader(file)
				self.headerlist = next(reader)
				self.columncount = len(self.headerlist)
				for row in reader:
					self.rowcount += 1
				self.dimension = [self.rowcount, self.columncount]
				return self.dimension
		except FileNotFoundError:
			return None

	def count_instances(self, column_heading, value):
		try:
			column_heading = column_heading.lower()
			value = value.lower()
			with open(leopard.csvfile, 'r') as file:
				reader = csv.reader(file)
				for row in reader:
					self.csvarray.append(row)
				self.csvarray[0] = list(map(str.lower, self.csvarray[0]))
				self.columnindex = self.csvarray[0].index(column_heading)
				for i in self.csvarray:
					if i[self.columnindex].lower() == value:
						self.occurences += 1
				return self.occurences
			
		except FileNotFoundError:
			return None

	def total_missing(self):
		try:
			with open(leopard.csvfile, 'r') as file:
				reader = csv.reader(file)
				for row in reader:
					self.csvarray.append(row)
				for i in self.csvarray:
					for j in i:
						if j == "NA" or j == "?" or j == "":
							self.missingcount += 1
							break	
				return self.missingcount
		except FileNotFoundError:
			return None

leopard = Leopard("diabetes_data.csv")
