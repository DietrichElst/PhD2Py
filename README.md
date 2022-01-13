# PhD2Py
Converting the MATLAB code from my PhD to a more structured python code (and learning python on the way).

# Introduction

This piece of code is intended to reproduce results from my up and coming PhD.
The original code was written in MATLAB, comprised of mostly scripts and some functions and was quite chaotic.
With this project, I intend to learn about python, scipy, matplotlib...
It also gives the opportunity to structure the definition of both the problem and solving method.

## Theory

# Program structure

The previous MATLAB scripts are integrated into 2 classes: a problem structure and an accompanying problem sovler.
A problem structure contains all relevant physical constants, all properties that describe the system and the relevant parameters that define the state of the system.
Parameters can be lists of tuples, such that the solver can solve for all or a selected subset of points in parameter space. 
Finally, the solver also contains some methods to plot and save all of the data incsv or JSON format.
