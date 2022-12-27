# Sierpiński triangle fractal

I recently saw this fractal online and thought it would be cool to code it up as a fun exercise.


### ***How to run:***

Clone the repository:
```
$ git clone https://github.com/darbymccauley/sierpinski_triangle.git
```

Install the required dependencies:
```
$ pip install -r requirements.txt
```
Run:
``` 
$ python3 fractal.py [nsamples]
```

The default number of samples used to generate the image when run is 1000. However, this can be changed as desired with the optional `nsamples` flag in the command line or in an interactive session:
```
import fractal
t = fractal.Triangle()
t.run(N)
```


The following image is an example of the output and was generated with 10,000 samples.
<p align="center">
<img src="https://github.com/darbymccauley/sierpinski_triangle/blob/master/sample.png?raw=true" />
</p>
