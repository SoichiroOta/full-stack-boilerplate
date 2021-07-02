FROM python:3.8
ENV PYTHONUNBUFFERED 1
ENV PORT '80'
ADD . /responder
WORKDIR /responder
RUN pip install -r requirements.txt
CMD python3 api.py
EXPOSE 80