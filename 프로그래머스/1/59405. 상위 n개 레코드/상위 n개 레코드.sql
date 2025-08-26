-- 코드를 입력하세요
select name
from
    (select name, rownum as rn
    from (SELECT *
          from ANIMAL_INS
          order by DATETIME)
    )
where rn = 1;