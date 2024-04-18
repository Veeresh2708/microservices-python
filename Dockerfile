FROM python:alpine3.19
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src src
EXPOSE 3000
HEALTHCHECK --interval=30s --retries=3 --start-period=30s --timeout=30s \
            CMD curl --fail http://localhost:3000/health || exit 1 
ENTRYPOINT ["python", "./src/app.py"]