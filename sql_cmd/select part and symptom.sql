select
part,
symptom_des
from 
failure_code
left join failure_parts on failure_parts.symptom_id = failure_code.symptom_id;