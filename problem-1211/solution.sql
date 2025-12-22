select
    query_name,
    round(avg(rating::decimal / position), 2) as quality,
    round(((sum(case when rating < 3 then 1 else 0 end)::decimal / count(*)) * 100), 2) as poor_query_percentage
from queries
group by query_name;
