with cte as (
    select
        account_id,
        case
            when income < 20000 then 'Low Salary'
            when income <= 50000 then 'Average Salary'
            else 'High Salary'
        end as category,
        income
    from Accounts
)
    select
        t.category,
        count(account_id) as accounts_count
    from (values ('Low Salary'), ('Average Salary'), ('High Salary')) as t(category)
    left join cte on cte.category = t.category
    group by t.category;
