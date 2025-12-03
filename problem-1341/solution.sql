with highest_user_cte as (
    select users.user_id, users.name as user_name, count(movierating.movie_id)
    from users
    left join movierating on movierating.user_id = users.user_id
    group by users.user_id, users.name
    order by count(distinct movierating.movie_id) desc, users.name asc
    limit 1
), highest_movie_cte as (
    select movies.movie_id, movies.title as movie_title, avg(movierating.rating)
    from movies
    left join movierating on movierating.movie_id = movies.movie_id
    where movierating.created_at >= '2020-02-01'::date 
      and movierating.created_at < '2020-03-01'::date
    group by movies.movie_id, movies.title
    order by avg(movierating.rating) desc, movierating.title asc
    limit 1
)
    select user_name as results from highest_user_cte
    union all
    select movie_title as results from highest_movie_cte
;
