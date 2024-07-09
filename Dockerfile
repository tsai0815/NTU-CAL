######### Clean, Short and Concise Dockefile #########
FROM ubuntu:lastest
# Use a lightweight base image
FROM python:3.10-slim

# Set up environment variable for the application directory
ENV APP_HOME=/app

# Create the application directory
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy only the requirements file
COPY requirements.txt .

# Create and activate virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN apt-get update && \
    apt-get install -y \
        build-essential \
        pkg-config \
        libcairo2-dev \
        python3-gi \
        python3-gi-cairo \
        gir1.2-gtk-3.0 \
        libgirepository1.0-dev \
        dbus \
        libdbus-1-dev \
        libdbus-glib-1-dev

# Install dependencies
RUN pip install --upgrade pip && \
    # pip install wheel && \
    pip install --no-cache-dir -r requirements.txt 


# Copy the entire local project into the container
COPY . .

# Start the server
CMD ["python3", "manage.py", "runserver"]