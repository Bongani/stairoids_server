FROM python:3.6

COPY ./requirements.txt stairoids/requirements.txt

WORKDIR /stairoids

RUN pip install --no-cache-dir -r requirements.txt && \
    mkdir -p /stairoids/db

COPY . /stairoids

ENV DATABASE_URL="sqlite:////stairoids/db/app.db"

VOLUME /stairoids/db
EXPOSE 9000

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
