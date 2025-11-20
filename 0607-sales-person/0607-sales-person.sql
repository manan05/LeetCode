with red_sales as (
    select sales_id
    from company c
    join orders o 
    on c.com_id = o.com_id
    where c.name = 'RED'
)

select sp.name as name
from salesPerson sp
left join red_sales rs
on sp.sales_id = rs.sales_id
where isnull(rs.sales_id)