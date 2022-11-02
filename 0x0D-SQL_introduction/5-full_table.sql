-- A script that prints full description of the first_table from the database
SELECT 
	*
FROM
	INFORMATION_SCHEMA.COLUMNS
WHERE
	TABLE_NAME = 'first_name';
