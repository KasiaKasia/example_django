# example_django
example django 1.7.

Create a Clean Workspace:                                                                                                    
<code>$ mkdir example_django  </code>                                                                                                      
<code>$ cd example_django </code> 

Create a virtualenv                                                                                                         
<code> virtualenv ./example_django/  </code>                                                                                                 
In the source directory of the project is not example_django virtual environment. Containing libraries and scripts installed in the environment.     

Run it with the command:                                                                                                     
<code> $ example_django\Scripts\activate</code>                                                                              
<code>(example_django)$ pip install django==1.7.7 </code> 

Creating the Project:                                                                                                 
<code>(example_django)$ django-admin.py startproject administration .  </code>  

Creating the App:                                                                                                       
<code>(example_django)$ python ./manage.py startapp people </code>                                                                                                            
                                                                                                           
The administration/settings.py file contains the Django configuration for our project:                                  
<code=python>
DATABASES = {                                                                                                  
    'default': {                                                                                                         
    'ENGINE': 'django.db.backends.sqlite3',                                                                              
    'NAME': 'people.db',                                                                                                
    }                                                                                                                        
}   </code> 

<code>
INSTALLED_APPS = (   
</code>                                                                                                          
       <code> 'django.contrib.auth',   </code>  
       <code> 'django.contrib.contenttypes',   </code>  
       <code> 'django.contrib.sessions',   </code>  
       <code> 'django.contrib.sites', </code>   </code>  
       <code> 'django.contrib.messages', </code>  
       <code> 'django.contrib.staticfiles',   </code>  
       <code> 'people', </code>  
<code>)        
</code>          

Perform migrations after changes                                                                                             
<code>(example_django)$ python ./manage.py syncdb     </code>                                                                
<code>(example_django)$ python manage.py makemigrations    </code>  

In the console, start the server with the command:                                                                           
<code>(example_django)$ python manage.py runserver   </code>                                                                                

Open your browser and enter the address:                                                                                    
http://127.0.0.1:8000/

You can run the tests for your application using manage.py:                                                                 
<code>(example_django)$ python manage.py test             </code>      
<code>(example_django)$ python manage.py test people  </code> 

Creating Bootstrap:                                                                                                          
Create the static directory in our project and unpack Bootstrap into it.                                                    
<code>(example_django)$ mkdir administration/static   </code>        
<code>(example_django)$ cd administration/static       </code>       
<code>(example_django)$ unzip ~/Downloads/bootstrap-3.3.2.zip   </code> 