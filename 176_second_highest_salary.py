# Write your MySQL query statement below
select max(Salary) as SecondHighestSalary from Employee where Salary < (select max(salary) from Employee);