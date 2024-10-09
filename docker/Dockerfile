FROM python:3.12

COPY requirements.txt /
COPY src /src

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "python" ]

CMD [ "src/main/main.py" ]
