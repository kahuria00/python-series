import os
import pandas as pd



current_directory = os.path.realpath(
	os.path.join(os.getcwd(), os.path.dirname(__file__)))

csv_list = ["transaction_data_1.csv",'transaction_data_2.csv','transaction_data_3.csv']


for sheet in csv_list:
	if sheet == "transaction_data_1.csv":
		df1 = pd.read_csv(f"{current_directory}/{sheet}") 
		# df1 = df1.drop('transaction_amount',axis=1)
		df1=df1.sort_values(by=["customer_id"],ascending=True)

		df1=df1.groupby(["customer_id"]).count().max(level=0)
		# df1 =df1["customer_id"].value_counts()

		print(df1)


	elif sheet == "transaction_data_2.csv":
		df2 = pd.read_csv(f"{current_directory}/{sheet}")
		df2 = pd.read_csv(f"{current_directory}/{sheet}") 
		# df2= df2.drop('transaction_amount',axis=1)
		df2=df2.sort_values(by=["customer_id"],ascending=True)

		df2=df2["customer_id"].value_counts()
		

		print(df2)
	elif sheet == "transaction_data_3.csv":
		df3 = pd.read_csv(f"{current_directory}/{sheet}")
		df3 = pd.read_csv(f"{current_directory}/{sheet}") 
		# df3 = df3.drop('transaction_amount',axis=1)
		df3=df3.sort_values(by=["customer_id"],ascending=True)

		df3 =df3["customer_id"].value_counts()

		print (df3)
		









