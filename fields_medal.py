import numpy as np;
import pandas as pd;
from datetime import date
from math import isnan
from statistics import mode,mean;
from copy import deepcopy
#read in mathmaticians.cdv
df=pd.read_csv("mathematicians.csv");
#Gets rid of instance of attribute
df=df.drop("instance of",axis=1)

death_day=deepcopy(df["day of death"]);
death_month=deepcopy(df["month of death"]);
death_year=deepcopy(df["year of death"]);
death_date=np.zeros(len(death_year));

for i in range(len(death_year)):
	if not isinstance(death_year[i],str):
		continue;
	if death_year[i][-1]=="s":
		death_year[i]=death_year[i][:-1]
		

impute_day= int(round(mode(death_day.dropna())));
impute_month= mode(death_month.dropna());
impute_year= int(round(mean(list(map(int,death_year.dropna())))))

print(impute_day,impute_month,impute_year)

for i in range(len(death_date)):
	if isnan(death_day[i]):
		death_day[i]=impute_day;
	if not isinstance(death_month[i],str):
		death_month[i]=impute_month;
	if  not isinstance(death_year[i],str):
		death_year[i]=str(impute_year);
