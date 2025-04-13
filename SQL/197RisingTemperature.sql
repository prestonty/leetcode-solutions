# Write your MySQL query statement below
SELECT w2.id as Id
FROM Weather w1
LEFT JOIN Weather w2
ON DATEDIFF(w2.recordDate, w1.recordDate) = 1 # DATEDIFF finds difference between two dates. if w2 - w1 = 1 (differs by 1 day), then w2 is current, w1 is previous
WHERE w2.temperature > w1.temperature;

# I need to start studying sql seriously, not that easy anymore without looking at soln cause idk that the tools exist in first place