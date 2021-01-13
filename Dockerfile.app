FROM python:3.8
WORKDIR /app
COPY . .
RUN pip install --upgrade pip && \
		pip install -r requirements.txt
EXPOSE 5000
# CMD [ "gunicorn", "-b 0.0.0.0:5000", "app:app" ]
CMD [ "python", "app.py" ]
