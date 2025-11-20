select q1.person_name 
from Queue q1
left join Queue q2 on q2.turn <= q1.turn
group by q1.person_name
having sum(q2.weight) <= 1000
order by sum(q2.weight) desc
limit 1;
