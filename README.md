notes:

For getting all employee data and post employeed data
1. http://localhost:8000/employeeslist_create/
   
For getting indivigual employee data and update employeed data & for delete
3. http://localhost:8000/employee/3/



1. http://localhost:8000/employee/
   Methods:=- ["GET", "POST"]

2. http://localhost:8000/employee/3/
      Methods:=- ["GET", "PUT", "DELETE"]


   json response data below :
   ````
   
        "id": 3,
        "address_details": {
          "id": 3,
          "hno": "12356",
          "street": "Main down stree",
          "city": "vskp",
          "state": "ap"
        },
        "work_experience": [
          {
            "id": 16,
            "company_name": "micro_mp",
            "from_date": "2021-08-08",
            "to_date": "2024-05-06",
            "address": "hyderabad"
          }
        ],
        "qualifications": [
          {
            "id": 16,
            "qualification_name": "Bachelor's Degree",
            "percentage": 85.5
          }
        ],
        "projects": [
          {
            "id": 16,
            "title": "refactored",
            "description": "e-learning management system"
          }
        ],
        "name": "vasu12345",
        "email": "vasu13@gmail.com",
        "age": 23,
        "gender": "Male",
        "phone_no": "+916302575062",
        "photo": "/media/images/person_4OVEF3o.jpg"


   `````

