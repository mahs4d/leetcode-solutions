with cte1 as (
    select 
        s.id, s.visit_date, s.people,
        b_1.people as b_1p,
        b_2.people as b_2p,
        f_1.people as f_1p,
        f_2.people as f_2p
    from stadium s
    left join stadium b_1 on b_1.id = s.id - 1
    left join stadium b_2 on b_2.id = s.id - 2
    left join stadium f_1 on f_1.id = s.id + 1
    left join stadium f_2 on f_2.id = s.id + 2
)
    select id, visit_date, people
    from cte1
    where
        people >= 100
        and (
            (b_1p >= 100 and b_2p >= 100) or
            (b_1p >= 100 and f_1p >= 100) or
            (f_1p >= 100 and f_2p >= 100)
        )