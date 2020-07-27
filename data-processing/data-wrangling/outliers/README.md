# Finding an outlier in a Dataset

- An outlier is a data point in a data set that is distant from all other observations.
- Rare conditions
- Outliers can be useful to find cases like credit card fraud cases
- But there could be outliers because of human errors, which needs to be avoided.
- Due to the outliers, the mean and standard deviation may change a lot.

## Methods to find outlier

1) Using scatter plot
	- Scatter plot is a distribution of x and y.
	- Outliers will be visible outside the normal population in the scatter plot.
2) Box plot
	- Box with 25%, 50%, 70% are drawn. Anything below 25% and 75% are outliers.
3) using z score
	- To find standard normal distribution:
		`Z = (x - mean)/standard deviation, where x = observations`
	- Z score tells us at which standard deviation a particular dataset fall into. 
	- If a data that falls outside the 3rd standard deviation, it is considered as outlier.
4) using the IQR interquantile range
	- `IQR = 75 percentile number - 25 percentile number`


## Find percentile:

Dataset: [4, 9, 5, 6, 7, 1, 2, 8, 10]
To find percentile:
- Sort: [1, 2, 4, 5, 6, 7, 8, 9, 10]
  Here, 1 is 0th percentile. There are zero numbers less than 1.
  2 is 10th percentile. 10% of total distribution are less than 2. 90% is greater than or equal to 2.


# Log Transformation for Outliers

- Treat outliers as Log base 10 transformation instead of deleting them as some outliers provide novel insights on data.

## Data Skewness

<img width="765" alt="Screen Shot 2020-07-26 at 1 33 04 PM" src="https://user-images.githubusercontent.com/8196343/88488810-98698780-cf44-11ea-82b8-19d0cc231ad5.png">

<b>Negative Skewness</b>: A curve or data is negatively skewed when the long tail is on the left hand side of the peak. In such kind of data, the mean also stays on the left hand side of the peak. 

<b>Normal Distribution</b>: A curve or data is not skewed at all. 
- It is perfectly symmetrical and the mean is exactly at the peak. If you a draw line in the middle, the left hand side will be a replica of right hand side.

<b>Positive Skewness</b>: A curve or data is negatively skewed when the long tail is on the right hand side of the peak.

Positive or negative skewed data interfer with running a parametric statistics. 


### Statistical techniques to make the data normally distributed:
1. Log Transformation
	- Applicable for right skewness. 
	- Cannot be applied to zero or negative values. If you apply log transformation on 0 value, you will get negative value.
	1.1. Log10x
	1.2. Lnx
	1.3. Log2x

2. Inverse Transformation
3. Square Root Transformation




