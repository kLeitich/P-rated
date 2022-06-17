# P-rated



A Django website that someone can submit a project and user can rate the project.



## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites & Installing

#### Cloning the repository:  
 ```bash 
https://github.com/kLeitich/P-rated.git
```
#### Navigate into the folder and install requirements  
 ```bash 
cd P-rated && pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations photoapp
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py runserver 
```
The application opens up on `127.0.0.1:8000`. <br>
If you want to use new server run e.g 9000
```bash 
 python manage.py runserver 9000

## Running the tests

```bash 
 python manage.py test app
```




## Deployment

After that you can deploy on Heroku or any of your preffered choice

## Built With

  
* [Python3.8](https://www.python.org/)  
* [Django 4.0.4](https://docs.djangoproject.com/en/4.0/)  
* [Heroku](https://heroku.com)  
  



## Versioning

see the [tags on this repository](https://github.com/kleitich/instagram_clone.git). 

## Authors

* **Kevin Leitich** - *Initial work* - [KEVIN](https://github.com/Kleitich)



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Hat tip to anyone whose uses my code

