from dataclasses import dataclass
import draccus


# Choice Registry lets you define a choice of implementations that can be selected at runtime
@dataclass
class ModelConfig(draccus.ChoiceRegistry):
    pass


@ModelConfig.register_subclass('gpt')
@dataclass
class GPTConfig(ModelConfig):
    """GPT Model Config"""
    num_layers: int = 12
    num_heads: int = 12
    hidden_size: int = 768


@ModelConfig.register_subclass('bert')
@dataclass
class BERTConfig(ModelConfig):
    """BERT Model Config"""
    num_layers: int = 12
    num_heads: int = 12
    hidden_size: int = 768
    dropout: float = 0.1


@dataclass
class TrainConfig:
    """Training Config for Machine Learning"""
    workers: int = 8                  # The number of workers for training
    exp_name: str = 'default_exp'     # The experiment name

    model: ModelConfig = BERTConfig()  # The model configuration


@draccus.wrap()
def main(cfg: TrainConfig):
    print(f"Training {cfg.exp_name} with {cfg.model.dropout} dropout...")

if __name__ == '__main__':
    cfg = TrainConfig()
    cfg.model.dropout=0.2
    cfg.exp_name='de'
    main(cfg)