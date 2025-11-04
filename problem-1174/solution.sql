with cte1 as (
    select
        delivery_id,
        customer_id,
        case
            when order_date = customer_pref_delivery_date then true
            else false
        end as is_immediate,
        case
            when rank() over (partition by customer_id order by order_date asc) = 1 then true
            else false
        end as is_first
    from delivery
), cte2 as (
    select count(*) as cnt from cte1 where is_immediate = true and is_first = true
), cte3 as (
    select count(*) as cnt from cte1 where is_first = true
)
    select 
        round(((cte2.cnt::float / cte3.cnt) * 100)::numeric, 2) as immediate_percentage
    from cte2
    join cte3 on true