few_shots = [
    {'Question': "How many connections did I make in September 2023?",
     'SQLQuery': "SELECT COUNT(*) FROM linkedin_connects WHERE STR_TO_DATE(`Connected On`, '%d-%b-%y') BETWEEN '2023-09-01' AND '2023-09-30';",
     'SQLResult': "Result of the SQL query",
     'Answer': "54"},
    
    {'Question': "How many connections did I make in 2023?",
     'SQLQuery': "SELECT COUNT(*) FROM linkedin_connects WHERE STR_TO_DATE(`Connected On`, '%d-%b-%y') BETWEEN '2023-01-01' AND '2023-12-31';",
     'SQLResult': "Result of the SQL query",
     'Answer': "330"},
    
    {'Question': "How many connections did I make on 30th December 2023?",
     'SQLQuery': "SELECT COUNT(*) FROM linkedin_connects WHERE STR_TO_DATE(`Connected On`, '%d-%b-%y') = '2023-12-30';",
     'SQLResult': "Result of the SQL query",
     'Answer': "0"},
    
    {'Question': "What is the most common Position in all my LinkedIn contacts?",
     'SQLQuery': "SELECT DISTINCT `Position` FROM linkedin_connects GROUP BY `Position` ORDER BY COUNT(`Position`) DESC LIMIT 1",
     'SQLResult': "Result of the SQL query",
     'Answer': "Data Analyst"},
    
    {'Question': "What are the names and position of the linkedin contacts I made between 5th Jan 2023 and 18th Jan 2023?",
     'SQLQuery': "SELECT `Name`,`Position` FROM linkedin_connects WHERE STR_TO_DATE(`Connected On`, '%d-%b-%y') BETWEEN '2023-01-05' AND '2023-01-18';",
     'SQLResult': "Result of the SQL query",
     'Answer': "[('Jagtar singh', 'PHP/laravel Developer'), ('Vinay Raheja', 'SEO Executive'), ('Shilpa Rana', ' Human Resources Manager'), ('Mark Parente', 'Application Developer')]"},
    
    {'Question': "How many invites did I send in 2024?",
     'SQLQuery': "SELECT COUNT(*) FROM linkedin_invites WHERE `Direction` = 'OUTGOING' AND STR_TO_DATE(`Sent At`, '%m/%d/%y, %h:%i %p') BETWEEN '2024-01-01 00:00:00' AND '2024-12-31 23:59:59';",
     'SQLResult': "Result of the SQL query",
     'Answer': "2"},
    
    {'Question': "What are the top 10 instagram pages I've liked?",
     'SQLQuery': "SELECT `Post Page`, COUNT(*) AS Likes FROM instagram_likes GROUP BY `Post Page` ORDER BY Likes DESC LIMIT 10;",
     'SQLResult': "Result of the SQL query",
     'Answer': "[('espnfc', 615), ('pubity', 176), ('brfootball', 169), ('newjerseywolvesfc', 169), ('433', 142), ('fcbarcelona', 114), ('leomessi', 99), ('successfulmaster', 46), ('psg', 41), ('fabriziorom', 39)]"},
    
    {'Question': "What is the position of the 10 most recent connections I made on LinkedIn?",
     'SQLQuery': "SELECT `Position` FROM linkedin_connects ORDER BY STR_TO_DATE(`Connected On`, '%d-%b-%y') DESC LIMIT 10;",
     'SQLResult': "Result of the SQL query",
     'Answer': "[('Teaching Assistant',), ('Assistant It Manager',), ('Chief Executive Officer',), ('Software Engineer',), ('Student',), ('Non-Technical Recruiter ',), ('Project Engineer',), ('Junior Business Analyst',), ('Digital Content Producer',), ('Store Manager',)]"},
    
    {'Question': "How many of my instagram advertisers don't have my data files and are only remarketing?",
     'SQLQuery': "SELECT COUNT(*) FROM instagram_advertisers WHERE `Has Data` = 0 AND `Has Remarketing` = 1;",
     'SQLResult': "Result of the SQL query",
     'Answer': "396"}
    
]
