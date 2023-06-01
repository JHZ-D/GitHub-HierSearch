
from pathlib import Path
BASE_DIR = Path('pybert')
config = {
    'raw_data_path': BASE_DIR / 'dataset' / '{data_name}' / 'train.csv',
    'test_path': BASE_DIR / 'dataset' / '{data_name}' / 'test.csv',
    'test_label_path': BASE_DIR / 'dataset' / '{data_name}' / 'test_labels.csv',

    'data_dir': BASE_DIR / 'dataset' / '{data_name}',
    'log_dir': BASE_DIR / 'output/log' / '{data_name}',
    'writer_dir': BASE_DIR / "output/TSboard",
    'figure_dir': BASE_DIR / "output/figure" / '{data_name}',
    'checkpoint_dir': BASE_DIR / "output/checkpoints" / '{data_name}',
    'predict_dir': BASE_DIR / "output" / '{data_name}',
    'cache_dir': BASE_DIR / 'model/',
    'result': BASE_DIR / "output/result",

    'bert_vocab_path': BASE_DIR / 'pretrain/bert/base-uncased/bert_vocab.txt',
    'bert_config_file': BASE_DIR / 'pretrain/bert/base-uncased/config.json',
    'bert_model_dir': BASE_DIR / 'pretrain/bert/base-uncased',

    'xlnet_vocab_path': BASE_DIR / 'pretrain/xlnet/base-cased/spiece.model',
    'xlnet_config_file': BASE_DIR / 'pretrain/xlnet/base-cased/config.json',
    'xlnet_model_dir': BASE_DIR / 'pretrain/xlnet/base-cased',

    'albert_vocab_path': BASE_DIR / 'pretrain/albert/albert-base/30k-clean.model',
    'albert_config_file': BASE_DIR / 'pretrain/albert/albert-base/config.json',
    'albert_model_dir': BASE_DIR / 'pretrain/albert/albert-base'


}

