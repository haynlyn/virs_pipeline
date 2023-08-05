INSERT INTO inspections (vehicle_id, inspection_date, vehicle_org_id, org_name, inspection_period_id, inspection_passed)
VALUES (:vehicle_id, :inspection_date, :vehicle_org_id, :org_name, :inspection_period_id, :inspection_passed)
ON CONFLICT (vehicle_id, inspection_date)
DO UPDATE SET
    vehicle_org_id = EXCLUDED.vehicle_org_id,
    org_name = EXCLUDED.org_name,
    inspection_period_id = EXCLUDED.inspection_period_id,
    inspection_passed = EXCLUDED.inspection_passed;
