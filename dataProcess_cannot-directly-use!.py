import pandas as pd
#user_data = pd.read_csv("/Users/Maverick/Desktop/CTR模型数据集/user_profile.csv")
#user_data.fillna(0, inplace=True)
#user_data_col = ['cms_segid', 'cms_group_id', 'final_gender_code', 'age_level', 'pvalue_level', 'shopping_level', 'occupation', 'new_user_class_level ']
#
#ad_feature= pd.read_csv("/Users/Maverick/Desktop/CTR模型数据集/ad_feature.csv")
#ad_feature.fillna(0, inplace=True)
#ad_feature_col = ['cate_id', 'campaign_id', 'customer', 'brand', 'price']
#
##raw_sample= pd.read_csv("/Users/Maverick/Desktop/raw_sample.csv")
#raw_sample= open("/Users/Maverick/Desktop/CTR模型数据集/raw_sample.csv",'r')
#
#data = open("/Users/Maverick/Desktop/data_ctr.txt",'w')
#
#c = 0
#for line in raw_sample:
#	lineList = line.split(",")
#	user_ID = int(lineList[0])
#	ad_ID = int(lineList[2])
#	
#	#find things
#	userPart = user_data[user_data["userid"]==user_ID]
#	adPart = ad_feature[ad_feature["adgroup_id"]==ad_ID]
#	
#	if userPart.empty or adPart.empty:
#		continue
#	
#	#combinte data
#	outputLine = lineList[-1][:-1] + " "
#	for column in user_data_col:
#		outputLine += userPart[column].to_string(index=False) + ","
#		
#	for column in ad_feature_col:
#		outputLine += adPart[column].to_string(index=False) + ","
#		
##	print(outputLine)
#	data.write(outputLine[:-1]+"\n")
#	
#raw_sample.close()
#data.close()

#df = pd.read_csv("/Users/Maverick/Desktop/data_ctr.csv")
#df.drop_duplicates().to_csv("/Users/Maverick/Desktop/data_ctr_no_duplicated.csv", index=False)

df = pd.read_csv("/Users/Maverick/Desktop/data_ctr_no_duplicated.csv")
ID = ['cms_segid', 'cms_group_id', 'cate_id', 'campaign_id', 'customer', 'brand']

allCol = ['cms_segid','cms_group_id', 'final_gender_code', 'age_level', 'pvalue_level', 'shopping_level', 'occupation', 'new_user_class_level', 'cate_id', 'campaign_id', 'customer', 'brand', 'price']

print(df['age_level'].unique())

#for i in allCol:
#	print(i)
#	print(len(df[i].unique()))
##	print(float(df[i].max())-float(df[i].min()))
#	print(int(df[i].max()), int(df[i].min()))
#	print("====================")








