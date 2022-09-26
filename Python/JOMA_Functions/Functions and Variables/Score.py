#Functions

def score(total,correct,wrong):
	# your code here
	total_score = correct*2 + wrong*1
	points = total_score/(total*2)
	percentage_score = points* 100	
	return percentage_score

print(score(20,20,0)) 
print(score(20,15,0)) 
print(score(20,15,5)) 
print(score(20,10,5))
print(score(20,0,20))  

def score75(total,correct,wrong):
	#your code here
	new_Correct = min(correct,total*0.75)
	new_Wrong = min(max(total*0.75-correct,0),wrong)
	new_Total = total * 0.75
	return score(new_Total,new_Correct,new_Wrong);

print(score75(20,20,0)) 
print(score75(20,15,0)) 
print(score75(20,15,5)) 
print(score75(20,10,5))
print(score75(20,0,20))
