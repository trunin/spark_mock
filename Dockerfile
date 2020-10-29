FROM docker.dcube.devmail.ru/base/python-3.7.5-lightgbm-2.3.1-pandas-1.1.3

COPY . /workdir
WORKDIR /workdir

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install flask

ENTRYPOINT ["/bin/bash"]

CMD ["run.sh"]
