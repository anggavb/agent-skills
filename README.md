# Personal Skills

Project ini merupakan backup kumpulan skills dan konfigurasi AI agent dari PC pribadi saya yang sudah saya terapkan dalam penggunaan sehari-hari. Repository ini menyimpan salinannya agar setup tersebut mudah dipulihkan, digunakan kembali, dan dipindahkan ke PC lain.

## Isi Repository

| Lokasi | Keterangan |
| --- | --- |
| [`agent-workspace/`](agent-workspace/) | Skill workspace untuk Velda, mengatur folder kerja tiap profil Hermes. |
| [`trading-daily/`](trading-daily/) | Skill riset dan penyusunan morning brief pasar saham Indonesia (IDX), beserta referensi, template, contoh, dan script validasi. |
| [`.codex/AGENTS.md`](.codex/AGENTS.md) | Instruksi workflow Go untuk Codex, termasuk kapan perlu berkonsultasi dengan subagent. |
| [`.codex/agents/go-skills-advisor.toml`](.codex/agents/go-skills-advisor.toml) | Konfigurasi subagent `go_skills_advisor` sebagai penasihat engineering Go dengan instruksi dan sandbox `read-only`. |

## Struktur Skills

```text
personal-skills/
├── .codex/
│   ├── AGENTS.md
│   └── agents/
│       └── go-skills-advisor.toml
├── agent-workspace/
│   └── SKILL.md
├── trading-daily/
│   ├── SKILL.md
│   ├── examples/
│   ├── references/
│   ├── scripts/
│   └── templates/
└── README.md
```

## Instalasi Skills di Project atau Workspace Lokal

Untuk Codex, salin skill yang ingin digunakan ke `<project>/.agents/skills/<nama-skill>/`. Jika workspace berisi beberapa repository Git terpisah, pasang skill di masing-masing repository yang membutuhkannya. Pada monorepo, skill di `.agents/skills/` root tersedia saat Codex dijalankan dari subfolder repository tersebut. Lihat [dokumentasi lokasi skills Codex](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills).

Folder skill di root `personal-skills` merupakan sumber backup. Saat dipasang di project tujuan, salin seluruh folder skill beserta resource pendukungnya ke `.agents/skills/`.

### Windows (PowerShell)

Contoh berikut menggunakan checkout repository ini di `D:\personal-skills`. Sesuaikan lokasi sumber, project tujuan, dan nama skill:

```powershell
$skillsSource = 'D:\personal-skills'
$projectPath = 'D:\workspace\my-project'
$skillName = 'trading-daily'
$skillsDestination = Join-Path $projectPath '.agents\skills'

New-Item -ItemType Directory -Path $skillsDestination -Force | Out-Null
Copy-Item -LiteralPath (Join-Path $skillsSource $skillName) -Destination $skillsDestination -Recurse
```

### Linux / macOS (Bash)

```bash
skills_source="$HOME/personal-skills"
project_path="$HOME/workspace/my-project"
skill_name="trading-daily"

mkdir -p "$project_path/.agents/skills"
cp -R "$skills_source/$skill_name" "$project_path/.agents/skills/"
```

Contoh di atas ditujukan untuk pemasangan pertama. Jika folder skill tujuan sudah ada, bandingkan isinya terlebih dahulu sebelum memperbarui salinannya. Perubahan pada sumber backup perlu disalin kembali ke project agar versi lokal ikut diperbarui.

Hasil instalasi:

```text
my-project/
└── .agents/
    └── skills/
        └── trading-daily/
            ├── SKILL.md
            ├── examples/
            ├── references/
            ├── scripts/
            └── templates/
```

Jalankan Codex dari project tujuan, lalu gunakan `/skills` untuk memeriksa skill yang tersedia. Codex mendeteksi perubahan skill secara otomatis; jika belum muncul, mulai ulang Codex. Skill juga dapat dipanggil secara eksplisit, misalnya `$trading-daily`.

Periksa kebutuhan runtime setiap skill sebelum digunakan. Sebagai contoh, `agent-workspace` memuat instruksi khusus profil Hermes dan lokasi workspace Linux; pemasangan folder ke Codex saja belum menyediakan runtime Hermes.

## Setup Codex Global

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
