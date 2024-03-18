# Example BSM Analysis 

Hello, and welcome to the example BSM analysis GitHub. This is supposed to cover what we expect from 

# Naming

The naming convention we want to use is 

```
IC<configuration>-<YYYY>-<desc>
```

For example, an analysis looking for attenuation of neutrinos passing through the Galactic Plane due to scattering on dark matter using the full Generation 1 that was first presented in 2022, you could use:

```
IC86-2022-GC_DM_scattering
```

Or, if you were looking for neutrinos produced in the Sun due to WIMP annihilation with the IceCube Upgrade, you could use:

```
IC93-2024-solar_WIMP_annihilation
```

# Reproducibility

Before unblinding, we will require that someone is able to run the code and find the same results as the analyzer.
This needs to be run on a IceCube-maintained machine, __i.e.__ the cobalts, rather than an institutional cluster.
While the exact requirements will vary based on the analysis, usually this requires running each step of the analysis chain up to and including the snesitivity for one point in the parameter space.
The BSM technical team will meet with you when we assign a working group reviewer and discuss options for reproducibility that make sense for the individual analysis

While there is a broad range of things that can make a script non-reproducible, the most common is random number generation.
This is used for many common analysis steps such as background scrambling, poisson realizations, and minimization.
In order to make sure this is consistent, across code executions, please make sure to seed the random number generator.

Another major component of reproducibility is code versioning.
While things are generally pretty consistent in their implementation, it is best to use the same versions of all packages.
To this end, the analyzer should point to the icetray version and setup script being used.
Furthermore, if the analysis is Python based, the analyzer may use a package like `poetry` to track their dependencies.
This will allow the user to create a virtual environment that tracks the packages and can be eeasily used by others.
You can install `poetry` with
``` bash
> poetry new <project_name>

> poetry env use `which python`

> poetry shell

> poetry add numpy
```
This will create a `pyproject.toml` file which will others to use an identical environment to yours.
If you want to use an environment that someone else has made, simply navigate to the directory whith the `pyproject.toml` file and do
```bash
> poetry init

> poetry shell
```

We request that after the reviewer has verified the code, you tag a release of the code as it was when you unblinded so that we have it for reference.
