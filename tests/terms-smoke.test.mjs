import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';

const read = path => readFileSync(new URL(`../${path}`, import.meta.url), 'utf8');
const enTerms = read('max-cam-scanner/terms.html');
const idTerms = read('max-cam-scanner/id/terms.html');
const enPrivacy = read('max-cam-scanner/privacy.html');
const idPrivacy = read('max-cam-scanner/id/privacy.html');
const enLanding = read('max-cam-scanner/index.html');
const idLanding = read('max-cam-scanner/id/index.html');
const enSupport = read('max-cam-scanner/support.html');
const idSupport = read('max-cam-scanner/id/support.html');

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

  // AI mode is live and its external processing is disclosed in both languages.
  assert.match(enTerms, /Effective 16 November 2026/);
  assert.match(enTerms, /AI mode, subject to the usage limits shown in the App/);
  assert.match(enTerms, /selected page images are sent to our server and the AI provider or providers configured/);
  assert.match(enTerms, /AI conversion may misread or omit content/);
  assert.match(enTerms, /https:\/\/openai\.com\/business-data\//);
  assert.match(enTerms, /https:\/\/privacy\.anthropic\.com\/en\//);
  assert.doesNotMatch(enTerms, /AI mode once available/);
  assert.match(idTerms, /Berlaku sejak 16 November 2026/);
  assert.match(idTerms, /mode AI dengan batas pemakaian/);
  assert.match(idTerms, /gambar halaman yang dipilih dikirim ke server kami dan penyedia AI/);
  assert.match(idTerms, /Konversi AI dapat salah membaca atau melewatkan isi/);
  assert.doesNotMatch(idTerms, /mode AI saat fitur itu tersedia/);

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

  assert.match(enPrivacy, /Effective 16 November 2026/);
  assert.match(enPrivacy, /selected page images are sent through our server to configured AI provider/);
  assert.match(enPrivacy, /Up to 10 page images may be sent in one request/);
  assert.match(enPrivacy, /AI result is returned to the App as a local document draft/);
  assert.match(enPrivacy, /Each AI provider handles submitted images under its own terms and privacy practices/);
  assert.doesNotMatch(enPrivacy, /current version does not send documents to any AI service/);
  assert.match(idPrivacy, /Berlaku sejak 16 November 2026/);
  assert.match(idPrivacy, /gambar halaman yang dipilih dikirim melalui server kami ke penyedia AI/);
  assert.match(idPrivacy, /Maksimal 10 gambar halaman/);
  assert.match(idPrivacy, /sebagai draf dokumen lokal/);
  assert.match(idPrivacy, /menangani gambar yang dikirim sesuai ketentuan dan praktik privasinya sendiri/);
  assert.doesNotMatch(idPrivacy, /Versi saat ini tidak mengirim dokumen ke layanan AI/);

  // Scanner pages describe the standalone app and current AI/storage/history behavior.
  for (const page of [enLanding, idLanding, enTerms, idTerms, enPrivacy, idPrivacy, enSupport, idSupport]) {
    assert.match(page, /maxq\.tools/);
    assert.doesNotMatch(page, /Same plan on maxq\.tools|Paket yang sama di maxq\.tools/);
    assert.doesNotMatch(page, /AI mode.{0,50}(Soon|next update)|Mode AI.{0,50}(Segera|update berikutnya)/i);
  }
  assert.match(enLanding, /standalone Android document scanner/i);
  assert.match(enLanding, /They do not connect or sync with maxq\.tools/);
  assert.match(idLanding, /aplikasi pemindai dokumen Android mandiri/i);
  assert.match(idLanding, /tidak terhubung atau tersinkron dengan maxq\.tools/);
  assert.match(enSupport, /AI mode is available on eligible paid plans/);
  assert.match(idSupport, /Mode AI tersedia di paket berbayar/);
  assert.match(enSupport, /full version history/);
  assert.match(idSupport, /seluruh riwayat versi/);
  assert.match(enSupport, /Pro and Pro Team have 25 GB/);
  assert.match(idSupport, /Pro dan Pro Team memiliki penyimpanan 25 GB/);
}
