import torch
from pybert.configs.basic_config import config
from pybert.io.bert_processor import BertProcessor
from pybert.model.bert_for_multi_label import BertForMultiLable


def main(text,arch,max_seq_length,do_lower_case,data_name):
    processor = BertProcessor(vocab_path=config['bert_vocab_path'], do_lower_case=do_lower_case)
    label_list = processor.get_labels(data_name)
    id2label = {i: label for i, label in enumerate(label_list)}
    model = BertForMultiLable.from_pretrained(config['checkpoint_dir'] /f'{arch}', num_labels=len(label_list))
    tokens = processor.tokenizer.tokenize(text)
    if len(tokens) > max_seq_length - 2:
        tokens = tokens[:max_seq_length - 2]
    tokens = ['[CLS]'] + tokens + ['[SEP]']
    input_ids = processor.tokenizer.convert_tokens_to_ids(tokens)
    input_ids = torch.tensor(input_ids).unsqueeze(0)  # Batch size 1, 2 choices
    logits = model(input_ids)
    probs = logits.sigmoid()
    return probs.cpu().detach().numpy()[0]

if __name__ == "__main__":
    text = '''Plotly Graphing Library for MATLAB®. Plotly Graphing Library for MATLAB® - Create interactive charts in your web browser with MATLAB® and Plotly
Version: 2.2.10
MATLAB is a registered trademarks of The MathWorks, Inc.
The latest version of the wrapper can be downloaded here.
Once downloaded, run plotlysetup_offline() to get started
If you have a plotly bundle url of the form 'http://cdn.plot.ly/plotly-latest.min.js', then run instead
`plotlysetup_offline('plotly_bundle_url')
For online use, run plotlysetup_online('your_username', 'your_api_key') to get started.
NOTE: plotlyupdate.m is currently turned off.
Please manually download and setup the latest version
of the wrapper by following the installation instructions above.
Convert your MATLAB® figures into online Plotly graphs with a single line of code:

Also, access other Plotly services and graphs programatically. Like, publication-quality image export:
and Plotly figure retrieval:
This lives here: https://plot.ly/matlab
https://community.plotly.com/c/api/matlab/
Please do! This is an open source project. Check out the issues or open a PR!
We want to encourage a warm, welcoming, and safe environment for contributing to this project. See the code of conduct for more information.
MIT © 2021 Plotly, Inc.'''
    max_seq_length = 512
    do_loer_case = True
    arch = 'bert'
    data_name = '0'
    probs = main(text,arch,max_seq_length,do_loer_case,data_name)
    print(probs)
    
#   '''
#   #output
#   [0.98304486 0.40958735 0.9851305  0.04566246 0.8630512  0.07316463]
#   '''
