SELECT date_info.case_id, date_info.sent_date, supplier_info.supplier_name
FROM date_info
JOIN main ON main.case_id = date_info.case_id
JOIN supplier_info ON main.supplier_id = supplier_info.id
where main.req_supplier = true and sent_date is not null;