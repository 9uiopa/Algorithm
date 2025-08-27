-- 코드를 입력하세요
select DATETIME

from
    (SELECT DATETIME
    from ANIMAL_INS
    order by DATETIME)
where rownum = 1;