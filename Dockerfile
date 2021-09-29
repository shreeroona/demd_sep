FROM python:3.6.1-alpine
## Changing your working directory 
WORKDIR /project
##copy local files to project directory
ADD . /project
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python","main.py"]