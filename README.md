# Boolfuck on Tracery

This project implements the [Boolfuck](http://samuelhughes.com/boof/) language in [Tracery](http://tracery.io/), relying on a bug which allows delayed, programmatic expansion of Tracery variables.

To convert a Boolfuck program defined in `program.bf` to Tracery, run the following command:

```
python bftracery.py program.bf
```

To convert the Boolfuck program and simulate keyboard input from `input.txt`, run the following command:

```
python bftracery.py program.bf -i input.txt
```

In both cases the resulting Tracery grammar will be written to `program.bf.json`.
