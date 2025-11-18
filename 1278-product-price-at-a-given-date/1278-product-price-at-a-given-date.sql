with date_less_than_given as (
	select p.*,
    row_number() over(partition by product_id order by change_date desc) as rn
    from products p
    where change_date <= '2019-08-16'
), 
	distinct_prod as (
	select distinct product_id
    from products
)

select dp.product_id, ifnull(dg.new_price, 10) as price
from distinct_prod dp
left join date_less_than_given dg
on dp.product_id = dg.product_id
and dg.rn = 1

