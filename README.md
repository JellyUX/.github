# JellyUX/.github

Organization-level files for [JellyUX](https://github.com/JellyUX).

- **`profile/README.md`** renders on the organization landing page.
- **`manifest.json`** is the combined Jellyfin plugin repository for the whole
  suite. Users add a single URL to Jellyfin:
  ```
  https://raw.githubusercontent.com/JellyUX/.github/main/manifest.json
  ```
  It is rebuilt from each plugin's own manifest by
  `.github/workflows/sync-manifest.yml` (daily, and on demand). Add or remove a
  plugin by editing `sources.json`.
