# Use an official Python runtime as a base image
FROM python 3.13.5

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

# Define the command to run your Python script
# Replace 'your_script_name.py' with the actual name of your Python script
CMD ["python", "titanic-python.py"]
