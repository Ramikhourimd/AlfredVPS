FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install dependencies early for caching
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Ensure entrypoint is executable
RUN chmod +x entrypoint.sh

# Expose Streamlit port
EXPOSE 8501

CMD ["./entrypoint.sh"]
