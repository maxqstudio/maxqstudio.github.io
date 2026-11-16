import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';

const read = path => readFileSync(new URL(`../${path}`, import.meta.url), 'utf8');
const enTerms = read('max-cam-scanner/terms.html');
const idTerms = read('max-cam-scanner/id/terms.html');
const enPrivacy = read('max-cam-scanner/privacy.html');
const idPrivacy = read('max-cam-scanner/id/privacy.html');

export function assertTermsPages() {
  // English and Indonesian Terms describe cached editing and explicit saves.
  assert.match(enTerms, /local working cache/);
  assert.match(enTerms, /Only an explicit <em>Save to Workspace<\/em>/);
  assert.match(enTerms, /cache remains after that save and is hidden from Documents/);
  assert.match(enTerms, /<em>Save to Device<\/em> creates a separate local document/);
  assert.match(enTerms, /does not merge concurrent edits or promise simultaneous editing/);
  assert.match(idTerms, /cache kerja lokal/);
  assert.match(idTerms, /hanya diperbarui setelah kamu memilih <em>Simpan ke Workspace<\/em>/);
  assert.match(idTerms, /Cache tetap tersimpan setelah penyimpanan itu dan tidak ditampilkan di Dokumen/);
  assert.match(idTerms, /<em>Simpan ke Perangkat<\/em> membuat dokumen lokal yang terpisah/);
  assert.match(idTerms, /tidak menggabungkan perubahan bersamaan atau menjanjikan pengeditan simultan/);

  // Both languages document lease, recovery, conflict protection, and history links.
  for (const terms of [enTerms, idTerms]) {
    assert.match(terms, /30 seconds|30 detik/);
    assert.match(terms, /60 seconds|60 detik/);
    assert.match(terms, /same device|perangkat yang sama/);
    assert.match(terms, /base version|versi dasar/);
    assert.match(terms, /issues\/107/);
    assert.match(terms, /issues\/106/);
  }
  assert.match(enTerms, /force-stop, crash, power loss, or connectivity failure/);
  assert.match(idTerms, /Force-stop, crash, perangkat mati, atau gangguan koneksi/);

  // Both Privacy pages disclose the active editor identity to workspace members.
  assert.match(enPrivacy, /identity of the member currently editing a file/);
  assert.match(enPrivacy, /Workspace members can also see which member currently holds the editing session/);
  assert.match(idPrivacy, /identitas anggota yang sedang mengedit file/);
  assert.match(idPrivacy, /Anggota workspace juga dapat melihat anggota yang sedang memegang sesi edit/);
}
