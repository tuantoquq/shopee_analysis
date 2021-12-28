FROM tuantoquq/spark-base

# -- Layer: JupyterLab

ARG spark_version=3.0.0
ARG jupyterlab_version

RUN apt-get update -y && \
    apt-get install -y python3-pip && \
    pip3 install -r $SHARED_WORKSPACE/requirements.txt && \
    apt install libffi-dev && \
    pip3 install pyspark  &&\
    pip3 install jupyterlab

# -- Runtime
EXPOSE 8888
WORKDIR ${SHARED_WORKSPACE}
CMD jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token=