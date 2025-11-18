# Write your MySQL query statement below
with CTE as
(
    select id, recordDate, temperature,
    lag(temperature, 1) over (order by recordDate) as PreviousTemp,
    lag(recordDate, 1) over (order by recordDate) as PreviousDate
    from Weather
)
select id
from CTE
where temperature > PreviousTemp
and recordDate = Date_add(PreviousDate, interval 1 year);