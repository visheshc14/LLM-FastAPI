import json
import torch
from torch.utils.data import Dataset
from minGPT.mingpt.model import GPT
from minGPT.mingpt.trainer import Trainer
import fire


class TextDataset(Dataset):
    def __init__(self, dataset, model):
        self.dataset = dataset
        self.model = model

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, index):
        text = self.dataset[index]["text"]
        tokenized_text = self.model.encode(text)  # Encode the text into tensor
        return tokenized_text


def train_model(fp: str, output_dir: str, max_epochs: int):
    # Load the dataset
    with open(fp, 'r') as file:
        dataset = json.load(file)

    # Initialize the model
    model_config = GPT.get_default_config()
    model_config.model_type = 'gpt2'
    model_config.vocab_size = 50257  # openai's model vocabulary
    model_config.block_size = 1024   # openai's model block_size (i.e. input context length)
    model = GPT(model_config)

    # Create the dataset
    train_dataset = TextDataset(dataset, model)

    # Train the model
    train_config = Trainer.get_default_config()
    train_config.learning_rate = 5e-4  # many possible options, see the file
    train_config.max_epochs = max_epochs
    train_config.batch_size = 32
    train_config.distributed_backend = 'dp'  # use data parallelism
    trainer = Trainer(train_config, model, train_dataset)
    trainer.run()

    # Save the model
    torch.save(model.state_dict(), output_dir)


if __name__ == '__main__':
    fire.Fire(train_model)