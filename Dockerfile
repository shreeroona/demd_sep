FROM python:3.6-alpine
WORKDIR /project
ADD . /
RUN pip install -r requirements.txt
CMD ['python','main.py']
