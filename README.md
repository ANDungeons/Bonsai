# Bonsai

__Koch ideas__
* Be able to standardize plots easily
  * Set colorscheme
  * Line/point style
  * Add error bars
  * Resize
  * Set axis values
  * Double y-axes
  * Highlight certain data points or lines
* Manipulate data
  * Be able to import new data and handle it accordingly
  * Change which data is being used (i.e., plot X vs Y, or X vs Z)
  * Tell which data goes to which axis
    * Multi-axis plots
    * Error bars
  * Filter data
    * Have move stringent filters (i.e., if max in some set, only use that set)
  * Envelope over data (this is kind of getting into postprocessing than solely plotting)

__Hoagland Thoughts__
* Data Stuctures
  * Primary data in a large multi-dimensional DataFrame
    * Multiple columns of "independent" descriptive data
    * (Potentially) multiple columns of "dependent" results data
  * Secondary data format of multiple two-dimensional DataFrames
    * Both axii being "independent" variables, and contents being results
    * Multi-level dict (or similar) to contain the numerous DataFrames
    * Meant for reading and/or writing two-dimensional tables, or plotting data
  * Be able to move from one format to the other
    * Extract multiple sets of two-dimensional data from primary structure
      * Also useful for providing data for visualization
    * Merge multiple layers of data into a single sructure
* Data Manipulation
  * Add new sets of data, including inserting new columns as needed
  * Envelope data
    * Select maximum or minimum data in certain sets
* Visualization
  * Standard visualizations: scatter or line plots of two-dimensional data
  * Colors: Have a default set of colormaps, but with full overwrite capability
    * Defaults dependent on the "independent" data the columns are
  * In general heavily rely on optional arguments with defaults
  * Have a standard Jupyter Notebook for pulling in a large DataFrame and then visualizing portions of it
