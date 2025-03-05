import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from scipy.fftpack import fft, fftfreq

# 日本語フォント設定
plt.rcParams['font.family'] = 'MS Gothic'  # Windowsなら 'MS Gothic' / Macなら 'Hiragino Sans'
plt.rcParams['axes.unicode_minus'] = False  # マイナス記号のバグを防ぐ

# 設定
SAMPLE_RATE = 44100  # サンプリングレート（CD音質）
DURATION = 5  # 録音時間（秒）

def record_audio():
    print("🎤 録音中... 5秒間")
    audio = sd.rec(int(SAMPLE_RATE * DURATION), samplerate=SAMPLE_RATE, channels=1, dtype='float32')
    sd.wait()
    return audio.flatten()

def analyze_frequencies(audio):
    N = len(audio)
    fft_result = fft(audio)
    frequencies = np.abs(fft_result[:N//2])
    freq_axis = fftfreq(N, 1 / SAMPLE_RATE)[:N//2]
    return freq_axis, frequencies

def plot_frequencies(freq_axis, frequencies):
    plt.figure(figsize=(10, 5))
    plt.plot(freq_axis, frequencies, color='blue')
    plt.xlabel("周波数 (Hz)")
    plt.ylabel("振幅 (Amplitude)")
    plt.title("環境音の波動スペクトル")
    plt.grid()
    plt.xlim(0, 5000)
    plt.show()

def generate_tone(frequency, duration=3, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(2 * np.pi * frequency * t)
    return tone

def play_tone(frequency):
    print(f"🔊 {frequency}Hz の波動音を再生中...")
    sound = generate_tone(frequency)
    sd.play(sound, samplerate=SAMPLE_RATE)
    sd.wait()

# 実行
audio_data = record_audio()
freq_axis, frequencies = analyze_frequencies(audio_data)
plot_frequencies(freq_axis, frequencies)
play_tone(528)  # 528Hz の波動を流す