import psycopg3

#What are the most popular three articles of all time?
first_query = """
select title, count(*) as num from articles join log on concat('/article/', articles.slug) = log.path 
group by articles.title order by num desc limit 3;
"""

#Who are the most popular article authors of all time?
second_query = """
select author.name, count(*) as num from articles join authors on articles.author = authors.id join log on concat('/article/', articles.slug) = log.path where log.status like '%200%' group by authors.name order by num; 
"""

#On which days did more than 1% of requests lead to errors?
#reference github
third_query = """
select * from (
    select a.day,
    round(cast((100*b.hits) as numeric) / cast(a.hits as numeric), 2)
    as ans from
        (select date(time) as day, count(*) as hits from log group by day) as a
        inner join
        (select date(time) as day, count(*) as hits from log where status
        like '%404%' group by day) as b
    on a.day = b.day)
as t where ans > 1.0;
"""


