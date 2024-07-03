#Reading and writing a file 
#writing to a text file
with open('majid.txt','w') as file:
    file.write("I am Majid and I love writing a file.\n")
    file.write("I used python for automation.\n")

#reading from a text file
with open('majid.txt', 'r') as file:
    content=file.read()
    print(content)

#Handling CSV files
"""
CSV(comma separated values)
Key Concepts:
Reading CSV files: Using CSV.reader()
Writing CSV files: Using CSV.writer()
DictReader and DictWriter: The class reads and writes CSV files as dictionaries
"""

#Writing and writing CSV files

import csv
#Writing to CSV files
with open('majid.csv', 'w', newline='') as csv_file:
    writer=csv.writer(csv_file)
    writer.writerow(['name', 'position', 'course'])
    writer.writerow(['Jeoff Jeff', 'Lecturer', 'BSE'])
    writer.writerow(['Fatuma', 'student', 'BSE'])
    writer.writerow(['Alungaru', 'student', 'BSE'])

#Reading from csv file
with open('majid.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)

#JSON and XML file processing
"""
summary_line
JSON(Javascript Object Notation) and XML(extensible Markup Language) are formats used to structure data.

Key Concepts:
Loading JSON data: using json.load() for reading JSON file
Dumping JSON data: using json.dump() for writing JSON file
Parsing JSON data:using json.loads() for handling JSON string

"""

#Read and write JSON file
import json

#writing to a json file

student_data={
    'name': 'Amadile',
    'course': 'BSE',
    'year': 'Year2'
}

#open the JSON file
with open('student_data.json', 'w') as json_file:
    json.dump(student_data, json_file)

#Reading the JSON file
with open('student_data.json', 'r') as json_file:
    student_data=json.load(json_file)
    print(student_data)

#Exercise write and read the XML file
#using abstraction calculate the area and perimeter of a rectangle
import xml.etree.ElementTree as ET

# Create the root element
root = ET.Element("shapes")

# Create a child element (rectangle) with attributes
rectangle = ET.SubElement(root, "rectangle")
ET.SubElement(rectangle, "width").text = "10"
ET.SubElement(rectangle, "height").text = "20"

# Create an ElementTree object and write to a file
tree = ET.ElementTree(root)
with open("shapes.xml", "wb") as files:
    tree.write(files)

import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse("shapes.xml")
root = tree.getroot()

# Extract the rectangle data
for rectangle in root.findall('rectangle'):
    width = rectangle.find('width').text
    height = rectangle.find('height').text
    print(f"Width: {width}, Height: {height}")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

# Create a rectangle instance
rectangle = Rectangle(10, 20)

# Calculate and print the area and perimeter
print(f"Area: {rectangle.calculate_area()}")
print(f"Perimeter: {rectangle.calculate_perimeter()}")
