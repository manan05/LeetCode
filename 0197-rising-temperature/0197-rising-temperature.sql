# Write your MySQL query statement below
with cte as (
    select w.*,
    lag(recordDate, 1) over (order by recordDate) as prevDate,
    lag(temperature, 1) over (order by recordDate) as prevTemp
    from weather w
)

select id as Id
from cte
where datediff(recordDate, prevDate) = 1
and temperature > prevTemp;