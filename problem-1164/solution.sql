with cte as (
    select
        product_id, new_price as price
    from products p1
    where change_date <= '2019-08-16'::date
    and   change_date = (
        select max(p2.change_date) from products p2
        where  p2.product_id = p1.product_id
        and    p2.change_date <= '2019-08-16'::date
    )
)
    select distinct
        products.product_id as product_id,
        coalesce(cte.price, 10) as price
    from products
    left join cte on products.product_id = cte.product_id;
