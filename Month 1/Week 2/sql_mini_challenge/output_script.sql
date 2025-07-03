SELECT
	o.order_id,
	o.order_date,
	SUM(oi.quantity) AS total_items_ordered,
	ROUND(SUM(oi.unit_price * oi.quantity),2) AS total_revenue
FROM orders AS o
LEFT JOIN order_items AS oi
	ON oi.order_id = o.order_id
GROUP BY 
	o.order_id, 
	o.order_date
HAVING ROUND(SUM(oi.unit_price * oi.quantity),2) > 100
ORDER BY total_revenue DESC;