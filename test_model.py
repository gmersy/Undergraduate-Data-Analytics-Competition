
#UDAC 2019 Data Analytics Competition

import csv

data = []

with open('test.csv') as file:
	reader = csv.reader(file, delimiter=',', quotechar='"')
	for row in reader:
		data.append(row)

satisfaction_conversion = {'Disatisfied': 0, 'OK': 1, 'Satisfied': 2, 'Very Satisfied': 3}
#job_roles = set()
role_conversion = {'Manager': 0, 'Sales Representative': 1, 'Sales Executive': 2, 'Human Resources': 3, 'Laboratory Technician': 4, 'Research Director': 5, 'Manufacturing Director': 6, 'Healthcare Representative': 7, 'Research Scientist': 8}
gender = {'Male': 0, 'Female': 1}
#travel_options = set()
travel_conversion = {'Non-Travel': 0, 'Travel_Rarely': 1, 'Travel_Frequently': 2}
#education_fields = set()
education_field_conversion = {'Human Resources': 0, 'Technical Degree': 1, 'Medical': 2, 'Life Sciences': 3, 'Marketing': 4, 'Other': 5}
marital_status_conversion = {'Divorced': 0, 'Single': 1, 'Married': 2}


cleaned_data = []
cleaned_data.append(data[0].copy())
cleaned_data[0].insert(5, "")

del cleaned_data[0][-1] #daily rate
del cleaned_data[0][34] #department
del cleaned_data[0][33] #overtime
del cleaned_data[0][32] #employee count
del cleaned_data[0][29] #employee number
del cleaned_data[0][26] #standard hours
del cleaned_data[0][24] #perfomance rating
del cleaned_data[0][22] #education field
del cleaned_data[0][17] #job role
del cleaned_data[0][14] #over 18
del cleaned_data[0][12] #monthly rate
del cleaned_data[0][4] #year of birth
del cleaned_data[0][2] #name

for i, row in enumerate(data[1:]):

	row.insert(5, "")
	#print(row)

	if row[6] == 'NA' or row[30] == 'NA':
		continue

	temp = row.copy()

	#job_roles.add(temp[17])
	#travel_options.add(temp[21])
	#education_fields.add(temp[22])

	temp[5] = 1 if temp[5].lower() == 'yes' else 0

	temp[13] = satisfaction_conversion[temp[13]]
	temp[17] = role_conversion[temp[17]]
	temp[20] = gender[temp[20]]
	temp[21] = travel_conversion[temp[21]]
	temp[22] = education_field_conversion[temp[22]]
	temp[23] = marital_status_conversion[temp[23]]

	del temp[-1] #daily rate ***
	del temp[34] #department
	del temp[33] #overtime
	del temp[32] #employee count
	del temp[29] #employee number
	del temp[26] #standard hours
	del temp[24] #perfomance rating
	del temp[22] #education field
	del temp[17] #job role
	del temp[14] #over 18
	del temp[12] #monthly rate ***
	del temp[4] #year of birth
	del temp[2] #name

	cleaned_data.append(temp)

#print(job_roles)
#print(travel_options)
#print(education_fields)

with open('test_output.csv', 'w', newline='') as out_file:
	writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	for row in cleaned_data:
		writer.writerow(row)

