# Write your MySQL query statement below
with cte as 
(
    select o.sales_id
    from company c
    join orders o
    on c.com_id = o.com_id
    where c.name = 'RED'
)


select name
from salesPerson sp
left join cte ct
on sp.sales_id = ct.sales_id
where isNull(ct.sales_id)