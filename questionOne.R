##  A. Make prediction of attrition status in the testing set (Make sure you present what methods you used).
# Reading in cleaned data (data was cleaned in Python)
library(readxl)
output_1_ = read_excel("~/Desktop/output (1).xlsx")
View(output_1_)

# Applying logistic regression model 
logisticRegression = glm(AttritionStatus ~ DistanceFromHome	+ JobLevel + WorkLifeBalance + PercentSalaryHike + HourlyRate + YearsWithCurrManager + JobSatisfaction + EnvironmentSatisfaction + YearsSinceLastPromotion + EducationLevel + YearsAtCompany + Travel_For_Business + MaritalStatus + MonthlyIncome + Age + TotalWorkingYears + LastYearTrainingTime + RelationshipSatisfaction + YearsInCurrentRole + JobInvolvement + StockOptionLevel + NumCompaniesWorked, family=binomial(link='logit'), data=output_1_)

summary(logisticRegression)

# Getting logistic regression coefficients 
coefficients =coefficients(logisticRegression, complete = TRUE)
View(coefficients)

pValues = coef(summary(logisticRegression))[,4]

# Creating new data frame with coefficients and p values 
logisticRegressionOutput = data.frame(coefficients, pValues)
View(logisticRegressionOutput)

# Writing data frame to CSV 
write.csv(logisticRegressionOutput, file = 'logisticRegressionOutput.csv')