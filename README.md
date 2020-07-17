#Abstract
##The model is based on Embedding+MLP, in MLP the model combines 3 parallel sub-model(DNN, CIN, AutoInt)  
##The 3 parallel parts share the same embedded input, and use a combination layer to get the CTR.(pretty much like the xDeepFM model, this model is actually a fork of it)

#Code
##Code of this model is written and run in jupyter notebook, build the model requries only tensorflow2.1.0 and numpy(yeah, nothing else!!!!)  
##And to run the run and simply analysis the results requires some commonly seen lib, they are all listed in the head of the code file.  

#Dataset
##Dataset of this model comes from here: https://tianchi.aliyun.com/dataset/dataDetail?dataId=56
##After you donwload the dataset from the url, you need some basic data dig(I used pandas)
##Short story, you need your dataset feeding to model looks like this:(here are some .csv examples)

label,cms_segid,cms_group_id,final_gender_code,age_level,pvalue_level,shopping_level,occupation,new_user_class_level,cate_id,campaign_id,customer,brand,price
0,0,10,1,4,0.0,3,0,1.0,6281,19451,96837,259125.0,99.0
0,7,2,2,2,1.0,3,0,2.0,4301,248040,202257,339499.0,129.0
0,0,2,2,2,0.0,3,0,0.0,1540,408389,63260,393737.0,38.0
0,0,3,2,3,2.0,3,0,0.0,5993,126962,156852,257537.0,15.0
0,0,4,2,4,0.0,3,0,3.0,24,338688,18656,0.0,5.3
......

##there is a dataProcess.py file, it's what I used to dig the data, only as a reference, cannot be directly use!!

###the code is not using any GPU computation(don't ask, I'm too poor and using AMD and haven't friguring out how to run tf on AMD gpus....  
