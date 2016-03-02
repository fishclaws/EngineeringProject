# EngineeringProject

This is a Feature Request form project written in Python 3.4, using Django 1.9.2, MySql (running on AWS RDS), SqLite, jQuery, jQuery validation, DataTables, and Bootstrap

You can visit the demo at
http://ec2-52-23-248-235.compute-1.amazonaws.com/feature_requests/
It is running on a Linux EC2 AWS server on Apache

Installation should be easy

1. Make sure you have Python 3.4 and pip installed
2. Install Django by running this ```pip install Django==1.9.2```

3. Don't do anything for this step and simply use the SqLite DB provided with the project (this is the current DATABASES configuration)
    ```python
	DATABASES = {
	 'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(os.path.abspath(os.path.dirname(__file__)), 'MainDB.db'),
		}
	}
```
 **OR**
3. Create and connect to an instance of MySql and run the following
  ```SQL
    CREATE DATABASE `MainDB` /*!40100 DEFAULT CHARACTER SET latin1 */;

    CREATE TABLE `feature_requests_client` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(100) DEFAULT NULL,
    `client_priority` int(11) DEFAULT '0',
    PRIMARY KEY (`id`)
      ) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

    CREATE TABLE `feature_requests_featurerequest` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `title` varchar(100) DEFAULT NULL,
    `description` varchar(2000) DEFAULT NULL,
    `client_id` int(11) DEFAULT NULL,
    `target_date` date DEFAULT NULL,
    `client_priority` int(11) DEFAULT NULL,
    `ticket_url` varchar(45) DEFAULT NULL,
    `product_area_id` int(11) DEFAULT NULL,
    `version` int(11) DEFAULT 0,
    PRIMARY KEY (`id`),
    UNIQUE KEY `id_UNIQUE` (`id`)
  ) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

    CREATE TABLE `feature_requests_productarea` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `product_category` varchar(100) DEFAULT NULL,
    PRIMARY KEY (`id`)
  ) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
  ```

4. If you did the 2nd option, edit the ```DATABASES``` section of the EngineeringProject\settings.py by uncommenting the second DATABASES block (contact me for my own credentials if you want to use my AWS database). Run ```$ pip install PyMySQL```.
5. Run ```python manage.py migrate```
6. Run ```python manage.py migrate --run-syncdb```
6. Run ```python manage.py runserver```
7. The app should be up and ready, go to http://localhost:8000/feature_requests/ to see it
8. To add the test data specified in the reqs press "Add Test Clients and Product Areas"
