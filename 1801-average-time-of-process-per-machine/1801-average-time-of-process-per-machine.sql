# Write your MySQL query statement below
select machine_id, 
    round(avg(case when activity_type = 'start' Then -timestamp
    else timestamp END) * 2, 3) as processing_time
from Activity
group by machine_id;