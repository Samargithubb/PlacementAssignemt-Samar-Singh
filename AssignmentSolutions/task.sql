/* 11. Create Student Table with ID as Primary Key and NOT NULL , Name as 20 Characters ,Age as Int value both are NOT NULL and Address have  25 charter And Insert Any 5 Records?  
Note: Add "GitHub" link for the solution if required*/

create table Student(
ID int Primary key,
Name varchar(20),
Age int(3),
Address varchar(25));

insert into Student values(01,"Samar Singh", 24, "Khera Nalagarh 12323"),
(02,"amar Singh", 23, " Nalagarh 12323"),(03,"ar Singh", 22, "Khera Nalagarh 123232323"),
(04,"ajay Singh", 21, "Khera Nalagarh 123567323"),(05,"vijay Singh", 20, "Khera Nalagarh 123634323");

/*12.  Write an SQL query to find the youngest student in the "student" table ? Note: Add 
"GitHub" link for the solution if required   */
select * from student
order by AGe desc
limit 1;

/* 13.  Write an SQL query to retrieve the names and addresses of all persons from the "Person" table along with their corresponding addresses from the "Address" table.
Note: Add "GitHub" link for the solution if required*/
select firstname, lastname, address from Student 
inner join Addresstable
using(personID);

/*14.  Write an SQL query to fetch the second highest number from the 
"student" table.? Note: Add "GitHub" link for the solution if required  */

select * from student
order by Hnumber desc
limit 1,1;

/*15.  SQL Quary to get the nth highest salary from Employee table Note:
 Add "GitHub" link for the solution if required  */
 select * from employees
 order by salary
 limit 1;
 
 

