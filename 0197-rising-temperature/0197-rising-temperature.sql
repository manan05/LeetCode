# Write your MySQL query statement below
-- select w2.id as Id
-- from Weather w1, Weather w2
-- where datediff(w2.recordDate, w1.recordDate) = 1
-- and w2.temperature > w1.temperature;


WITH PreviousWeatherData as
(
    select id, recordDate, temperature,
    lag(temperature, 1) over (order by recordDate) as PreviousTemp,
    lag(recordDate, 1) over (order by recordDate) as PreviousRecordDate
    from Weather
)

select id
from PreviousWeatherData
where temperature > PreviousTemp
and recordDate = Date_add(PreviousRecordDate, Interval 1 day);