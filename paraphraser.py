import numpy as np
import pandas as pd
import os
import torch

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


class Paraphraser:
    def __init__(self, model_path, device="cpu"):
        self.device = torch.device(device)
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_path).to(self.device)

    def _paraphrase(self, question, **kwargs):
        num_beams = kwargs.get("num_beams", 5)
        num_beam_groups = kwargs.get("num_beam_groups", 5)
        num_return_sequences = kwargs.get("num_return_sequences", 5)
        repetition_penalty = kwargs.get("repetition_penalty", 10.0)
        diversity_penalty = kwargs.get("diversity_penalty", 3.0)
        no_repeat_ngram_size = kwargs.get("no_repeat_ngram_size", 2)
        temperature = kwargs.get("temperature", 0.7)
        max_length = kwargs.get("max_length", 128)

        input_ids = self.tokenizer(
            f"paraphrase: {question}",
            return_tensors="pt",
            padding="longest",
            max_length=max_length,
            truncation=True,
        ).input_ids.to(self.device)

        outputs = self.model.generate(
            input_ids,
            temperature=temperature,
            repetition_penalty=repetition_penalty,
            num_return_sequences=num_return_sequences,
            no_repeat_ngram_size=no_repeat_ngram_size,
            num_beams=num_beams,
            num_beam_groups=num_beam_groups,
            max_length=max_length,
            diversity_penalty=diversity_penalty,
        )

        res = self.tokenizer.batch_decode(outputs, skip_special_tokens=True)
        return res

    def paraphrase(self, question, **kwargs):
        return self._paraphrase(question, **kwargs)[:kwargs.get("num_return_sequences", 5)]
