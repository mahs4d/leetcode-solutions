with cte1 as (
    select *, id - row_number() over (order by id) as grp
    from stadium
    where people >= 100
), cte2 as (
    select id, count(id) over (partition by grp) as cnt
    from cte1
)
    select id, visit_date, people from cte1
    where  id in (
        select id from cte2 where cnt >= 3
    )