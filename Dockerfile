FROM python:3.11.5
RUN useradd -m jupyter
EXPOSE 8888

RUN apt update && apt-get install -y lsof build-essential make gcc g++ git gfortran npm \
        gdal-bin libgdal-dev python3-all-dev libspatialindex-dev
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

# Install Julia
RUN curl -fsSL https://install.julialang.org | sh -s -- -y && \
    mv /root/.juliaup /home/jupyter/.juliaup && \
    chown -R jupyter:jupyter /home/jupyter/.juliaup
ENV PATH="/home/jupyter/.juliaup/bin:${PATH}"
ENV JULIA_DEPOT_PATH="/home/jupyter/.julia"
RUN mkdir -p ${JULIA_DEPOT_PATH} && chown -R jupyter:jupyter ${JULIA_DEPOT_PATH}

# Install Mimi.jl as jupyter user
USER jupyter
RUN julia -e 'using Pkg; Pkg.add("Mimi")'
USER root

# Install Python requirements
RUN pip install --upgrade --no-cache-dir hatch pip

COPY --chown=1000:1000 . /jupyter/
RUN chown -R 1000:1000 /jupyter

RUN pip install -e /jupyter/climate-python
RUN pip install -e /jupyter/mimi-julia

# Switch to non-root user. It is crucial for security reasons to not run jupyter as root user!
USER jupyter
WORKDIR /jupyter

# Service
CMD ["python", "-m", "beaker_kernel.server.main", "--ip", "0.0.0.0"]