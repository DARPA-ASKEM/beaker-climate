## Example 1: The code initializes the FUND climate model, runs it through year 2200 with default parameters, and extracts time series data for key climate variables including global temperature and emissions of four greenhouse gases (CO2, CH4, N2O, and SF6), printing the results at specific milestone years (2020, 2050, 2100, and 2200) to show the progression of climate change impacts over time.

```julia
using MimiFUND

m = MimiFUND.get_model()
set_dimension!(m, :time, 1950:1:2200)
run(m)

# Get emissions data
emissions_df = getdataframe(m, :emissions=>:mco2)
ch4_df = getdataframe(m, :emissions=>:globch4)
n2o_df = getdataframe(m, :emissions=>:globn2o)
sf6_df = getdataframe(m, :emissions=>:globsf6)

# Get temperature data
temp_df = getdataframe(m, :climatedynamics=>:temp)

# Print some summary statistics
println("Global temperature increase by 2100:")
temp_2100 = temp_df[temp_df.time .== 2100, :temp][1]
println("$(round(temp_2100, digits=2)) °C")

println("\nGlobal temperature increase by 2200:")
temp_2200 = temp_df[temp_df.time .== 2200, :temp][1]
println("$(round(temp_2200, digits=2)) °C")

# Print emissions data for key years
println("\nGHG Emissions Summary:")
println("\nCO2 emissions (GtC):")
for year in [2020, 2050, 2100, 2200]
    value = emissions_df[emissions_df.time .== year, :mco2][1]
    println("$year: $(round(value, digits=2))")
end

println("\nCH4 emissions (Mt):")
for year in [2020, 2050, 2100, 2200]
    value = ch4_df[ch4_df.time .== year, :globch4][1]
    println("$year: $(round(value, digits=2))")
end

println("\nN2O emissions (Mt):")
for year in [2020, 2050, 2100, 2200]
    value = n2o_df[n2o_df.time .== year, :globn2o][1]
    println("$year: $(round(value, digits=2))")
end

println("\nSF6 emissions (kt):")
for year in [2020, 2050, 2100, 2200]
    value = sf6_df[sf6_df.time .== year, :globsf6][1]
    println("$year: $(round(value, digits=2))")
end
```


## Example 2: Basic FUND model simulation using default parameters to project global temperature changes from 2020 to 2300

```julia
using MimiFUND

# Create a default version of the FUND model
m = MimiFUND.get_model()

# Run the model
run(m)

# Get global temperature changes at key years
temperature = m[:climatedynamics, :temp]

println("Global temperature change (°C) at selected years:")
for year in [2020, 2050, 2100, 2200, 2300]
    year_index = year - 1950 + 1  # Convert year to index
    temp = round(temperature[year_index], digits=2)
    println("$year: $(temp)°C")
end
```


## Example 3: Basic FUND model simulation with visualization: Creates a line plot of projected temperature changes from 1950 to 2300 and prints key values at specific years

```julia
using MimiFUND
using Plots

# Create and run model
m = MimiFUND.get_model()
run(m)

# Get temperature data
temperature = m[:climatedynamics, :temp]

# Create a simple line plot
plot(temperature, 
     title="FUND Model Temperature Projections (1950-2300)",
     xlabel="Years (from 1950)",
     ylabel="Temperature Change (°C)",
     legend=false,
     lw=2)

# Print some key values
println("\nTemperature change (°C) at key years:")
for year in [2020, 2050, 2100, 2200, 2300]
    year_index = year - 1950 + 1
    temp = round(temperature[year_index], digits=2)
    println("$year: $(temp)°C")
end
```
