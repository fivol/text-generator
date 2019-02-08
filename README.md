## To train model use:
- -f `<text file name>`
- -o `<model name to save>` (without extension, default = 'model')

### Example:
```
python text_generator.py -f example_texts/voina-i-mir.txt
python text_generator.py -f example_texts/voina-i-mir.txt -o new_model
```
 
## To generate text use:
- -g `<model name>` (without extension)
- -s `<seed>` (not nessesary)
- -o `<output text file name to save>` (not nessesary, default - console output)
- -b `<begin word to text generation>` (not nessesary, default - random)
- -l `<required text length>` (not nessesary, default = 10)
- -p `<power>` (default = 1, affects word generation style. Raised to a power frequency of each next word. Float number) 
[than greater the degree, the less likely the small frequency word will fall]


### Example:
```
python text_generator.py -g model
python text_generator.py -g model -o result_text.txt -b андрей -l 30 -s 456
```

## Enjoy!