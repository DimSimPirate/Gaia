Comments on Python-generated content
====================================

Missing or duplicate sensor readings
------------------------------------

Each combination of sensor, timestamp and chemical should have exactly one reading.  reading_counts_all.png shows the actual reading counts for all the timestamps in the dataset.  reading_counts_irregular_only.png shows the same information for only the timestamps where there are anomalies.

This shows that there are numerous missing readings for methyloslomene corresponding exactly to duplicate readings for agoc (suggesting that the duplicate agoc readings may actually be mislabelled methylosmolene readings).  


Identifying polluting factories
-------------------------------

sensor_reading_labels.mp4 is an animation combining factory and sensor locations with time series data of sensor readings, wind speed and wind direction.  This shows that:

* The sensors show persistent background readings (most likely noise) even when they are upwind of the factories.  
* Unusually large chemical readings typically
  - only occur when a sensor is close to the streamline from a factory
  - show the same chemicals for the same factories (indicating which factories emit which chemicals).  Incriminating frames from this video are in the smoking_guns folder.  The chemicals released by the factories are:
    . Indigo Sol Boards: Applumonia
    . Kasios Office Furniture:  Methylosmolene, Agoc
    . Radiance ColourTek:  Agoc
    . Roadrunner Fitness Electronics: Chlorodinine, Methylosmolene, Agoc
  - Only happen occasionally (indicating that the chemicals are released intermittently)


Data availability and sensor calibration
----------------------------------------

sensor_readings_scatterplot.png shows a time series of wind and sensor data.  This shows that the data is not continuous, but occurs in three one-month periods - April, August and December 2016. 

sensor_readings_distributions.png shows the distributions of readings for each chemical from each sensor for each of the three months for which data is available.  These indicate apparent drifts in sensor calibration:
* The _levels_ of the readings from sensor 4 (only) increase over the three periods.
* The _variabilities_ in the readings from sensors 5 and 9 (only) increase over the three periods.  


Source code
-----------

Images for all these visualizations were produced using the Jupyter notebooks shown in data_prep.html and visualizations.html.  The animation was produced as still images (one for each frame) which were combined into a video using [ffmpeg](https://www.ffmpeg.org/).



