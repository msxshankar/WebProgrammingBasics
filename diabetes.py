import csv
from matplotlib import pyplot as plt


def generate_summary_for_web(csvfile, html_title, html_filename):
	
	data = get_datalist_from_csv(csvfile)

	if data == "File error":
		return
	
	with open(html_filename, "w") as html:
		html.write('<html>')
		html.write('<title>' + html_title + '</title>\n')
		html.write('<center>\n')
		html.write('<h1>' + html_title + '</h1>\n')
		html_table = create_html_table_with_data(data)
		html.write(html_table)
		html.write('</center>\n')
		html.write('</html>\n')

def get_datalist_from_csv(csvfile):
	global list_of_header_names, list_of_attributes
	list_of_header_names = []
	list_of_attributes = []
	try:
		with open(csvfile, "r") as diabetes_data:
			#diabetes_data.readline()
			reader = csv.reader(diabetes_data)
			list_of_header_names = next(reader)
			list_of_attributes.append(list_of_header_names)
			datalist = list(reader)
			for row in reader:
				list_of_attributes.append(row)
			return datalist
			#header = get_headerdata_from_csv(csvfile)
	except (FileNotFoundError):
		return "File error"
	
'''
def get_headerdata_from_csv(csvfile):
	try:
		with open(csvfile, "r") as header_data:
			csv_reader = csv.reader(header_data)
			list_of_header_names = []
			for row in header_data:
				list_of_header_names.append(row)
				break
	except (FileNotFoundError):
		return "File error"
'''

def create_html_table_with_data(data):
	html_string = "<style>\n"
	html_string += "table,th,td {\n border: 1px solid black; \n"
	html_string += "border-collapse: collapse; text-align:center\n"
	html_string += "}\n"
	html_string += "</style>\n"
	html_string += "<table>\n"

	html_string += "<tr>"
	html_string += "<th rowspan='3'>Attributes</th>"
	html_string += "<th colspan='4'>Class</th>"
	html_string += "</tr>"

	html_string += "<tr>"
	html_string += "<th colspan='2'>Positive</th>"
	html_string += "<th colspan='2'>Negative</th>"
	html_string += "</tr>"

	html_string += "<tr>"
	html_string += "<td> Yes </td>"
	html_string += "<td> No </td>"
	html_string += "<td> Yes </td>"
	html_string += "<td> No </td>"
	html_string += "</tr>"
	
	occurences = 0
	for i in list_of_attributes:
		if i == 'Age' or 'Gender'
			continue
		else:
			for j in 
				if j = 'Yes'
			occurences += 1
				if i[columnindex].lower() == value:
					occurences += 1
			return occurences
	x = -1
	for record in data:
		html_string += "<tr>\n"
		for datum in record:
			html_string += "<td>" + datum + "</td>\n"
			x += 1
			print(x)
		html_string += "</tr>\n\n"

	html_string += "</table>\n\n"
	return html_string
				
generate_summary_for_web("diabetes_data.csv", "Diabetes Table", "summary.html")