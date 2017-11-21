from flask import Flask, request, flash, url_for, redirect, render_template
from model import Buku, Anggota, Pinjam, app

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/buku', methods=['GET'])
def lihat_buku():
	buku = Buku.query.all()
	return render_template('buku.html')


@app.route('/anggota', methods=['GET'])
def lihat_anggota():
	anggota = Anggota.query.all()
	return render_template('anggota.html')

@app.route('/tambah_buku', methods=['POST'])
def tambah_buku():
	if request.method == 'POST':
		if not request.form['judul'] or not request.form['pengarang'] or not request.form['penerbit']:
			flash('Silahkan masukan semua data bukunya')
		else:
			buku = Buku(request.form['judul'], request.form['pengarang'], request.form['penerbit'])

			db.session.add(buku)
			db.session.commit()

			flash('Penyimpanan buku sukses bertambah')
			return redirect(url_for('lihat_buku'))
	return render_template()

@app.route('/tambah_anggota', methods=['POST'])
def tambah_anggota():
	if request.method == 'POST':
		if not request.form['nama'] or not request.form['alamat']:
			flash('Silahkan masukan semua data anggota barunya')
		else:
			anggota = Anggota(request.form['nama'], request.form['alamat'])

			db.session.add(anggota)
			db.session.commit()

			flash('Penambahan anggota baru sukses')
			return redirect(url_for('lihat_anggota'))

	return render_template()



@app.route('/peminjaman', methods=['POST', 'GET'])
def peminjaman():
	pinjam = Pinjam.query.all()
	return render_template('pinjam.html')


# for handling form see it below
# http://exploreflask.com/en/latest/forms.html 