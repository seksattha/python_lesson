
select  main.customer, problem.problem_name
from
main
left join problem on main.problem_id = problem.id;
 