FROM python:3.13
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
WORKDIR /code/app
ENV EXPORT_FORMAT=pdf
ENV EXPORT_DIR=/export
CMD ["python", "main.py"]
