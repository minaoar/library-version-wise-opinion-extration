# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# download a library
RUN python -m spacy download en_core_web_lg

# copy the content of the local source directory to the working directory
COPY source/ ./source/

# copy the content of the local data directory to the working directory
COPY data/ ./data/

# command to run on container start
CMD [ "python", "./source/process_post_text.py" ]