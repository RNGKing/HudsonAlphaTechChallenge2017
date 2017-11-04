import csv
        
def insertionSort(object_to_sort):
    i = 1
    while i < len(object_to_sort):
        j = i - 1
        temp = object_to_sort[i]
        while j >= 0 and object_to_sort[j][1] > temp[1]:
            object_to_sort[j+1] = object_to_sort[j]
            j = j - 1
        object_to_sort[j+1] = temp
        i = i + 1
    return object_to_sort

marker_path = 'Copy of gwas_catalog_v1.0-associations_e90_r2017-10-10.csv'
file = open(marker_path, newline='', encoding='utf-8')
reader = csv.reader(file)
header = next(reader)
marker_data = [row for row in reader]
marker_dict = {}

for row in marker_data:
    key = row[22]
    attribute = row[8]
    if key not in marker_dict:
        marker_dict.update({key:[attribute]})
    else:
        marker_dict[key].append(attribute)

genome_path = 'genome_Douglas_R_Full_20130114135651.txt'
genome_file = open(genome_path, newline='', encoding='utf-8')
genome_reader = csv.reader(genome_file, delimiter='\t')
genome_data = [row for row in genome_reader]
list_of_problems = []
for row in genome_data:
    if row[0] in marker_dict:
        list_of_problems.append(marker_dict[row[0]])

histogram = {}
for problem in list_of_problems:
    for issue in problem:
        if 'itis' in issue:
            if issue not in histogram:
                histogram.update({issue:1})
            else:
                histogram[issue] = histogram[issue] + 1

currated_list = list(histogram.items())



sorted_list = insertionSort(currated_list)
sorted_list = list(reversed(sorted_list))

for i in range(0,10):
    print(sorted_list[i][0])

            
