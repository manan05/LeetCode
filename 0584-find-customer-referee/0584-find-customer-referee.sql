# Write your MySQL query statement below
select name
from customer
where referee_id != 2
or isNull(referee_id);