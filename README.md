## Django_Assessment2_GroupTask

### Development logs:  
**From 26th March to 27th March Complete Version:94c9524** Build website, database, data parse, basic functions design, websites page design and ...  
**28th March Complete Version:a79bbed** A running version (prototype) finishes, functions including date search, position search, coordinates search, and total data check.  
**29th March Complete Version:fffadf6** A modification about performance.  
**From 30th March to 31th March Complete Version:9f224a5** A registration and login system added.   
**31th March Complete Version:9a3c2b6** Testing registration and login system, and pass successfully.  
**1st April Complete Version:cce3b6b** Data edit function added and tested, pass successfully.  
**1st April Complete Version:ba45767** Testing each function and templates pages. The whole design finishes.  
**1st April Complete Version:42a41eb** Add teble pattern for better performance.  

### What is our design?  
We design a website application basing on Django, which allows users to check, search, edit data flexibly.  
### The Data Source  
From https://www.kaggle.com/code/benhamner/san-francisco-top-crimes-map/data, we downloaded the crime records in San Francisco, and picked 20000 rows (from 01/01/2015 to 31/03/2015) as data source.  
### Linked Tables (models.py and parse_csv.py)  
We created two linked tables basing on the data source: one is the detail information basing on date and weekday, while the other is related with position, address and accurate ordinates.  
### Functions (views.py, templates and forms)  
Our application offers 4 functions to search and check the data, 1 function allowing users to edit, and one registration and login function.  
#### 1.Index Page (index.html, views.index)  
This application gives 7 buttons (links) in the index page.   
**Home:** allows you return to index page whenever you want.  
**Login:** skips to a login and registration page.  
**Date search:** search specific data in a certain date.  
**Position search:** search specific data in a certain position.  
**Accurate coordinates search:** allows you enter a couple of floating numbers including longitude and latitude, and find the matching data from the database.  
**Total data table check:** jumps to the database, including two tables.  
**Data edit (requires login):** allows you to add, edit, or delete data as you want.  
#### 2.Login and Registration Page (login.html, logout.html, signup.html, models.Visitor, form.py, views.signup, views.log_out):  
Login and Registration system support users to create personal account, which allows them to use more function.(Especially, give them rights to edit the database). Every account should consist of a username and a password, and the form can be seen in the form.py file. The login and registration is basing on the source tool in Django.  
#### 3.Date and Position Search (date_search.html, date_result.html, position_search.html, position_result.html, views.position_search, views. position_result, views.date_search, views.date_result):  
Date search page shows every date from 01/01/2015 to 31/03/2015, and each date is a URL link as a search condition to date result page, while position search page shows every recorded address in the data base, and each address can be a condition for searching. Once there are contents in this date, the result page will post all matching data, or it will tell the users no data matches.  
#### 4.Accurate Coordinates Search (coordinates_search.html, views.coordinates_search):  
In this page, users are asked to enter a couple of floating number, longitude and latitude. Then the system will feedback the result matching the coordinates. The more digits means more accurate result, as well as less result (because more accurate).  
#### 5.Data Edit Page (data_edit.html, views.data_edit):  
This function is only used after login. It allows users to search a certain row of data by entering the row id, and users can make differences on any data as they want. If users make changes on a data row with existing row id, then the existing values will be changed if the inputs are not empty. If users enter a not existing row id, then the system will generate a new row data instead. It also allows users to delete certain rows.  
#### 6.Total Data Page (total.html, views.total_data):  
Check two tables respectively.  
### Testing (Tests.py)  
We use the test tool in Django for application test, including function and templates. Our application consists of 10 pages (with 1 base page ), we combine date search and result, position search and result. Finally 8 tests are used, including 1 test requires for login system. All tests pass successfully.  
### Github and Heroku  
Our group consists of 3 members, and achieve remote collaboration by using github. From 26th March we start group work, until 1st April all work steps, logs, and versions are recorded and submitted onto github and heroku. All flowing version and logs can be checked in the git-log text.  
