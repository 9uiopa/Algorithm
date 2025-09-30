-- 코드를 입력하세요
SELECT hour(DATETIME) as hour, count(hour(DATETIME)) as count
from ANIMAL_OUTS 
group by hour
having hour > 8 and hour < 20
order by hour