
## Structure

* `/calibration` - functions for setting up model forcing for calibration
* `/data` - calibration and forcing scenario data
* `/docs` - files for GitHub Pages site documentation
* `/examples` - Jupyter notebooks demonstrating the workflows for model calibration, downscaling global sea-level change to local, and making model hindcasts and projections; we anticipate that it will be useful to take these notebooks and modifying them to fit users' own use cases
* `/joss_submission` - files associated with the MimiBRICK.jl Journal of Open Source Software submission
* `/src` - functions for the actual component submodels of BRICK, for configuring these models as a combined coupled BRICK model, for performing the downscaling to local sea-level change, and for performing the model calibration; includes the likelihood function configuration
* `/test` - contains tests for out-of-box model configurations, testing a small model calibration, and downscaling to local sea-level change; used for continuous integration testing

### Substituting/Modifying Component Sub-models

Below is a summary of the changes that would be needed to modify a component sub-model of MimiBRICK. A much more comprehensive discussion of running, modifying old, and creating new models within the Mimi coupled modeling framework can be found at the [Mimi Documentation](https://www.mimiframework.org/Mimi.jl/stable/).

* Create/modify the source code for the new/modified component in `/src/components`. See the Design Pattern section below for a stencil. Pattern-matching with the existing component sub-models is encouraged!
* In `/src/MimiBRICK.jl`…
    * Add an `include` statement if you have created a new file for your model component
    * Add/modify `update_param` calls, component name, and parameter names/default values
    * Connect parameters across components using `connect_param` and `add_shared_param` near the bottom of the `brick` module, as needed
* In `/src/calibration/run_historic_models/run_brick_historic_climate.jl`…
    * Add/modify the parameter names and `update_param` calls to match what is in the source code for your modified component and in `/src/MimiBRICK.jl`
* In `/src/calibration/run_hindcast.jl` and `/src/calibration/run_projections.jl`…
    * Modify the `ar1_noise_xxx` and `obs_error_xxx` variables, as needed, depending on whether the modified component uses a similar or new residual model. Might also require modifying at “Statistical noise models” if a new residual model is used
    * Modify `update_param` calls associated with the modified component (similarly to in `/src/MimiBRICK.jl`)
    * If your modification create new output that you would like to write to files, you may want to modify at “Save output” as well to include any new fields that you want to write
* If your altered the model components and the naming conventions for the model output CSV files, then you may also need to modify the `/src/downscale.jl` file to generate estimates of local sea-level change.
* If you would like to modify the calibration data used, then you should modify…
    * the function `load_calibration_data` within `/src/calibration/calibration_helper_functions.jl`
    * the appropriate `create_log_posterior_xxx.jl` script within `/src/calibration/create_log_posteriors`

### Design Pattern

Typical Mimi component models use the pattern depicted below. Most notably, models are run timestep-by-timestep using a `run_timestep` function that is defined for each model component. `run_timestep` has four input arguments:
* `p` - model parameters (see [Mimi Documentation on parameters and variables](https://www.mimiframework.org/Mimi.jl/stable/howto/howto_5/) for more information)
* `v` - model variables
* `d` - model dimensions (e.g., `d.regions` or `d.time`)
* `t` - timestep (see [Mimi Documentation on the timestep types](https://www.mimiframework.org/Mimi.jl/stable/howto/howto_4/) for more information)

`run_timestep` typically does not have a return value. Rather, this function modifies the shared model variables in `v`. For example, within `MimiBRICK.jl`, sea levels for the glaciers and ice caps component are computed and stored in `v.gsic_sea_level` within the glaciers and ice caps `run_timestep` function.

More information about defining new model components in Mimi can be found in the [Mimi Documentation](https://www.mimiframework.org/Mimi.jl/stable/tutorials/tutorial_4/).

```
using Mimi

@defcomp component_name begin

    # --------------------
    # Model Parameters
    # --------------------

    compshortname_scalarparam = Parameter()                   # description (units)
    compshortname_timeseriesparam = Parameter(index=[time])   # description (units)

    # --------------------
    # Model Variables
    # --------------------

    compshortname_timeseriesvariable = Variable(index=[time]) # description (units)

    # --------------------
    # Model Equations
    # --------------------
    
    function run_timestep(p, v, d, t)
    
        # what does a single time step within the sub-model component do?
      
    end
    
end
```
