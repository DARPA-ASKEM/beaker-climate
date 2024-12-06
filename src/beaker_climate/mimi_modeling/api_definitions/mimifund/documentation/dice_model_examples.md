# DICE Model Usage Examples

This document contains examples of common operations with the DICE model, showing both the user query and the corresponding code implementation.

## Running the DICE Model

**Query:** Can you run the DICE Model?

**Code:**
```julia
# First, install the package
import Pkg; Pkg.add(MimiDICE2010)

# Then run the model
using MimiDICE2010
m = MimiDICE2010.get_model()
run(m)
```

## Accessing Model Variables

### Method 1: Direct Access

**Query:** Access a specific variable's data in tabular format

**Code:**
```julia
co2_emissions = m[:co2_cycle, :E_co2]
```

### Method 2: DataFrame Format

**Query:** Access a specific variable's data in a Dataframe

**Code:**
```julia
co2_emissions = getdataframe(m, :co2_cycle, :E_co2)
```

## Additional Queries

**Query:** Can you install BRICK?

*Note: Implementation example not available in the database.*
