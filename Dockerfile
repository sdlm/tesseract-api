FROM tesseractshadow/tesseract4re

RUN apt update && apt install -y curl python3.7 python3-distutils
RUN unlink /usr/bin/python3 && ln -s /usr/bin/python3.7 /usr/bin/python && ln -s /usr/bin/python3.7 /usr/bin/python3

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py
RUN pip install poetry

COPY poetry.lock ./
COPY pyproject.toml ./
RUN poetry config settings.virtualenvs.create false && \
    poetry install --no-dev --no-ansi --no-interaction

COPY src /webapp

CMD gunicorn -b 0.0.0.0:80 webapp.app:app --chdir / --reload
