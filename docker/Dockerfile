FROM python:3.11
ARG work_dir="/root/manageme/"
WORKDIR ${work_dir}

RUN apt-get update &&\
    apt-get -y install locales &&\
    apt-get -y install vim &&\
    echo -e "\n alias ll='ls -la --color'\n " >> ~/.bashrc &&\
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9

RUN pip install --upgrade pip


# Poetryのインストール
RUN curl -sSL https://install.python-poetry.org | python -

# Poetryのパスの設定
ENV PATH /root/.local/bin:$PATH

#COPY ./shue_store ./

RUN if [ -f pyproject.toml ]; then poetry install; fi

# RUN poetry install

# Poetryが仮想環境を生成しないようにする
# RUN poetry config virtualenvs.create true

# EXPOSE 8000
