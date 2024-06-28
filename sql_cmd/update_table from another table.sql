SET SQL_SAFE_UPDATES = 0;

update employee e
join employee_a ea
on e.id = ea.staff_id
set e.fname = ea.fname,
	e.lname = ea.surname;
    
SET SQL_SAFE_UPDATES = 1;