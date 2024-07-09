# This is NTU-CAL: A Simple Q&A Website with Django

## Website Description
This is a simple question and answer website built using Django. Users can ask questions, provide answers, and vote on answers.

## Bases:
 - backend: Python, Django
 - frontend: bootstrap, HTML, CSS, Javascript

## Docker Run Command
To run the website using Docker, use the following command:
```
docker pull tsai815/ntu-cal-web:latest
docker run -d -p 8080:80 tsai815/ntu-cal-web:latest
```
Then visit http://localhost:8080
## Admin Page
You can manage the website via the `/admin` page:
- Visit `http://localhost:8080/admin` in your browser after starting the Docker container.
- Login with the admin credentials to manage users, questions, and answers.
