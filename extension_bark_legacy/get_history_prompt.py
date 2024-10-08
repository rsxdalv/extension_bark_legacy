from typing import Optional
from extension_bark_legacy.history_to_hash import history_to_hash
from extension_bark_legacy.create_voice_string import create_voice_string


def get_history_prompt(
    language: Optional[str],
    speaker_id: Optional[int],
    useV2: bool,
    history_prompt: Optional[str],
    use_voice: bool,
):
    if history_prompt is None:
        history_prompt = (
            create_voice_string(language, speaker_id, useV2) if use_voice else None  # type: ignore
        )
        history_prompt_verbal = history_prompt or "None"
    else:
        history_prompt_verbal = (
            history_prompt
            if isinstance(history_prompt, str)
            else f"from_{history_to_hash(history_prompt)[:8]}"
        )

    return history_prompt, history_prompt_verbal
