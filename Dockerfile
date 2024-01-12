FROM python:3.11.4-slim-buster

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONUNBUFFERED=1

WORKDIR /python_colombia/talk_organizer

COPY ./requirements.txt /python_colombia/talk_organizer/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /python_colombia/talk_organizer/requirements.txt

COPY ./ /python_colombia/talk_organizer

CMD ["uvicorn", "core.application:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]