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
			for row in reader:
				list_of_attributes.append(row)
			datalist = list(reader)
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
	
	
	
	count_yes_positive = 0
	count_yes_negative = 0
	count_no_positive = 0
	count_no_negative = 0
	horizontal_count = 0
	vertical_count = 0

	for j in list_of_attributes[0]:
		if j == 'Age' or j == 'Gender' or j == 'class':
			horizontal_count += 1
			print(horizontal_count)
			continue
		else:
			for k in list_of_attributes:
				if vertical_count >= 520:
					html_string += "<tr>\n"
					html_string += "<td>" + j + "</td>\n"
					html_string += "<td>" + str(count_yes_positive) + "</td>\n"
					html_string += "<td>" + str(count_no_positive) + "</td>\n"
					html_string += "<td>" + str(count_yes_negative) + "</td>\n"
					html_string += "<td>" + str(count_no_negative) + "</td>\n"
					html_string += "</tr>\n\n"
					horizontal_count += 1
					vertical_count = 0
					count_yes_positive = 0
					count_no_positive = 0
					count_yes_negative = 0
					count_no_negative = 0
					continue
				vertical_count += 1
				print(vertical_count)
				if (list_of_attributes[vertical_count][horizontal_count] == 'Yes') and (list_of_attributes[vertical_count][16] == 'Positive'):
					count_yes_positive += 1
				if (list_of_attributes[vertical_count][horizontal_count] == 'No') and (list_of_attributes[vertical_count][16] == 'Positive'):
					count_no_positive += 1
				if (list_of_attributes[vertical_count][horizontal_count] == 'Yes') and (list_of_attributes[vertical_count][16] == 'Negative'):
					count_yes_negative += 1
				if (list_of_attributes[vertical_count][horizontal_count] == 'No') and (list_of_attributes[vertical_count][16] == 'Negative'):
					count_no_negative += 1
	
	

	print(count_yes_positive)
	print(count_no_positive)
	print(count_yes_negative)
	print(count_no_negative)

	'''
	x = -1
	for record in data:
		html_string += "<tr>\n"
		for datum in record:
			html_string += "<td>" + datum + "</td>\n"
			x += 1
			print(x)
		html_string += "</tr>\n\n"
	'''

	html_string += "</table>\n\n"
	return html_string
				
generate_summary_for_web("diabetes_data.csv", "Diabetes Table", "summary.html")