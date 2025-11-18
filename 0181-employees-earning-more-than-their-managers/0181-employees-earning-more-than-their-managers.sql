# Write your MySQL query statement below
select e.name as Employee
from employee e join employee em
on e.managerId = em.id
where e.salary > em.salary;