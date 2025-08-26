select name
from (select name
      from ANIMAL_INS
      order by DATETIME)
where rownum = 1;