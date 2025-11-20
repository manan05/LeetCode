# Write your MySQL query statement below
select u.user_id as buyer_id, join_date, count(order_date) as orders_in_2019
from users u
left join orders o
on u.user_id = o.buyer_id
and order_date >= '2019-01-01' and order_date <= '2019-12-31'
group by u.user_id