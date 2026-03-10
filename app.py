from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 1. Wyświetlamy stronę z poradami dla mechanika
@app.route('/')
def strona_glowna():
    # Flask automatycznie szuka tego pliku w folderze 'templates'
    return render_template('index.html')

# 2. Odbieramy ukrytą paczkę danych z przeglądarki (kliknięcie przycisku)
@app.route('/zglos_sukces', methods=['POST'])
def zglos_sukces():
    # Odbieramy dane w formacie JSON (format wymiany danych)
    dane = request.get_json()
    id_porady = dane.get('id_porady')
    
    # Wypisujemy w terminalu, żeby udowodnić, że działa
    print(f"\n🟢 BDOFIX INFO: Mechanik zgłosił sukces dla porady: {id_porady}!\n")
    
    # Odsyłamy odpowiedź do telefonu, że wszystko się udało
    return jsonify({"status": "sukces", "wiadomosc": "Zapisano w bazie BDOFIX!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)