with cte as (
    select 
        visited_on,
        sum(amount) as amount,
        row_number() over (order by visited_on) row_n
    from customer
    group by visited_on
)
select
    c1.visited_on,
    sum(c2.amount) amount,
    round(avg(c2.amount), 2) average_amount
from cte c1
left join cte c2 on c2.row_n between c1.row_n - 6 and c1.row_n
where c1.row_n >= 7
group by c1.visited_on, c1.amount
order by c1.visited_on asc;
