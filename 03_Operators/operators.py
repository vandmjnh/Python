#Declare your age as integer variable
age = 19
#Declare your height as a float variable
height = 1.67
#Declare a variable that store a complex number
complexNumber = 3 + 4j
#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = int(input("Enter base: "))
height = int(input("Enter height: "))
print("The area of the triangle is: ", 0.5 * base * height)
#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
sideA = int(input("Enter side a: "))
sideB = int(input("Enter side b: "))
sideC = int(input("Enter side c: "))
print("The perimeter of the triangle is: ", sideA + sideB + sideC)
#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input("Enter length: "))
width = float(inpur("Enter width: "))
print("The area of the rectangle is: ", length * width)
print("The perimeter of the rectangle is: ", 2 * (length + width))
#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = float(input("Enter radius: "))
print("The area of the circle is: ", 3.14 * radius * radius)
print("The circumference of the circle is: ", 2 * 3.14 * radius)
#Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope8 = 2
x_intercept = -2 / 2
y_intercept = 2 * 0 - 2
#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
slope9 = (10 - 2) / (6 - 2)
#Compare the slopes in tasks 8 and 9.
slope8 < slope9
#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0
x = -3
y = x ** 2 + 6 * x + 9
#Find the length of 'python' and 'jargon' and make a falsy comparison statement.
len("python") == len("jargon")
#Use and operator to check if 'on' is found in both 'python' and 'jargon'
'on' in 'python' and 'on' in 'jargon'
#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
'jargon' in 'I hope this course is not full of jargon'
#There is no 'on' in both dragon and python
'on' not in 'dragon' and 'on' not in 'python'
#Find the length of the text python and convert the value to float
str(float(len('python')))
#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = int(input("Enter a number: "))
print("The number is even: ", number % 2 == 0)
#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
7 // 3 == int(2.7)
#Check if type of '10' is equal to type of 10
type('10') == type(10)
#Check if int('9.8') is equal to 10
int('9.8') == 10
#Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input("Enter hours:"))
rate_per_hour = int(input("Enter rate per hour: "))
print("Your weekly earning is: ", hours * rate_per_hour)
#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter number of years you have lived: "))
print("You have lived for ", years * 365 * 24 * 60 * 60, " seconds.")
#Write a Python script that displays the following table
table = """1 1 1 1 1
           2 1 2 4 8
           3 1 3 9 27
           4 1 4 16 64
           5 1 5 25 125"""
print(table)
