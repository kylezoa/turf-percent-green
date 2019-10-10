# turf-percent-green
Turfgrass quality can be measured based on a percent green value. Images collected in a lightbox may contain part of the lightbox and needs to be removed in a percent green calculation. Image calculations done on the HSV scale.

This project replaces Fiji/ImageJ macros, exporting a time-series dataset of repetitive blocks to a pandas dataframe for further analysis.

Dependencies:
* Python 3.7
* pandas
* opencv2
* numpy

Contact me at my profile email if you need some edits for your folder structure. My script follows a vary naive approach.

Relevant literature:
* Zhang, C., G. D. Pinnix, Z. Zhang, G. L. Miller, and T. W. Rufty. 2017. [Evaluation of Key Methodology for Digital Image Analysis of Turfgrass Color Using Open-Source Software.](https://dl.sciencesocieties.org/publications/cs/abstracts/57/2/550) Crop Sci. 57:550-558. doi:10.2135/cropsci2016.04.0285
  * North Carolina State University's Turfgrass DIA ImageJ [plugin](https://www.turffiles.ncsu.edu/nc-state-turfgrass-dia-imagej-plugin/)
* Karcher, D. E., and M. D. Richardson. 2003. [Quantifying Turfgrass Color Using Digital Image Analysis.](https://dl.sciencesocieties.org/publications/cs/abstracts/43/3/943) Crop Sci. 43:943-951. doi:10.2135/cropsci2003.9430
* [Image analysis tools for turfgrass managers and scientists](https://turf.umn.edu/news/image-analysis-tools-turfgrass-managers-and-scientists) by Garett Heineck
* Reiter, M., J. Friell, B. Horgan, D. Soldat, and E. Watkins. 2017. [Drought Response of Fine Fescue Mixtures Maintained as a Golf Course Fairway. International Turfgrass Society Research Journal](https://dl.sciencesocieties.org/publications/its/abstracts/13/1/65) 13:65-74. doi:10.2134/itsrj2016.06.0460
