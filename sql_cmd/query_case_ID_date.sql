select main.case_id, main.customer, date_info.production_date, date_info.install_date, date_info.problem_date
from main
join date_info on main.case_id = date_info.case_id
where problem_id = 1;
