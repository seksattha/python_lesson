SELECT date_info.case_id, supplier_info.supplier_name
FROM date_info
JOIN main ON date_info.case_id = main.case_id
JOIN supplier_info ON supplier_info.id = main.supplier_id
WHERE date_info.sent_date IS NULL AND main.req_supplier = TRUE;