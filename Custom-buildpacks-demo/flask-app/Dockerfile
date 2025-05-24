FROM python:3.11

# Set working directory
WORKDIR /app

# Copy requirements file if you have one (optional)
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# For your case, just install Flask directly
RUN pip install --no-cache-dir Flask

# Copy app code
COPY . .

# Expose port 5000
EXPOSE 5000

# Run the app
CMD ["python", "main.py"]
