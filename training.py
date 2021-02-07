from aitextgen.utils import GPT2ConfigCPU
from aitextgen import aitextgen
from aitextgen.TokenDataset import TokenDataset
from aitextgen.tokenizers import train_tokenizer

file_name = "data.txt"
train_tokenizer(file_name)
vocab_file = "aitextgen-vocab.json"
merges_file = "aitextgen-merges.txt"

ai = aitextgen(vocab_file=vocab_file, merges_file=merges_file, config=GPT2ConfigCPU())

data = TokenDataset(file_name, vocab_file=vocab_file, merges_file=merges_file, block_size=64)

ai.train(data, batch_size=16, num_steps=10000)
ai.save('.')