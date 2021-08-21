FROM python:3.9

RUN mkdir -p /usr/src/app

WORKDIR usr/src/app

COPY . /usr/src/app/

RUN pip install -U setuptools pip pipenv \
    && pipenv install --system --deploy --ignore-pipfile

CMD ["python","CalculatorBot.py"]