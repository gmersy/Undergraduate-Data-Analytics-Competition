
import math
import csv


fields = {
"JobID": 2,
"AttritionStatus": 3,
"DistanceFromHome": 4,
"JobLevel": 5,
"WorkLifeBalance": 6,
"PercentSalaryHike": 7,
"HourlyRate": 8,
"YearsWithCurrManager": 9,
"JobSatisfaction": 10,
"EnvironmentSatisfaction": 11,
"YearsSinceLastPromotion": 12,
"EducationLevel": 13,
"YearsAtCompany": 14,
"Gender": 15,
"Travel_For_Business": 16,
"MaritalStatus": 17,
"MonthlyIncome": 18,
"Age": 19,
"TotalWorkingYears": 20,
"LastYearTrainingTime": 21,
"RelationshipSatisfaction": 22,
"YearsInCurrentRole": 23,
"JobInvolvement": 24,
"StockOptionLevel": 25,
"NumCompaniesWorked": 26,
}


alpha = 0.01
constants = []

def predictAttrition(row):

	tot = 0.

	#add intercept if p-value is below the threshold
	if constants[0][1] <= alpha:
		tot += constants[0][1]

	for c in constants[1:]:
		#if p-value less than alpha
		if c[2] <= alpha:
			#multiply variable by constant and add total
			tot += float(row[fields[c[0]]]) * c[1]

	return 'Yes' if math.exp(tot) >= 0.5 else 'No'
	#return math.exp(tot)


with open('logisticRegressionOutput.csv') as file:

	for i, line in enumerate(file):

		if line != '' and i != 0:
			temp = line.split(',')
			constants.append((temp[0][1:-1], float(temp[1]), float(temp[2])))

	#for c in constants:
	#	print(c)

data = []

with open('test_output.csv') as file:
	reader = csv.reader(file, delimiter=',', quotechar='"')
	for row in reader:
		data.append(row)

results = []

for i, row in enumerate(data):

	if i == 0:
		#results.append(['', 'JobID', 'AttritionStatus'])
		continue

	results.append([i, row[fields['JobID']], predictAttrition(row)])


with open('test_predictions.csv', 'w') as file:
	string = ',JobID,AttritionStatus\n'
	for r in results:
		#print(r)
		string += '%d,%s,%s\n' % (r[0], r[1], r[2])
	#print(string)
	file.write(string)

