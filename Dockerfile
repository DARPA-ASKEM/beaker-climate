FROM python:3.11.5
RUN useradd -m jupyter
EXPOSE 8888

RUN apt update && apt-get install -y lsof build-essential make gcc g++ git gfortran npm \
        gdal-bin libgdal-dev python3-all-dev libspatialindex-dev
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

# Install Python requirements
RUN pip install --upgrade --no-cache-dir hatch pip

COPY --chown=1000:1000 . /jupyter/
RUN chown -R 1000:1000 /jupyter
RUN pip install -e /jupyter

# TODO: remove this once type checking in archytas is released
RUN pip uninstall -y archytas && pip install --no-cache-dir "archytas @ git+https://github.com/jataware/archytas.git@robust-tool-typing"


# Switch to non-root user. It is crucial for security reasons to not run jupyter as root user!
USER jupyter
WORKDIR /jupyter

# Service
CMD ["python", "-m", "beaker_kernel.server.main", "--ip", "0.0.0.0"]