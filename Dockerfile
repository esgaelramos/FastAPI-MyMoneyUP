FROM python:3.11.4-slim-buster

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONUNBUFFERED=1

WORKDIR /python_colombia/temii

COPY ./requirements.txt /python_colombia/temii/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /python_colombia/temii/requirements.txt

COPY ./ /python_colombia/temii

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]