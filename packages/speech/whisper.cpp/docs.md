The current directory will have the built files of `whisper.cpp` (with cuda). By default it will run the following command:

```
ENTRYPOINT ./stream -m ./models/<model>.bin -t 4 8 --step 500 --length 5000
```

The model can be selected using the `WHISPER_MODEL` argument, defaulting to `small`.
