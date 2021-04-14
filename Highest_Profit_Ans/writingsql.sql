CREATE TABLE highest_profit (
	Year int,
	Rank int,
	Company TEXT,
	revenue float,
	profit float
);

SELECT DISTINCT * from highest_profit 
ORDER by profit DESC 
LIMIT 20;