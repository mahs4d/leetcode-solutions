with customer_distinct_products as (
    select customer_id, count(distinct product_key) as products_count
    from Customer
    group by customer_id
)
    select
        customer_id
    from customer_distinct_products
    where products_count = (select count(product_key) from Product)