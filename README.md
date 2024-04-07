# Online food delivery website with Recommendation system
## General introduction:  
> This is an intelligence recommendation system for online food ordering platform based on **Collaborative Filtering** and **Content-based recommendation**.  

- **User type**:
1. customer
2. merchant
3. administrator

---
 
## 🚀Configuration:  
- Language: python (3.9) (Version >=3.7)   
- Database: mysql  
- Framework: django (4.2)  

**third-party library:**  
- PyMySql 1.1.0  
- numpy 1.26.4  
- pandas 2.2.1  
- scikit-learn 1.4.1  
- Bootstrap 3  
- Feather icon  
- Jquery  

----

## 📜Recommendation system:
### Collaborative Filtering:  
- User CF:  
> user similarity matrix

### Content-based recommendation:  
> Using content-based recommendation as a strategy for cold start.

---

## 💻Deploy & Run project:
- How to run this project?  
`python manage.py runserver`  
url: `http://127.0.0.1:8000/`  

- How to migrate a database?
```
python manage.py makemigrations

python manage.py migrate
``` 

---

### Administrator:  
- How to access the admin page?  
`http://127.0.0.1:8000/admin`  

- How to create an admin account?  
`python  manage.py createsuperuser `  

- Administrator account:  
```
username: Blueblue2222
Password: cdut8888
```  

--- 

### View of website:
- main page
![main page](md_img/main_1.jpg)
![main page](md_img/main_2.jpg)
![main page](md_img/main_3.jpg)
