from extension_bark_legacy.create_voice_string import create_voice_string
from extension_bark_legacy.get_speaker_gender import get_speaker_gender
from typing import Union
import gradio as gr


def generate_choice_string(use_v2: bool, language: str, speaker_id: Union[int, str]):
    history_prompt = create_voice_string(language, speaker_id, use_v2)
    gender = get_speaker_gender(history_prompt)
    return gr.Markdown(value=f"Chosen voice: {history_prompt}, Gender: {gender}")
