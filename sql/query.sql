-- S2a: Total delay days by service type

SELECT
    r.service_type,
    SUM(
        CASE
            WHEN d.actual_days > d.promised_days
            THEN d.actual_days - d.promised_days
            ELSE 0
        END
    ) AS total_delay_days
FROM deliveries AS d
INNER JOIN routes AS r
    ON d.route_id = r.route_id
GROUP BY r.service_type
ORDER BY total_delay_days DESC;

-- S2b: Routes whose total delay days are greater than 8

SELECT
    d.route_id,
    SUM(
        CASE
            WHEN d.actual_days > d.promised_days
            THEN d.actual_days - d.promised_days
            ELSE 0
        END
    ) AS total_delay_days
FROM deliveries AS d
GROUP BY d.route_id
HAVING SUM(
    CASE
        WHEN d.actual_days > d.promised_days
        THEN d.actual_days - d.promised_days
        ELSE 0
    END
) > 8
ORDER BY total_delay_days DESC;

-- S2c: Top 2 hubs by total delay days

SELECT
    d.hub,
    SUM(
        CASE
            WHEN d.actual_days > d.promised_days
            THEN d.actual_days - d.promised_days
            ELSE 0
        END
    ) AS total_delay_days
FROM deliveries AS d
GROUP BY d.hub
ORDER BY total_delay_days DESC, d.hub ASC
LIMIT 2;

-- Diagnostic: unmatched route IDs

SELECT
    d.route_id,
    COUNT(*) AS unmatched_records
FROM deliveries AS d
LEFT JOIN routes AS r
    ON d.route_id = r.route_id
WHERE r.route_id IS NULL
GROUP BY d.route_id;