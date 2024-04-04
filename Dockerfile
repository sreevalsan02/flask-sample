
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Expose port (adjust if your app runs on a different port)
EXPOSE 8000

# Command to run the app
CMD ["gunicorn","-b","0.0.0.0:8000","app:app"]
