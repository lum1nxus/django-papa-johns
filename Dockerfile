# I would use ubuntu24.04 as it shows best benchmarks for python apps, but I had weird error and not that
# much time to fix it, so using python image instead
FROM python:3.10-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

RUN groupadd -r djangouser && useradd -r -g djangouser djangouser
RUN chown -R djangouser:djangouser /app
USER djangouser

EXPOSE 8000

CMD ["sh", "-c", "python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000"]
