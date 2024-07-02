SELECT s.case_id, s.des, d.finish_date, su.supplier_name, m.customer
FROM supplier_part s
JOIN date_info d ON s.case_id = d.case_id
JOIN main m ON s.case_id = m.case_id
JOIN supplier_info su ON m.supplier_id = su.supplier_id;
