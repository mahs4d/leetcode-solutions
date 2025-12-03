select
    product_id,
    product_name
from product
where exists (
    select 1 from sales 
    where sales.product_id = product.product_id
      and sales.sale_date >= '2019-01-01'::date 
      and sales.sale_date <= '2019-03-31'::date
)
and not exists (
    select 1 from sales 
    where sales.product_id = product.product_id
      and (
        sales.sale_date < '2019-01-01'::date 
        or sales.sale_date > '2019-03-31'::date
    )
);
