FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT ["python", "calculator.py"]
# Example default args (can be overridden):
CMD ["add","1","2"]
