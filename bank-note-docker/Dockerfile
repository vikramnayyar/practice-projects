FROM continuumio/anaconda3:4.4.0
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN pip install --upgrade pip
RUN conda uninstall numpy
RUN conda uninstall tornado 
RUN pip install -r requirements.txt --ignore-installed six
CMD python app/flask-app.py
