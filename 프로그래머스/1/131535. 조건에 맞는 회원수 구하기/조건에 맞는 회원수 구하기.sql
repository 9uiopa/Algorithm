-- 코드를 입력하세요
SELECT count(*) as users
from USER_INFO 
where extract(year from JOINED) = 2021 and (AGE >= 20 and AGE<=29)