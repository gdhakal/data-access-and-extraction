# Pre-Modeling: Data Preprocessing and Feature Exploration in Python

## Modeling
- Statistical technique to predict unknown outcomes.

	- Binary classification - Determine the probability that an observation belongs to one of two groups.
	  Example: 
		- Whether a person votes for one of two political candidates
		- Whether a credit card transaction is fraud
		- Whether or not a person will be diagnosed with a given disease in the next year

## Data Terminology
- Inputs: Independent variables (features)
	- Predictors
- Outputs: Dependent variable (outcomes)
	- Target variable for prediction
- Model shows the effect that features have on the outcome

## Assess model performance
- Randomly split observations into train/test sets
- Build model on train set and assess performance on test set
- Use performance measurement metric to find out if those predictions matched the expected outcome.


## Data cleaning
Three types of data:
1) Numeric, e.g. income, age
2) Categorical, e.g. gender, nationality
3) Ordinal/Scale, e.g. low/medium/high

- Models can only handle numeric features
- Must convert categorical and ordinal features into numeric features
	- Transform the categorical variable into a set of dummies. Each dummy represents unique category.
	- For low frequency category, its better to use 'Other' rather than dummy for all of them.


