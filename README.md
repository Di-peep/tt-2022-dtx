# Test task for Data-OX

> Junior Python test *(estimation: 1 day)*

From the [website](https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273) collect all ads, pagination includes.  
From every ad, you need to gather next points:
  - Image: save only url in database.
  - Date: save in format dd-mm-yyyy.
  - Currency must be saved as a separate attribute.
  - Save database dump to SQL file, with database creation schema.


## Technical requirements
1. For sending requests to the website, you can use any of the following: `requests, aiohttp, httpx`

2. If you decide to render page to get information from site pages, use any of the following: `Selenium, Playwright`
    
3. As ORM you can use the following: `peewee, SQLAlchemy, mongoengine`

4. Database for storing parsed data, any of the following: `PostgreSQL, MySQL, MongoDB`

### Must have
- Using of any virtual environment manager(venv, pipenv, poetry)
- All your source code should be uploaded to VCS. (GitHub, GitLab, Bitbucket)

### Nice to have
- Use docker.
- Asynchronous requests.
- Upload results into Google Sheet.

### Result of task
Fully working code and SQL database dump that must be uploaded on any VCS.  
Please add readme file with a short description of the project and instructions on how to set it up.
