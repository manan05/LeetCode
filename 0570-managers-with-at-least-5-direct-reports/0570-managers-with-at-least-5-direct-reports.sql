# Write your MySQL query statement below
with cte as (
    select managerId, count(managerId)
    from employee
    group by managerId
    having count(managerId) >= 5
)


select name
from employee e
join cte ct
on e.id = ct.managerId