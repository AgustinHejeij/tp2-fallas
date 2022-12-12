FROM python:2
RUN mkdir /api
WORKDIR /api
ADD requirements.txt /api
RUN pip install http://www.antlr3.org/download/Python/antlr_python_runtime-3.1.3.tar.gz
RUN pip install --no-cache-dir -r requirements.txt
ADD . /api
EXPOSE 8000
CMD export FLASK_APP=wsgi.py && flask run --host=0.0.0.0 -p $PORT