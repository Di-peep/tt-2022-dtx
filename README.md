# tt-2022-dtx
Test task for Data-OX  



## Installation

First, you need to clone this repository:

```bash
git clone https://github.com/Di-peep/tt-2022-dtx.git
```

Then change into the `tt-2022-dtx` folder:

```bash
cd tt-2022-dtx
```

Now, we will need to create a virtual environment and install all the dependencies:

```bash
python -m venv venv
. venv\Scripts\activate
pip install -r requirements.txt
```

## Start
- If you have your own MySQL server, you must configure access in the `db.py` file.  
After just run:

```bash
python parser.py
```

> After executing the script, you get a completed table on the mysql server and a `.csv` file in the `/data` folder.  

- If you don`t have your own MySQL server, you can use mysql image. 

```bash
docker volume create data
docker run -it --name=mysql_db -p 3306:3306 -e MYSQL_ROOT_PASSWORD=pass --mount source=data,destination=/data -d mysql
```

You can also use this parser image:

```bash
docker run --rm --name parser -v data:/app/data --link mysql_db vidmy/kijiji-parser
```

For tracking the work of the parser:  

```bash
docker logs -f parser
```

Finally, to get the `data_dump.sql`:  

```bash
docker exec -ti mysql_db bash
mysqldump -u root -p parsing > data/parsing.sql
>> pass
```

> After executing the script, you get a `.csv` file and a `data_dump.sql` in the `../volume/data/` folder on your PC.  
