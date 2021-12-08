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
	try:
		with open(csvfile, "r") as diabetes_data:
			diabetes_data.readline()
			reader = csv.reader(diabetes_data)
			datalist = list(reader)
			return datalist
	except (FileNotFoundError):
		return "File error"

def create_html_table_with_data(data):
	html_string = "<style>\n"
	html_string += "table,th,td {\n border: 1px solid black; \n"
	html_string += "border-collapse: collapse; text-align:center\n"
	html_string += "}\n"
	html_string += "</style>\n"
	html_string += "<table>\n"

	html_string += "<tr>"
	html_string += "<th>Attributes</th>"
	html_string += "<th>Class</th>"
	html_string += "</tr>"

	for record in data:
		html_string += "<tr>\n"
		for datum in record:
			html_string += "<td>" + datum + "</td>\n"
		html_string += "</tr>\n\n"

	html_string += "</table>\n\n"
	return html_string
				
generate_summary_for_web("diabetes_data.csv", "Diabetes Table", "summary.html")