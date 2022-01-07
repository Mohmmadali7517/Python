
def Prime(no):
	bFlag=True
	for i in range(2,no):
		if((no%i)==0):
			bFlag=False
			break
	return bFlag
	
def Maximum(no1,no2):
	if(no1>no2):
		return no1
	else:
		return no2