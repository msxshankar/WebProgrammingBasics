import csv
from matplotlib import pyplot as plt

def generate_summary_for_web(html_filename):
	with open(html_filename, "w") as html:
		html.write("<html>")
		html.write("<style>")
		html.write("table,th,td {\n")
		html.write("border:1px solid black;\n")
		html.write("}\n")
		html.write("</style>")
		html.write("<body>")
		html.write("<h1>hello</h1>")
		html.write("<table>")
		html.write("<tr>")
		html.write("<th>Attributes</th>")
		html.write("<th>Class</th>")
		html.write("</tr>")
		html.write("</table>")
		html.write("</body>")
		html.write("</html>")
		
		with open("diabetes_data.csv", "r") as diabetes_data:
			diabetes_data.readline()
			
			reader = csv.reader(diabetes_data)
			for row in reader:
				html.write("<tr>\n")
				for elm in row:
					html.write(""+ elm + "</td>\n")
				html.write("</tr>\n")

		# Close all the opened html tags
		html.write("</body>")
		html.write("</html>")
				
generate_summary_for_web("summary.html")

	
