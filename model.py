from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pustaka.sqlite3'

db = SQLAlchemy(app)

class Buku(db.Model):
	id = db.Column('buku_id', db.Integer, primary_key=True)
	judul = db.Column(db.String(100))
	pengarang = db.Column(db.String(30))
	penerbit = db.Column(db.String(30))

	def __init__(self, judul, pengarang, penerbit):
		self.judul = judul
		self.pengarang = pengarang
		self.penerbit = penerbit

class Anggota(db.Model):
	id = db.Column('anggota_id', db.Integer, primary_key=True)
	nama = db.Column(db.String(50))
	alamat = db.Column(db.String(250))

	def __init__(self, nama, alamat):
		self.nama = nama
		self.alamat = alamat

# pinjam = db.Table('pinjam',
# 		db.Column('buku_id', db.Integer, db.ForeignKey('buku.buku_id')),
# 		db.Column('anggota_id', db.Integer, db.ForeignKey('anggota.anggota_id'))
# 		db.Column('status', db.Column(db.Boolean(default=False)))
# 	)

class Pinjam(db.Model):
	id = db.Column('id_pinjam', db.Integer, primary_key=True)
	judul = db.Column(db.String(100), db.ForeignKey('buku.judul'))
	nama = db.Column(db.String(50), db.ForeignKey('anggota.nama'))
	status = db.Column(db.Boolean)

	def __init__(self):
		self.judul = judul
		self.nama = nama
		self.status = status

# if __name__ == '__main__':
# 	db.create_all()
# 	app.run(debug=True)
