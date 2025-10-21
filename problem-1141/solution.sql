select activity_date as day, count(distinct user_id) as active_users 
from Activity
where activity_date <= '2019-07-27' and activity_date > ('2019-07-27'::date - interval '30 days')::date
group by activity_date
having count(distinct user_id) > 0
order by activity_date