
def calculate_average(x,y,z,name):
    sum=0
    avg=0
    sum=x+y+z
    avg= round(sum/3,2)
    return avg
def classify_performance(average):
  if(average >= 80): return "Exelent"
  elif(average >= 70): return "Good"
  elif(average >= 60):return "Satisfactory"
  else:return " Needs Improvemen"
 
arr = (
  [201, "Amina", [78, 85, 90]],
  [202, "Rahim", [65, 70, 68]],
  [203, "Nadia", [92, 88, 95]],
  [204, "Hasan", [55, 60, 65]],
  [205, "Tania", [80, 80, 80]]
 )
X=str(input("Enter students name: "))
sum=0
for i in range (0,5):
    if (X==arr[i][1]):
      name=X
      x=arr[i][2][0]
      y=arr[i][2][1]
      z=arr[i][2][2]

      print("Average number of "+name+" is: "+ str(calculate_average(x,y,z,name)))
      print("Performance: ",classify_performance(calculate_average(x,y,z,name)) )

      break
else:print("Student no found")

      
