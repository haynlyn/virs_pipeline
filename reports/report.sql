WITH base AS (
	SELECT org_name, COUNT(vehicle_id) tot_v, SUM(CASE WHEN inspection_passed = FALSE THEN 1 ELSE 0 END) failed_v
	FROM inspections
	GROUP BY 1
)
SELECT org_name, tot_v, failed_v
FROM base
ORDER BY (failed_v::float / tot_v) DESC
LIMIT 3
;
