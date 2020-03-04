## 3. Previewing A Table Using SELECT ##

SELECT * FROM recent_grads LIMIT 10


## 4. Filtering Rows Using WHERE ##

SELECT Major, ShareWomen FROM recent_grads WHERE ShareWomen<0.5

## 5. Expressing Multiple Filter Criteria Using AND ##

SELECT Major, Major_category, Median, ShareWomen FROM recent_grads WHERE ShareWomen>=0.5 AND Median>50000

## 6. Returning One of Several Conditions With OR ##

SELECT Major, Median, Unemployed FROM recent_grads WHERE Median>=10000 OR Unemployed<=1000 LIMIT 20

## 7. Grouping Operators With Parentheses ##

SELECT Major, Major_category, ShareWomen, Unemployment_rate FROM recent_grads WHERE (Major_category='Engineering') and (ShareWomen>=0.5 or Unemployment_rate<0.051)

## 8. Ordering Results Using ORDER BY ##

SELECT Major, ShareWomen, Unemployment_rate FROM recent_grads WHERE ShareWomen>0.3 and  Unemployment_rate<0.1 ORDER BY ShareWomen DESC

## 9. Practice Writing A Query ##

SELECT Major_category, Major, Unemployment_rate FROM recent_grads WHERE Major_category='Engineering' OR Major_category='Physical Sciences' ORDER BY Unemployment_rate ASC