import numpy as np;
import pandas as pd

df=pd.read_csv("mathematicians.csv")
causes_death=df["manner of death"].dropna();
causes_death=np.array(causes_death)
#print(causes_death[0])

def convert_array(word):
	word=word.replace("["," ");
	word=word.replace("]"," ");
	word=word.replace("'","");
	array=word.split(",");
	for i in range(len(array)):
		array[i]=array[i].lstrip();
	return array;
	


def counter(array):
	array=array.dropna();
	array=np.array(array);
	count={};
	for i in range(len(array)):
		for death in convert_array(array[i]):
			if death in count:
				count[death]+=1;
			else:
				count[death]=1;
	print();
	for death in count:
		print(death,count[death]);
	return count






# for death in count:
	# print(death,count[death]);
	
#counter(df["manner of death"]);
#counter(df["instance of"]);
#counter(df["award received"])
#counter(df["country of citizenship"])