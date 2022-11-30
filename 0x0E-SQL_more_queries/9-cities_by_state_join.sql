-- Script using JOIN command
SELECT id, name FROM cities c
FULL OUTER JOIN states s
ON c.state_id = s.id
