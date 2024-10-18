# Simple Backround Processing With Redis Queue (RQ) With Python
This is source code and notes for a [livestream](https://youtube.com/live/sfLBdTO-wMg) I did on Redis Queue.

The notes are [here](./notes.md)

## How to run the simple demo
1. Create a virtual environment and activate it

2. Install dependencies
```bash
$ pip3 install -r requirments.txt
```

You need to have Redis installed.

3. Run the worker script
```bash
rq worker -s
```

4. Run the RQ Dashboard to monitor tasks
``` bash
rq dashboard --port 3000
```
