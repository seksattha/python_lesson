update main
set name = (

select t1.name
from t1
where t1.case_id = main.case_id


);