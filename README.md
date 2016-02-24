# EngineeringProject

This is a Feature Request form project written in Python 3.4, using Django 1.9.2, MySql (running on AWS RDS), jQuery, jQuery Verification and Bootstrap.

Installation should be easy

1. Make sure you have Python 3.4 and pip installed
2. Install Django by running this ```pip install Django==1.9.2```
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
    PRIMARY KEY (`id`),
    UNIQUE KEY `id_UNIQUE` (`id`)
  ) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

    CREATE TABLE `feature_requests_productarea` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `product_category` varchar(100) DEFAULT NULL,
    PRIMARY KEY (`id`)
  ) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
  ```

  **OR** Simply use Sqlite and change __EngineeringProject\settings.py__ with the following configuration
    ```python
DATABASES = {
 'default': {
	'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(PROJECT_DIR, 'MainDB.db'),
	}
}
    ```

4. Edit the ```DATABASES``` section of the EngineeringProject\settings.py file for this to work (contact me for my own credentials if you want to use my database).
5. Run ```$ pip install PyMySQL```
6. Then Run ```python manage.py migrate```
7. Then run ```python manage.py runserver```
8. The server should be up and ready, go to http://localhost:8000/feature_requests/ and you should be good to go
9. The button at the top of the main page "Add Test Clients and Product Areas" will add the test data given in the requirements
