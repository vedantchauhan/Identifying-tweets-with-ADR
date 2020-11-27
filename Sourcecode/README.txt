
- README.txt: This file, which describes problem context, program implementation details, procedure to execute program, 
files used in program, and output details.

- Program context: Identifying tweets with Adverse Drug Reactions
Identify tweets which show signs of adverse drug reactions 

- Implementation details and Execution of program:
The program is implemented in python. The path /Sourcecode/ has Proj2.py file. Run this program in terminal by 
executing the following command:
python Proj2.py

- Files used and Output details:
The files used are words.txt, output.csv, outputWeka.arff, (train_new/dev_new/test_new).arff, (train/dev/test).txt, and (train/dev/test).arff
1. words.txt
This file contains list of features selected manually.
2. output.csv
This file is used to print output in comma separated values of new features from words.txt.
3. outputWeka.arff
This file is used to print Weka file format(.arff) with attributes and csv values.
4. (train/dev/test).txt
These files is used one at a time to check frequency of features in tweets.
5. (train/dev/test).arff
These files used one at a time to read old values and combine those values in outputWeka.arff.
6. (train_new/dev_new/test_new).arff
These files are the final files that can be upload into Weka for evaluating models. These files contain 
updated attributes, and csv values.

All files from 1-5 are used in code, but 6th is created manually with all new data for Weka use.
