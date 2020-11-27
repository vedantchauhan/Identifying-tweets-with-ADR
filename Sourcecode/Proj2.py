# Author     : Vedant Chauhan
# Student id : 892758
import sys, re

# Weka input file
wekaFile = open("test.arff",'r')
write_content = []
feature = []
wekaSplit = []

# Feature file
feature_file = "words.txt"

# Feature length, bigrams
feature_length = 2

# Input file(train,dev,test can be included)
input_file = "test.txt"

# Output file(csv output)
output_file = "output.csv"

# Feature file is open and read by line and strip with newline
with open(feature_file) as f:
    feature_content = f.readlines()
feature_contents = [x.strip() for x in feature_content]

feature_extracts = []
for feature_content in feature_contents:
    words = feature_content.split()
    if len(words) == feature_length:
        feature_extracts.append(feature_content)

csv_start = 'id'
for feature_extract in feature_extracts:
    csv_start += ',' + feature_extract
csv_start += '\n'

# Input file is open and read by line and strip with newline
with open(input_file) as f:
    feature_content = f.readlines()
input_file_contents = [x.strip() for x in feature_content]

csv_content = ''

# Code for counting frequency of feature in a tweet
for input_file_content in input_file_contents:
    current_csv_content = input_file_content.split('\t')
    current_csv_line = str(current_csv_content[0]) + ','
    for feature_extract in feature_extracts:
        current_csv_line += str( len(re.findall(feature_extract, current_csv_content[2], flags=re.IGNORECASE)) ) + ','
    csv_content += current_csv_line.rstrip(",") + "\n"

csv_content = csv_content.rstrip('\n')

#To create arff file
for wekaFeature in wekaFile:
	feature = wekaFeature.split("\n")
	for string in feature:
		if string.startswith("@ATTRIBUTE zombie"):
			write_content.append("@ATTRIBUTE zombie NUMERIC\n")
			for tokens in feature_extracts:
				write_content.append("@ATTRIBUTE "+tokens+"  NUMERIC\n")
		elif string.startswith("3"):
			write_content.append(string)
		else:
			write_content.append(string)

# Write content of arff file
writeContents = open("outputWeka.arff", 'w')
for item in write_content:
   writeContents.write("%s" % item)
# Write content of csv file
op_file = open(output_file, "w")
op_file.write(csv_start)
op_file.write(csv_content)
op_file.close()
