# Write your MySQL query statement below

SELECT v.customer_id, COUNT(v.visit_id) AS count_no_trans
FROM Visits v
LEFT JOIN Transactions t
ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL # Need to use IS NULL instead of "= null"
GROUP By customer_id # Need to use alongside visit_id to determine how the count is grouped up. We are summing up visit_id that has the same customer_id, therefore customer_id is how we are grouping up our COUNT function