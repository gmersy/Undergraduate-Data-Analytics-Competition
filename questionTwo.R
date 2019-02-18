##  B. What variables have the highest impact on job-satisfaction? 
multipleLinearRegression = lm(JobSatisfaction ~ AttritionStatus + DistanceFromHome	+ JobLevel + WorkLifeBalance + PercentSalaryHike + HourlyRate + YearsWithCurrManager + EnvironmentSatisfaction + YearsSinceLastPromotion + EducationLevel + YearsAtCompany + Travel_For_Business + MaritalStatus + MonthlyIncome + Age + TotalWorkingYears + LastYearTrainingTime + RelationshipSatisfaction + YearsInCurrentRole + JobInvolvement + StockOptionLevel + NumCompaniesWorked, data=output_1_)
summary(multipleLinearRegression)

coefficientsLM = coefficients(multipleLinearRegression, complete = TRUE)
View(coefficients)

pValuesLM = coef(summary(multipleLinearRegression))[,4]
standardErrorLM = coef(summary(multipleLinearRegression))[,2]

# Creating new data frame with coefficients and p values 
LMOutput = data.frame(coefficientsLM, pValuesLM, standardErrorLM)
View(LMOutput)

write.csv(logisticRegressionOutput, file = 'multipleLinearRegressionOutput.csv')