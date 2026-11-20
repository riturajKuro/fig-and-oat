import json, os, subprocess, sys
from faster_whisper import WhisperModel
FF = r"C:\Users\DELL\Projects\sfc_laptop_de26d20\ffmpeg\ffmpeg.exe"
R = r"C:\Users\DELL\AppData\Local\Temp\claude\17f9b7d0e0fd4553\25cc2d0d-f4a0-4f43-8b9b-b3a78a520184\scratchpad\refs"
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = {"ugc-5": os.path.join(R, "influencer", "ugc-5-luna-livingroom.mp4"),
       "_skip": None,
       "ugc-1": os.path.join(R, "videos", "ugc-1-routine-howto-FINAL.mp4"),
       "ugc-2": os.path.join(R, "videos", "ugc-2-not-your-razor.mp4"),
       "ugc-4": os.path.join(R, "influencer", "ugc-creator-stick.mp4")}
m = WhisperModel("small.en", device="cpu", compute_type="int8")
for k, v in SRC.items():
    if k!="ugc-5": continue
    wav = os.path.join(HERE, k + ".wav")
    subprocess.run([FF, "-v", "error", "-y", "-i", v, "-ac", "1", "-ar", "16000", wav], check=True)
    import wave, numpy as np
    with wave.open(wav, "rb") as wf:
        audio = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0
    segs, _ = m.transcribe(audio, word_timestamps=True, beam_size=5, vad_filter=False)
    words = [{"w": w.word.strip(), "s": round(w.start, 3), "e": round(w.end, 3), "p": round(w.probability, 2)}
             for s in segs for w in s.words]
    json.dump(words, open(os.path.join(HERE, k + "_words.json"), "w"), indent=0)
    print("==", k, len(words), "words")
    print(" ".join(f"{x['w']}[{x['s']:.2f}]" for x in words))
