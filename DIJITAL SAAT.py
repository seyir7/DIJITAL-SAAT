import tkinter as tk
from tkinter import colorchooser
import time
import random

# Güzel sözler listesi
beautiful_quotes = [
    "Hayat kısa, kuşlar uçuyor.",
    "Mutluluk paylaşıldıkça büyür.",
    "Gülümse, çünkü her şey güzel olacak.",
    "Bugün yeni bir başlangıç.",
    "Hayal et, inan, başar.",
    "Kendine inan, her şey mümkün.",
    "Güzel ol, güzel gör, güzel düşün.",
    "Düşünmek, hayatı değiştirebilir.",
    "Sabır, başarının anahtarıdır.",
    "Her şeyin başı sağlık."
]

# Yeşil renk tonları
green_shades = [
    "#7CFC00", "#00FF00", "#32CD32", "#228B22", "#008000", 
    "#006400", "#9ACD32", "#ADFF2F", "#2E8B57", "#3CB371"
]

# Mavi renk tonları
blue_shades = [
    "#1E90FF", "#4682B4", "#5F9EA0", "#87CEFA", "#00BFFF"
]

# Beyaz renk
white_color = "#FFFFFF"

# Ana pencere
root = tk.Tk()
root.title("Dijital Saat")
root.geometry("500x300")
root.resizable(False, False)

# Etiketler
time_label = tk.Label(root, font=("Helvetica", 48), fg="#7CFC00") 
time_label.pack(expand=True)

# Tarih konumu ve rengi yazı tipi
date_label = tk.Label(root, font=("Helvetica", 16), fg="white")
date_label.place(relx=1.0, rely=1.0-37.8/500, anchor="se")

quote_label = tk.Label(root, font=("Helvetica", 14), fg="red", bg="black")
quote_label.pack()

# Başlangıç renkleri
current_hour_color = random.choice(green_shades)
current_minute_color = white_color
current_second_color = random.choice(blue_shades)
quote_index = 0  # İlk güzel söz

# Saatin rengini, dakikanın rengini ve saniyenin rengini değiştirme özelliği
def update_time():
    global current_hour_color, current_minute_color, current_second_color, quote_index

#Zaman formatları
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%d/%m/%Y")
    
    # Saat, dakika ve saniye renklerini ayarlıyoruz
    time_label.config(text=current_time, fg=current_hour_color)
    date_label.config(text=current_date, fg=current_minute_color)

    # Güzel söz değişim zamanaları
    quote_label.config(text=beautiful_quotes[quote_index])

    # Renk değişim zamanları
    current_hour_color = random.choice(green_shades)
    current_second_color = random.choice(blue_shades)
    current_minute_color = white_color

    # SÖZ DEĞİŞİM ZAMANLARI
    quote_index = (quote_index + 1) % len(beautiful_quotes)

    root.after(1000, update_time)  # 1 saniye sonra tekrar çalıştır

# Renk seçici fonksiyonu
def change_bg_color():
    color_code = colorchooser.askcolor(title="Arka Plan Rengi Seçin")  # Renk seçici
    if color_code[1]:
        root.config(bg=color_code[1])  # Seçilen rengi arka plan olarak ayarla
        time_label.config(bg=color_code[1])  # Saatin arka planını da değiştir
        date_label.config(bg=color_code[1])  # Tarihin arka planını değiştir
        quote_label.config(bg=color_code[1])  # Güzel söz etiketinin arka planını değiştir

# Renk butonunu ekle
color_button = tk.Button(root, text="Renk Seç", command=change_bg_color, font=("Helvetica", 12), fg="black", bg="lightblue")
color_button.place(x=20, y=260)

# başlat
update_time()

# Pencereyi çalıştır
root.mainloop()
