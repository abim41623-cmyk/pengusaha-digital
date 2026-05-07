from flask import Flask, render_template, request

app = Flask(__name__)

# Data Produk (Simulasi data)
produk_data = [
    {"nama": "Jasa Pembuatan Website", "deskripsi": "Website profesional untuk bisnis Anda.", "harga": "Rp 1.500.000"},
    {"nama": "Social Media Management", "deskripsi": "Optimasi konten Instagram dan TikTok.", "harga": "Rp 800.000"},
    {"nama": "SEO Optimization", "deskripsi": "Meningkatkan ranking website di Google.", "harga": "Rp 1.000.000"}
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/produk')
def produk():
    return render_template('produk.html', produk=produk_data)

@app.route('/kontak', methods=['GET', 'POST'])
def kontak():
    if request.method == 'POST':
        nama = request.form.get('nama')
        email = request.form.get('email')
        return render_template('respon.html', nama=nama, email=email)
    return render_template('kontak.html')

if __name__ == '__main__':
    app.run(debug=True)
