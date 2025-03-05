import random
import tkinter as tk

# 名言リスト（英語、日本語訳、意味）
quotes = [
    {
        "english": "The only limit to our realization of tomorrow is our doubts of today.",
        "japanese": "明日を実現するための唯一の制約は、今日の疑念である。",
        "meaning": "未来を切り開くためには、現在の不安や疑いを乗り越えることが大切。"
    },
    {
        "english": "Do what you can, with what you have, where you are.",
        "japanese": "できることを、持っているもので、今いる場所でやりなさい。",
        "meaning": "完璧な環境を待つのではなく、今ある状況で最善を尽くすことが成功への近道。"
    },
    {
        "english": "It does not matter how slowly you go as long as you do not stop.",
        "japanese": "止まらない限り、どんなに遅く進んでも問題ない。",
        "meaning": "進みが遅くても、諦めずに努力を続ければ目標に到達できる。"
    },
    {
        "english": "Act as if what you do makes a difference. It does.",
        "japanese": "自分の行動が変化を生むと信じて行動しなさい。実際に変化を生むのだから。",
        "meaning": "小さな行動でも積み重ねることで大きな影響を与える。"
    },
    {
        "english": "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "japanese": "成功は最終的なものではなく、失敗は致命的ではない。大事なのは続ける勇気だ。",
        "meaning": "成功も失敗も一時的なもの。大切なのは挑戦し続けること。"
    }
]

# 名言を取得する関数
def show_quote():
    quote = random.choice(quotes)
    english_text.set(f"📜 {quote['english']}")  # 英語
    japanese_text.set(f"📝 {quote['japanese']}")  # 日本語訳
    meaning_text.set(f"💡 {quote['meaning']}")  # 意味の説明

# 🎨 GUIアプリを作成
root = tk.Tk()
root.title("✨ 名言ジェネレーター ✨")
root.geometry("600x400")  # ウィンドウサイズを設定
root.configure(bg="#f4f4f4")  # 背景色を設定

# ラベルのテキストを格納する変数
english_text = tk.StringVar()
japanese_text = tk.StringVar()
meaning_text = tk.StringVar()

english_label = tk.Label(root, textvariable=english_text, font=("Arial", 12, "bold"), wraplength=500, justify="center", bg="#f4f4f4")
english_label.pack(pady=5)

japanese_label = tk.Label(root, textvariable=japanese_text, font=("Arial", 12), wraplength=500, justify="center", bg="#f4f4f4", fg="#333333")
japanese_label.pack(pady=5)

meaning_label = tk.Label(root, textvariable=meaning_text, font=("Arial", 12, "italic"), wraplength=500, justify="center", bg="#f4f4f4", fg="#666666")
meaning_label.pack(pady=10)

# 🔘 名言を取得するボタン
button = tk.Button(root, text="📜 名言を表示 📜", font=("Arial", 12, "bold"), command=show_quote, bg="#4CAF50", fg="white", padx=15, pady=10, relief="raised", borderwidth=3)
button.pack(pady=10)

# アプリ起動
root.mainloop()
