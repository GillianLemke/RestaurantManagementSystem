# Restaurant Management System

## Initialization

Install pip:<br>
mac: ```sudo easy_install pip```<br>
[windows](https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation)
<br><br>
Install Flask:<br>
mac: ```sudo pip install Flask```<br>
windows: ```pip install Flask```

## Running the app
```
$ export FLASK_APP=main.py
$ flask run
```

## Connecting to the DB
1. Make sure MySQL is installed and working
2. Make sure your IP is authorized on the Google Cloud instance
3. Install ```mysql-client```. You can do so [here](https://cloud.google.com/sql/docs/mysql/connect-admin-ip?authuser=2#install-mysql-client).
4. ```mysql --host=[INSTANCE_IP] --user=root --password```
5. Enter the password
	You should now see the mysql prompt.

## Connecting to the DB Using MySQLWorkbench
1. Go through the steps to connect to the database through the command line
2. Open MySQLWorkbench and click the ```+``` to add a new connection.
3. Enter the ```INSTANCE_IP``` as the host. Leave the port and user the same.
4. Enter the ```password``` and click ```okay```.

## Add to DB
```
cd db/
python [filename].py
```
example: ```python create_employee.py```
