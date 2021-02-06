from aitextgen.utils import GPT2ConfigCPU
from aitextgen import aitextgen
from aitextgen.TokenDataset import TokenDataset
from aitextgen.tokenizers import train_tokenizer

vocab_file = "aitextgen-vocab.json"
merges_file = "aitextgen-merges.txt"

ai = aitextgen(model="./pytorch_model.bin", vocab_file=vocab_file, merges_file=merges_file, config='./config.json')

