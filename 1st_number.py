#program to find the percentage of students

english=input("enter the marks for english")
math=input("\nenter the marks for math")
nepali=input("\nenter the marks for nepali")
science=input("\nenter the marks for science")
total=english+math+nepali+science
print total

def percentage(a):
     return (a)*100.0/400


print percentage(total)


