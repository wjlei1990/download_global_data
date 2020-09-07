This directory contains the eventlist files and CMT solution files. There are a few subdirectories:

1. CMT.1480
There are 1480 earthquake CMT files. It includes 1040 earthquakes used from GLAD-M15 to GLAD-M19. There are 440 extra events added in GLAD-M20. So there are total of 1480 events used from GLAD-M20 to GLAD-M20.

2. CMT.360
There are 360 earthquakes used as the held-out dataset in GLAD-M25. This events will be added into the inversion data data starting from GLAD-M26.

3. Subdirectory: `M25.source_inversion`
There are `400 + 500` earthqaukes picked after GLAD-M25. We will further picked subsets from this event pool and add them into the inversion dataset of GLAD-M26. To make the total number of earthqaukes larger than 2,000 in GLAD-M26.

#### Attention:
1. the CMT solutions are only used for data downloaded, but not for structure inversion, since some of them haven't been conducted in the source inversion.
