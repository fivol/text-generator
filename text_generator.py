import language_model
import argparse
import time


parser = argparse.ArgumentParser()

parser.add_argument('-s', dest="seed", default=time.time(), type=int)
parser.add_argument('-f', dest="file_path", default="_null_", type=str)
parser.add_argument('-g', dest="model_path", default="_null_", type=str)
parser.add_argument('-o', dest="output_name", default="_null_", type=str)
parser.add_argument('-b', dest="begin_word", default="", type=str)
parser.add_argument('-l', dest="text_length", default="10", type=int)
parser.add_argument('-p', dest="metrics_power", default="1", type=float)

args = parser.parse_args()

model = language_model.Text_generator(args.seed)

if args.file_path != "_null_":
    path = args.file_path
    file = open(path, 'r')
    file_content = file.read()
    file.close()
    model.fit(file_content)

    model_name = args.output_name
    if model_name == "_null_":
        model_name = "model"
    model.save_model(model_name)

    print(f"Model successfully saved (name = '{model_name}.pickle')")

elif args.model_path != "_null_":
    path = args.model_path
    model.load_model(path)

    text = model.generate(args.begin_word, length=args.text_length, power=args.metrics_power)
    if args.output_name != "_null_":
        file = open(args.output_name, 'w')
        file.write(text)
        file.close()
    else:
        print(text)
else:
    print("Incorrect launch parameters")
    print("Please, read README.md file")
