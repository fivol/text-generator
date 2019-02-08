## To train model use:
- -f <text file name>
- -o <model name to save> (without extension, default = 'model')

### Example:
```
python text_generator.py -f example_texts/voina-i-mir.txt
```
 
## To generate text use:
- -g <model name> (without extension)
- -s <seed> (not nessesary)
- -o <output text file name to save> (not nessesary, default - console output)
- -b <begin word to text generation> (not nessesary, default - random)
- -l <required text length> (not nessesary, default = 10)

### Example:
```
python text_generator.py -g model
```

## Enjoy!