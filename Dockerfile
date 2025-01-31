FROM python:3.11.5
RUN useradd -m jupyter
EXPOSE 8888

RUN apt update && apt-get install -y lsof build-essential make gcc g++ git gfortran npm \
        gdal-bin libgdal-dev python3-all-dev libspatialindex-dev graphviz libgraphviz-dev texlive
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

# Install Julia
RUN wget --no-verbose -O julia.tar.gz "https://julialang-s3.julialang.org/bin/linux/$(uname -m|sed 's/86_//')/1.10/julia-1.10.1-linux-$(uname -m).tar.gz"
RUN tar -xzf "julia.tar.gz" && mv julia-1.10.1 /opt/julia && \
    ln -s /opt/julia/bin/julia /usr/local/bin/julia && rm "julia.tar.gz"

# Add Julia to Jupyter
USER 1000
RUN julia -e 'using Pkg; Pkg.add("IJulia");'

# Install Julia requirements
RUN julia -e ' \
    packages = [ \
        "JLLWrappers", "DataSets", "XLSX", "Plots", "Downloads", "DataFrames", "ImageShow", "FileIO", "JSON3", "DisplayAs"  \
    ]; \
    using Pkg; \
    Pkg.add(packages);'

# Install beaker-decapodes requirements in julia environment
RUN julia -e ' \
    packages = [ \
        "Decapodes", "GraphViz", "Catlab", "DiagrammaticEquations", "CombinatorialSpaces", "CoordRefSystems", "GeometryBasics", \
        "SparseArrays", "LinearAlgebra", "CairoMakie", "ComponentArrays", "Interpolations", "OrdinaryDiffEq", "MLStyle" \
    ]; \
    using Pkg; \
    Pkg.add(packages);'

# Back to root for Python package install
USER root

RUN pip install --upgrade --no-cache-dir hatch pip tomli
# Install project requirements
# Hack to install requirements without requiring the rest of the files
COPY --chown=1000:1000 pyproject.toml /jupyter/beaker_climate/pyproject.toml
RUN bash -c "pip install --no-build-isolation --no-cache-dir -r <(echo 'import tomli; c = tomli.load(open(\"/jupyter/beaker_climate/pyproject.toml\", \"rb\")); d = c[\"project\"][\"dependencies\"]; print(\"\n\".join(f\"{dep}\" for dep in d))' | python)"

# Copy project files
COPY --chown=1000:1000 . /jupyter/beaker_climate
RUN chown -R 1000:1000 /jupyter/beaker_climate

# Install Python requirements
# RUN pip install --no-cache-dir -v -e /jupyter/beaker_climate
RUN pip install --upgrade --no-cache-dir hatch pip tomli editables
RUN pip install --no-build-isolation --no-cache-dir -v -e /jupyter/beaker_climate

# Switch to jupyter user and install Julia packages
USER jupyter
WORKDIR /jupyter

# Install required Julia packages for Mimi (these are used in the procedures/*.jl files)
RUN julia -e 'using Pkg; Pkg.add(["Mimi"]); using Mimi'
# Install MimiFund from GitHub
RUN julia -e 'using Pkg; Pkg.add(url="https://github.com/fund-model/MimiFUND.jl.git"); using MimiFUND;'

# other mimi models 
RUN julia -e 'using Pkg; Pkg.add("MimiBRICK"); using MimiBRICK;'
RUN julia -e 'using Pkg; Pkg.add(url="https://github.com/anthofflab/MimiFAIRv2.jl.git"); using MimiFAIRv2;'


# Service
CMD ["python", "-m", "beaker_kernel.server.main", "--ip", "0.0.0.0"]
