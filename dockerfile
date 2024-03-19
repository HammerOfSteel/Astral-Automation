FROM alpine:latest

RUN apk update && apk add --no-cache curl python3 py3-pip
RUN python3 -m venv /venv
RUN /venv/bin/pip install fastapi uvicorn

COPY . /app
WORKDIR /app
EXPOSE 8000

CMD ["/venv/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
