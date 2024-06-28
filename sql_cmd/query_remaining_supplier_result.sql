select date_info.case_id, finish_date
from date_info
left join main on date_info.case_id = main.case_id
where main.req_supplier is true and finish_date is null;
