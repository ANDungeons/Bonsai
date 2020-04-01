# Bonsai

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
  * Support use of matplotlib plots/figs kwargs (In general heavily rely on optional arguments with defaults)
    * Set colorscheme
    * Line/point style
    * Add error bars
    * Resize
    * Set axis values
    * Double y-axes
    * Multi-axis plots
    * Error bars
  * Highlight/filter certain data points
    * Based on non-plotted variables
    * Based on arbirarty functions (max, min, envel, etc.)
  * Standard visualizations:
    * Have a standard Jupyter Notebook for pulling in a large DataFrame and then visualizing portions of it
    * Standard letter quality plots of two-dimensional data
  * API Interface for custom plotting for individual needs
