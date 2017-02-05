Simple JSON to String parser. Aims at making reading JSON a little more human friendly. 
It follows the builtin Python String format strategy ([see here](https://docs.python.org/2/library/string.html)).

It just reads from `STDIN` and writes to `STDOUT`. 

Example

```
$ echo '{"time": "2017-01-01 20:00:00 PST", "message": "Some message"}' | json-to-pattern -p "{time} - {message}
2017-01-01 20:00:00 PST - Some message
```

This was thought as a bridge between logback/logstash JSON output format and human readible, the 
default pattern is `[{thread_name:20}] {level:>5} {@timestamp} - {message}`.

# Installing

## Brew

```
$ brew tap hartimer/tap
$ brew install hartimer/tap/json-to-pattern
```

## Manual

Copy [json-to-pattern](json-to-pattern) to your `PATH`.

# Usage

1. `cat file.json | json-to-pattern [-p '<pattern>']`
2. `tail [-f] file.json | json-to-pattern [-p '<pattern>']`
