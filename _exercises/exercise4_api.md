# Exercise 4 - working with data from API

In this exercise sheet, you will work with API in python

> [!NOTE]
> These exercises covers lecture 11.

You need to go through the lecture note and/or video in order to be able to do these exercises

## 0. Resrobot time table API

&nbsp; a) Make a function for doing get request for time tables API in resrobot as we didn't have a function in the lecture notes.

&nbsp; b) Find the number of transports arriving to Göteborg centralstationen. 

&nbsp; c) Find the number of transports departuring from Göteborg centralstationen. 

&nbsp; d) Find the trams departuring from Göteborg centralstationen, their destinations and time. Note that trams in Swedish is "spårvagn" or in the dataset denoted as "Spårväg". 

&nbsp; e) See if you can plot in a map points corresponding to directions of each departuring tram. 

&nbsp; f) Do more EDA on this data to find things that you are interested in. 

## 1. Plan travel using resrobot route planner  

&nbsp; a) Find the stops names between Göteborg and Lund for a train that is departuring from Göteborg. 

&nbsp; b) Find stops names, and times between two different cities of your choice in Sweden. 

&nbsp; c) See if you can plot in a map points of a train on each stops between two locations of your choice. 


## 2. Make digital display boards for trains/trams

&nbsp; a) Make a departure board for trams and buses for a station of your choice, e.g. Göteborg korsvägen. It displays how many minutes are left to wait. An example could be to print out 

```
spårvagn 8 mot angered 2 minuter
spårvagn 2 mot högsbohöjd 5 minuter
...
```

&nbsp; b) Make a departure board for trains. Here list the trains, their destinations and the time it departures.

&nbsp; c) Make an arrival board for trains. Here list the trains, their destinations and the time it arrives.
