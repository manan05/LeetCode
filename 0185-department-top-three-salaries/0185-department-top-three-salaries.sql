# Write your MySQL query statement below
with rank_salary as (
    select e.*,
    dense_rank() over (partition by departmentId order by salary desc) as dept_sal
    from employee e
)

select d.name as Department, rs.name as Employee, rs.salary as Salary
from department d
join rank_salary rs
on rs.departmentId = d.id
where dept_sal <= 3