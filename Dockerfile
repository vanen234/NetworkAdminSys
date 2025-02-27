# Step 1: Use an official Python image as a base image
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the current directory contents to the container at /app
COPY . /app

# Step 4: Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Make port 5000 available to the world outside the container
EXPOSE 5000

# Step 6: Define environment variables
ENV FLASK_APP=app.py

# Step 7: Run the app when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
