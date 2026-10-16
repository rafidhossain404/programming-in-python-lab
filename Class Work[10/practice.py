def bonus_score(score,bonus=5):
 if score+bonus>100:
  return "Invalid score" 
 
 return score+bonus

x =float(input("Enter the number: ")) 
y=float(input("Enter the score: "))
print("score after adding bonus: ",bonus_score(y,x)) 
print
