with all_transactions as (
    select 
        to_char(trans_date, 'YYYY-MM') as month,
        country,
        count(id) as trans_count,
        sum(amount) as trans_total_amount
    from transactions
    group by to_char(trans_date, 'YYYY-MM'), country
), approved_transactions as (
    select 
        to_char(trans_date, 'YYYY-MM') as month,
        country,
        count(id) as approved_count,
        sum(amount) as approved_total_amount
    from transactions
    where state = 'approved'
    group by to_char(trans_date, 'YYYY-MM'), country
)
    select 
        all_transactions.month,
        all_transactions.country,
        all_transactions.trans_count,
        coalesce(approved_transactions.approved_count, 0) as approved_count,
        all_transactions.trans_total_amount,
        coalesce(approved_transactions.approved_total_amount, 0) as approved_total_amount
    from all_transactions
    left join approved_transactions
        on coalesce(all_transactions.month, 'X') = coalesce(approved_transactions.month, 'X')
        and coalesce(all_transactions.country, 'X') = coalesce(approved_transactions.country, 'X')
    ;