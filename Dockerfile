FROM python

#IF YOU USE PROXY SERVER
ENV HTTP_PROXY "http://127.0.0.1:3001"
ENV HTTPS_PROXY "https://127.0.0.1:3001"

COPY . /microapi
WORKDIR /microapi
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]