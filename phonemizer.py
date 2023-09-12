from allosaurus.app import read_recognizer
from transformers import pipeline
from transformers import Wav2Vec2PhonemeCTCTokenizer
from huggingface_hub import notebook_login
from datasets import load_dataset, load_metric
from datasets import ClassLabel
import random
import pandas as pd
from IPython.display import display, HTML

import transformers
import torchaudio

class phonemizer:
    def __init__(self):
        pass

    def phonemize(self, num_examples=10):
        notebook_login()

        dataset = load_dataset("timit_asr")
        print(dataset)

        dataset = dataset['train'].remove_columns(["dialect_region", "speaker_id"])

        assert num_examples <= len(dataset)
        picks = []
        for _ in range(num_examples):
            pick = random.randint(0, len(dataset)-1)
            while pick in picks:
                pick = random.randint(0, len(dataset)-1)
            picks.append(pick)

        df = pd.DataFrame(dataset[picks])

        with open("data.html", "w") as file:
            file.write(df.to_html())

        # bundle = torchaudio.pipelines.WAV2VEC2_ASR_BASE_960H
        # classifier = Wav2Vec2PhonemeCTCTokenizer(bundle.get_labels())
        # return classifier.phonemize("It is speech recognition")

        # Allosaurus basic instance
        # model = read_recognizer("eng2102")
        # return model.recognize("Recordings/mic.wav", timestamp=True)

test_obj = phonemizer()
test_obj.phonemize()
