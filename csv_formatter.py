import csv

csv_file = open("~/Desktop/sleep_test.csv", "r")
out_file = open("sleep_test_output.csv", "w")

reader = csv.reader(csv_file)
for line in reader:
    print(line)
# out_file.write()

