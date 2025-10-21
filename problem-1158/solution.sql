select 
    users.user_id as buyer_id,
    users.join_date as join_date,
    count(orders) as orders_in_2019
from users
left join orders on orders.buyer_id = users.user_id and orders.order_date between '2019-01-01' and '2020-01-01'
group by users.user_id, users.join_date
;