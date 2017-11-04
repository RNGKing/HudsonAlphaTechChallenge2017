import csv

# Column 8 and 22

marker_path = 'Copy of gwas_catalog_v1.0-associations_e90_r2017-10-10.csv'
disease_file = open(marker_path, newline='', encoding='utf-8')
reader = csv.reader(disease_file)
header = next(reader)
data = [row for row in reader]
marker_map = []
for i in range(len(data)):
    disease = ''
    marker = ''
    for j in range(len(data[i])):
        if j == 8:
            disease = data[i][j]
        elif j == 22:
            marker = data[i][j]
            break
    paired_data = (marker, disease)
    marker_map.append(paired_data)


genome_path = 'genome_Douglas_R_Full_20130114135651.txt'
genome_file = open(genome_path, newline='', encoding='utf-8')
genome_reader = csv.reader(genome_file, delimiter='\t')
genome_data = [row for row in genome_reader]
risk = []
for i in range(len(genome_data)):
    for j in range(len(marker_map)):
        if genome_data[i][0] == marker_map[j][0]:
            print("You may be at risk for: " + marker_map[j][1])
            risk.append(marker_map[j][1])

if len(risk) != 0:
    print(risk)
else:
    print('no risk factors were located!')
        
    
    
