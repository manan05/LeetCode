# Write your MySQL query statement below

with prevData as 
(
    select w.*,
    lag(temperature) over(order by recordDate) as prevTemp,
    lag(recordDate) over(order by recordDate) as prevDate
    from weather w
)

select id
from prevData
where temperature > prevTemp
and datediff(recordDate, prevDate) = 1