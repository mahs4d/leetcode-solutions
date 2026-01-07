select
    prices.product_id,
    coalesce(round(sum(prices.price * unitssold.units)::decimal / sum(unitssold.units), 2), 0) as average_price
from prices
left join unitssold 
       on unitssold.product_id = prices.product_id
       and unitssold.purchase_date >= prices.start_date 
       and unitssold.purchase_date <= prices.end_date
group by prices.product_id;
