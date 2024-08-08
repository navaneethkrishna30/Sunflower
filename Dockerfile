FROM python:3.11.5-slim

WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app

# 
CMD ["fastapi", "run", "api/main.py", "--port", "8080"]