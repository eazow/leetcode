# Write your MySQL query statement below
select employee1.name as Employee from employee as employee1, employee as employee2 
where employee1.managerId=employee2.id and employee1.salary > employee2.salary