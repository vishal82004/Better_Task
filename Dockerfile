# -------- Stage 1: Builder --------
FROM python:3.9-slim-bookworm AS builder

WORKDIR /app

# Copy only requirement file first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire source code
COPY . .

# -------- Stage 2: Final Runtime --------
FROM python:3.9-slim-bookworm AS final

WORKDIR /app

# Upgrade base system (optional but helps avoid CVEs)
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Copy installed Python packages from builder
COPY --from=builder /usr/local/lib/python3.9 /usr/local/lib/python3.9
COPY --from=builder /usr/local/bin /usr/local/bin


COPY --from=builder /app /app


EXPOSE 5000

CMD ["python", "app.py"]
