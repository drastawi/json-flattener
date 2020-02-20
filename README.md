# Mongo JSON formatter

MongoDB takehome problem by Dominik Rastawicki.

This project contains a program that takes a JSON object as input and outputs a flattened version of the JSON object, with keys as the path to every terminal value in the JSON structure.


## Getting Started

This project uses python 3.8.0.

To run the program:

```sh
python json_formatter.py < sample.json
```
or 
```sh
cat sample.json | python json_formatter.py
```

where the `sample.json` is the file with JSON contents we'd like to flatten.

### Example

The following JSON object: 

```json
{
    "a": 1,
    "b": true,
    "c": {
        "d": 3,
        "e": "test"
    }
}
```

should output:

```json
{
    "a": 1,
    "b": true,
    "c.d": 3,
    "c.e": "test"
}
```

In this example the path to the terminal value `1` is `"a"` and the path to the terminal value `3` is `"c.d"`.

#### Assumptions

* The input file should be a JSON object
* All keys named in the original object should be simple strings without ‘.’ characters
* The input JSON should not contain arrays

## Test
 
To run tests:
 
```sh
python -m unittest json_formatter_test.py
```
