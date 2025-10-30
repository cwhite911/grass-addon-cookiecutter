#!/usr/bin/env python

##############################################################################
# MODULE:    {{ cookiecutter.tool }}
#
# AUTHOR(S): {{ cookiecutter.author_name }} <{{ cookiecutter.email }}>
#
# PURPOSE:   {{ cookiecutter.description }}
#
# COPYRIGHT: (C) {% now 'utc', '%Y' %} by {{ cookiecutter.author_name }} and the GRASS Development Team
#
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
#            for details.
##############################################################################

"""{{ cookiecutter.description }}"""

# %module
# % description: {{ cookiecutter.description }}
# % keyword: raster
# % keyword: algebra
# % keyword: random
# %end
# %option G_OPT_R_INPUT
# %end
# %option G_OPT_R_OUTPUT
# %end


import sys
import atexit
import numpy as np
import grass.script as gs
from grass.tools import Tools


def main():

    # initalize tools
    tools = Tools()

    # get input options
    options, flags = gs.parser()
    input_raster = options["input"]
    output_raster = options["output"]

    # if changing computational region is needed, uncomment
    # gs.use_temp_region()

    # run analysis
    tmp_gauss_surface = tools.r_surf_gauss(output=np.array)
    tools.r_mapcalc(expression=f"{output_raster} = {input_raster} + {tmp_gauss_surface}")

    # save history into the output raster
    gs.raster_history(output_raster, overwrite=True)


if __name__ == "__main__":
    sys.exit(main())
