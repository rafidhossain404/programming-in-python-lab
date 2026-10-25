
def calculate_average(x,y,z,name):
    sum=0
    avg=0
    sum=x+y+z
    avg=round(sum/3,2)
    return "Average number of "+name+" is: "+ str(avg)


 
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
      print(calculate_average(x,y,z,name))
      break
else:print("Student no found")

      
