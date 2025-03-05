import note_seq
from note_seq.protobuf import music_pb2

sequence = music_pb2.NoteSequence()

### 1️⃣ 深みのある低音（長く続く）
drone_notes = [24, 28, 31, 35]  # C1, E1, G#1, Bb1
start_time = 0.0

for i, pitch in enumerate(drone_notes):
    note = sequence.notes.add()
    note.pitch = pitch
    note.start_time = start_time
    note.end_time = start_time + 120.0  # 120秒持続
    note.velocity = 50 + (i * 5)  # 強弱をつける

### 2️⃣ 環境音風の動き（不規則な倍音）
pad_notes = [48, 50, 52, 55]  # C3, D3, E3, G3
pad_times = [10, 25, 40, 55, 70, 85, 100]  # 徐々に入る

for i, pitch in enumerate(pad_notes):
    note = sequence.notes.add()
    note.pitch = pitch
    note.start_time = pad_times[i]
    note.end_time = pad_times[i] + 15.0  # ゆっくりフェードアウト
    note.velocity = 60

### 3️⃣ 「映像向け」な効果音（不規則なノイズ）
noise_notes = [84, 86, 89, 92]  # 高音のランダムなノイズ
noise_times = [5, 18, 32, 47, 58, 66, 72, 90]  # ランダムなタイミング

for i, pitch in enumerate(noise_notes):
    note = sequence.notes.add()
    note.pitch = pitch
    note.start_time = noise_times[i]
    note.end_time = noise_times[i] + 2.5
    note.velocity = 70

### 4️⃣ メロディ（不気味なゆっくりとした旋律）
melody_notes = [62, 65, 69, 71, 74]  # D4, F4, A#4, B4, D#5
melody_times = [15, 33, 51, 68, 80]  # 徐々に増える

for i, pitch in enumerate(melody_notes):
    note = sequence.notes.add()
    note.pitch = pitch
    note.start_time = melody_times[i]
    note.end_time = melody_times[i] + 4.0
    note.velocity = 75

sequence.total_time = 120.0  # 120秒

# 新しいファイル名で保存
note_seq.sequence_proto_to_midi_file(sequence, "pro_dark_ambient.mid")

print("MIDIファイルを生成しました: pro_dark_ambient.mid")
