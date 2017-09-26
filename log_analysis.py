

import psycopg2

first_ques = 'What are the most popular three articles of all time?'
first_query = """select title, count(*) as num from articles join log on concat('/article/', articles.slug) = log.path group by articles.title order by num desc limit 3
"""

second_ques = 'Who are the most popular article authors of all time?'
second_query = """
select authors.name, count(*) as num from articles join authors on articles.author = authors.id join log on concat('/article/', articles.slug) = log.path where log.status like '%200%' group by authors.name order by num desc
"""

third_ques = 'On which days did more than 1% of requests lead to errors?'
third_query = """
select * from (
    select error_percentage.date, error_percentage.perc_rate from error_percentage where error_percentage.perc_rate > 1 order by error_percentage.perc_rate desc limit 1
"""


class SolveLog:
    def __init__(self):
        try:
            self.db = psycopg2.connect('dbname=news')
            self.cursor = self.db.cursor()
        except Exception as e:
            print e

    def execute_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def solve(self, ques, query, suffix='views'):
        query = query.replace('\n', ' ')
        result = self.execute_query(query)
        print ques
        for i in range(len(result)):
            print '\t', i + 1, '.', result[i][0], '--', result[i][1], suffix
        
        print ''

    def exit(self):
        self.db.close()


if __name__ == '__main__':
    solveLog = SolveLog()
    solveLog.solve(first_ques, first_query)
    solveLog.solve(second_ques, second_query)
    solveLog.solve(third_ques, third_query, '% error')
    solveLog.exit()
