# JellyUX

A small suite of plugins that refine the Jellyfin web experience. Each one is
self-contained, targets Jellyfin 10.11.x, and uses the
[File Transformation](https://github.com/IAmParadox27/jellyfin-plugin-file-transformation)
plugin to inject its assets. None of them patch Jellyfin itself, and each can be
uninstalled with no residue.

## Plugins

| Plugin | What it does |
|---|---|
| **[Homepage](https://github.com/JellyUX/Homepage)** | A modular home screen engine. Replaces the default Jellyfin landing page with configurable widgets for native content, personalized recommendations, and external sources. |
| **[Keep or Remove](https://github.com/JellyUX/Keep_or_Remove)** | Users vote keep or remove on movies and series; the admin gets a read-only aggregated table to decide library rotation by hand. Never modifies the library. |

Each repository holds that plugin's full documentation, screenshots, and release notes.

## Installation

1. In Jellyfin: **Dashboard > Plugins > Repositories > Add**
2. Paste this URL:
   ```
   https://raw.githubusercontent.com/JellyUX/.github/main/manifest.json
   ```
3. Open **Dashboard > Plugins > Catalog**, install any JellyUX plugin, then restart Jellyfin.

Adding the single URL above exposes every JellyUX plugin in the catalog.

## Requirements

- Jellyfin **10.11.x**
- The [File Transformation](https://github.com/IAmParadox27/jellyfin-plugin-file-transformation) plugin

## License

Every plugin is released under **GPL-3.0**. See each repository for details.
