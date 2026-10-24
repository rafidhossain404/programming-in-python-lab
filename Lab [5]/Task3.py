
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
def display_report(arr):
    print("Id: ",arr[0])
    print("Name: ",arr[1])
    print("Average:",arr[2])
    print("Performance: "+ arr[3])


 
arr = (
  [201, "Amina", [78, 85, 90]],
  [202, "Rahim", [65, 70, 68]],
  [203, "Nadia", [92, 88, 95]],
  [204, "Hasan", [55, 60, 65]],
  [205, "Tania", [80, 80, 80]]
 )
X=str(input("Enter students name: "))
sum=0
for i in arr:
    if (X==i[1]):
      name=X
      
      arr1=[i[0],i[1],calculate_average(*i[2],i[1]),classify_performance(calculate_average(*i[2],i[1]))]
      display_report(arr1)
      break
else:print("Student no found")

      
