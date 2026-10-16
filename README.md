# Personal Skills

Project ini merupakan backup kumpulan skills dan konfigurasi AI agent dari PC pribadi saya yang sudah saya terapkan dalam penggunaan sehari-hari. Repository ini menyimpan salinannya agar setup tersebut mudah dipulihkan, digunakan kembali, dan dipindahkan ke PC lain.

## Isi Repository

| Lokasi | Keterangan |
| --- | --- |
| [`skills/`](skills/) | Kumpulan skills pribadi beserta referensi, template, contoh, dan script pendukung. |
| [`skills/agent-workspace/`](skills/agent-workspace/) | Skill workspace untuk Velda, mengatur folder kerja tiap profil Hermes. |
| [`.codex/AGENTS.md`](.codex/AGENTS.md) | Instruksi workflow Go untuk Codex, termasuk kapan perlu berkonsultasi dengan subagent. |
| [`.codex/agents/go-skills-advisor.toml`](.codex/agents/go-skills-advisor.toml) | Konfigurasi subagent `go_skills_advisor` sebagai penasihat engineering Go dengan instruksi dan sandbox `read-only`. |

## Setup Codex

### 1. Terapkan Konfigurasi Global

Untuk menggunakan setup ini di berbagai project, salin file backup ke direktori pengguna berikut. Codex mendukung custom agent global di `~/.codex/agents/`. Lihat [dokumentasi subagent Codex](https://learn.chatgpt.com/docs/agent-configuration/subagents).

| File Backup | Tujuan di Windows |
| --- | --- |
| `.codex\AGENTS.md` | `%USERPROFILE%\.codex\AGENTS.md` |
| `.codex\agents\go-skills-advisor.toml` | `%USERPROFILE%\.codex\agents\go-skills-advisor.toml` |

Jika sudah memiliki `AGENTS.md` global, gabungkan workflow dari backup dengan instruksi yang sudah ada.

### 2. Instal Skills Go yang Dibutuhkan

**Sebelum menggunakan `.codex\agents\go-skills-advisor.toml`, perlu menginstal skills dari [samber/cc-skills-golang](https://github.com/samber/cc-skills-golang).** Skills tersebut merupakan dependensi eksternal dan perlu dipasang terpisah dari repository ini.

Ikuti panduan instalasi pada repository tersebut dan pasang skills secara global untuk Codex di:

```text
~/.agents/skills/
```

Pada Windows, lokasi tersebut adalah:

```text
%USERPROFILE%\.agents\skills\
```

Pastikan folder skills `golang-*` beserta `SKILL.md` dan resource pendukungnya tersedia di lokasi itu. Konfigurasi advisor menggunakan direktori tersebut untuk memilih dan membaca skills yang relevan. Lokasi skills global juga dijelaskan dalam [dokumentasi skills Codex](https://learn.chatgpt.com/docs/build-skills).

### 3. Mulai Sesi Codex

Buka sesi Codex baru setelah menerapkan setup. Di Codex CLI, gunakan `/skills` untuk memeriksa apakah skills Go sudah terdeteksi.

Contoh permintaan untuk menggunakan advisor:

```text
Gunakan subagent go_skills_advisor untuk meninjau rencana perubahan Go ini
sebelum implementasi, lalu terapkan rekomendasi yang sesuai dengan project.
```

## Peran Go Skills Advisor

`go_skills_advisor` membaca kode dan skills yang relevan, lalu memberi rekomendasi untuk pekerjaan Go yang membutuhkan keputusan engineering, seperti transaksi database, error handling, context, concurrency, API, dan arsitektur.

Agent utama tetap bertanggung jawab atas perubahan file, implementasi, dan validasi. Sesuai workflow dalam `.codex/AGENTS.md`, perubahan berisiko lebih tinggi juga ditinjau kembali oleh advisor setelah implementasi.
