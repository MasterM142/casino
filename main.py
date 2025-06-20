from flask import Flask, render_template
import os

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'casino-secret-key-2024'

@app.route('/')
def index():
    """Homepage - Casino Hauptseite mit Spielauswahl"""
    return render_template('index.html')

@app.route('/mines')
def mines():
    """Mines Spiel"""
    return render_template('mines.html')

@app.route('/blackjack')
def blackjack():
    """Blackjack Spiel"""
    return render_template('blackjack.html')

# Zusätzliche Routen für zukünftige Spiele
@app.route('/roulette')
def roulette():
    """Roulette Spiel (für später)"""
    return render_template('roulette.html')

@app.route('/slots')
def slots():
    """Slot Machine (für später)"""
    return render_template('slots.html')

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    return f"""
    <div style="text-align: center; padding: 50px; background: #121826; color: #e2e8f0; font-family: Arial;">
        <h1>🎰 404 - Seite nicht gefunden</h1>
        <p>Die angeforderte Seite existiert nicht.</p>
        <a href="/" style="color: #00d4ff; text-decoration: none;">← Zurück zur Hauptseite</a>
    </div>
    """, 404

@app.errorhandler(500)
def internal_error(error):
    return f"""
    <div style="text-align: center; padding: 50px; background: #121826; color: #e2e8f0; font-family: Arial;">
        <h1>🎰 500 - Server Fehler</h1>
        <p>Ein interner Server-Fehler ist aufgetreten.</p>
        <a href="/" style="color: #00d4ff; text-decoration: none;">← Zurück zur Hauptseite</a>
    </div>
    """, 500

if __name__ == '__main__':
    # Stelle sicher, dass der templates Ordner existiert
    templates_path = os.path.join(os.path.dirname(__file__), 'templates')
    if not os.path.exists(templates_path):
        os.makedirs(templates_path)
        print(f"📁 Templates Ordner erstellt: {templates_path}")
    
    print("🎰 Casino Server startet...")
    print("=" * 50)
    print("📍 Verfügbare Casino Spiele:")
    print("   🏠 http://localhost:5000/ (Hauptseite)")
    print("   💣 http://localhost:5000/mines (Mines Spiel)")
    print("   ♠️  http://localhost:5000/blackjack (Blackjack)")
    print("=" * 50)
    print("🚀 Server läuft auf http://localhost:5000")
    print("💡 Drücken Sie Ctrl+C zum Beenden")
    
    # Starte den Development Server
    app.run(
        debug=True,          # Debug-Modus für Entwicklung
        host='0.0.0.0',      # Erreichbar von allen Netzwerk-Interfaces
        port=5000,           # Port 5000
        threaded=True        # Multi-Threading für bessere Performance
    )
