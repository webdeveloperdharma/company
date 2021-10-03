# company

Python Questions :
I have a couple of problems that I would like you to work progressively on paper using python code without any import modules.  

1.	If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples 
		is 23. Find the sum of all the multiples of 3 or 5 below 1000. (Answer: 233168) 
		(solution code attached: problem_1_solution_code.py)
	print(sum([i for i in range(1,1000) if i%3 == 0 or i%5 == 0]))
		
2.	Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, 
		the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... By considering the terms in the Fibonacci sequence 
		whose values do not exceed four million, find the sum of the even-valued terms. (Answer: 4613732) 
		(solution code attached: problem_2_solution_code.py)
		
Once you have them written on paper, can you put that code on the system and make changes as required 
		and share the changed code as well.
 
 
Django Questions : 
 
1. What command line interface instructions are required to create a django project called
‘company’ and application called ‘staff’?

Sol : Command to create a project in django : "django-admin startproject company"
	  Command to create an application 		: "python manage.py startapp staff"
	  
	  

2. models.py - Please use the django ORM framework to create the tables below.
Employee table
Employee name
Department
Email
Date of birth
Picture
Department table
Department name
Manager (employee)

			


 
3. admin.py - Please implement the code to allow the admin interface to be used to
manipulate the database for both the Employee and Department objects. When viewing
the Employee objects you should be able to filter by department and date of birth. 

When creating/editing a Department object there should be inlines for each of the Employee objects in the Department.
		
	
 
4. What command line interface instructions are required to be able to test the admin interface after you have completed #2 and #3 above?
Sol : 1. Create an admin user using the command : "python manage.py createsuperuser"
	  2. After the above command we have to type username, email_id and password then it creates an admin user.
	  3. To access the admin interface in local server, we have to type : 127.0.0.1:8000/admin
		
 
5. views.py (Department) - Using generic class-based views please write the following views for the Department objects: list and detail
	
	
6. forms.py - Create a ModelForm class to create an Employee object only entering the Employee name and Department fields.
 
7. views.py (Employee) - Using a generic class-based view use the form in #6 in a create view for Employee objects. 
		Is your models.py class for Employee compatible with the form and view?
Sol : Yes the Employee model is compatible with both form and view. Employee model is being used in ModelForm and this 
				ModelForm is being used for class based CreateView

 
8. What template files would be required for the views in #5 and #7 to work? Where would you put these files?
Sol :	For #5 : 'department_list.html' is required for the list of Department objects
		For #5 : 'department_detail.html' is required for the details of individual Department object.
		For #7 : 'employee_form.html' is required for the displaying the form and creating a user.
		
		All these files were kept in "company\staff\templates" folder i.e. inside the staff application.
		
		
