import csv
from matplotlib import pyplot as plt


def generate_summary_for_web(csvfile, html_title, html_filename, show_barchart_gender=True):
	
	data = get_datalist_from_csv(csvfile)

	if data == "File error":
		return
	
	if show_barchart_gender == True:
		draw_bar_chart()

	with open(html_filename, "w") as html:
		html.write('<html>')
		html.write('<title>' + html_title + '</title>\n')
		html.write('<center>\n')
		html.write('<h1>' + html_title + '</h1>\n')
		html_table = create_html_table_with_data(data, show_barchart_gender)
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
	except (FileNotFoundError):
		return "File error"

def create_html_table_with_data(data, show_barchart_gender):
	html_string = "<style>\n"
	html_string += ".styled-table,th,td {\n border: 1px solid blue; \n"
	html_string += "border-collapse: collapse; text-align:center\n"
	html_string += "font-family: sans-serif;\n"
	html_string += "box-shadow: 0 0 20px rgba(0,0,0,0.15);\n"
	html_string += "}\n"
	html_string += "tr:nth-child(2n + 4) {\n background-color: #89CFF0; \n"
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
			continue
		else:
			for k in list_of_attributes:
				if vertical_count >= 520:
					html_string += "<tr>\n"
					html_string += "<td>" + j.capitalize() + "</td>\n"
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
				if (list_of_attributes[vertical_count][horizontal_count] == 'Yes') and (list_of_attributes[vertical_count][16] == 'Positive'):
					count_yes_positive += 1
				if (list_of_attributes[vertical_count][horizontal_count] == 'No') and (list_of_attributes[vertical_count][16] == 'Positive'):
					count_no_positive += 1
				if (list_of_attributes[vertical_count][horizontal_count] == 'Yes') and (list_of_attributes[vertical_count][16] == 'Negative'):
					count_yes_negative += 1
				if (list_of_attributes[vertical_count][horizontal_count] == 'No') and (list_of_attributes[vertical_count][16] == 'Negative'):
					count_no_negative += 1
	
	html_string += "</table>\n\n"

	if show_barchart_gender == True:
		html_string += "<img src='barchart.png' alt='Bar Chart'>"

	return html_string

def draw_bar_chart():

	count_male_positive = 0
	count_female_positive = 0
	count_male_negative = 0
	count_female_negative = 0
	bar_vertical_count = 0
	count_male = []
	count_female = []

	for l in list_of_attributes:
		bar_vertical_count += 1
		if bar_vertical_count >= 520:
			count_male.append(count_male_positive)
			count_male.append(count_male_negative)
			count_female.append(count_female_positive)
			count_female.append(count_female_negative)

			ind = [1,2]
			width = 0.3
			x = [x - width for x in ind]

			middle = []
			o = -1
			for p in ind:
				o += 1
				middle.append((p + x[o])/2)

			plt.bar(x, count_male, label="Male", width = width)
			plt.bar(ind, count_female, label="Female", width = width)
			plt.title("Gender of Positive vs Negative Cases")
			plt.xlabel("Class")
			plt.ylabel("Count")
			plt.xticks(middle, ('Positive', 'Negative'))			
			plt.legend(loc='best')
			plt.savefig('barchart.png')
			break

		if (list_of_attributes[bar_vertical_count][1] == 'Male') and (list_of_attributes[bar_vertical_count][16] == 'Positive'):
			count_male_positive += 1
		if (list_of_attributes[bar_vertical_count][1] == 'Female') and (list_of_attributes[bar_vertical_count][16] == 'Positive'):
			count_female_positive += 1
		if (list_of_attributes[bar_vertical_count][1] == 'Male') and (list_of_attributes[bar_vertical_count][16] == 'Negative'):
			count_male_negative += 1
		if (list_of_attributes[bar_vertical_count][1] == 'Female') and (list_of_attributes[bar_vertical_count][16] == 'Negative'):
			count_female_negative += 1
			
				
generate_summary_for_web("diabetes_data.csv", "Diabetes Table", "summary.html", show_barchart_gender=True)