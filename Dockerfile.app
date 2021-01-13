FROM python:3.8
WORKDIR /app
COPY . .
RUN pip install --upgrade pip && \
		pip install -r requirements.txt
EXPOSE 5000
CMD [ "gunicorm", "-b localhost:5000", "app:app" ]
