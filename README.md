# Project log_analysis.
 This project is given on the udacity Nano degree program.
## Installation and running the project.
1. To run this program, I assume you have the specific virtual machine for this poject installed.
2. If not then follow this link to install [Virtual Machine]("https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0")
3. Then, run the commands bellow to create views needed for the third query to run execute the queries in given sequence below.
`CREATE VIEW number_of_view AS SELECT date(time), COUNT(time) AS view FROM log GROUP BY date(time) ORDER BY date(time) DESC;`
`CREATE VIEW view_error AS SELECT date(time), COUNT(time) AS log_error FROM log WHERE status = '404 Not Found' ORDER BY date(time);`
`CREATE VIEW  error_percentage AS SELECT number_of_view.date, number_of_view.view AS total, view_error.log_error AS error, (100 * error/total) AS perc_rate FROM number_of_view, view_error WHERE number_of_view.date = view_error.date ORDER by number_of_view.date`
4. Lastly in your vagrant shell run the file log_analysis.py 




 

