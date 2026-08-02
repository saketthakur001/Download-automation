# Download-automation

A personal collection of Python scripts for auto-finding and downloading movies/anime
episodes from various streaming/download sites, with some Windows-only screen-automation
thrown in to click through the sites' download flows.

This is a grab-bag of experiments rather than a single polished tool — expect duplicated
logic, hardcoded paths, and a couple of broken/unfinished files.

## What's here

All the code lives in `1Automate Downloading/`:

- **`movies_verse.py` / `movies_verse_2.0.py`** — Google-searches for a movie on
  moviesverse.org.in, scrapes the download page for a Google Drive link, opens it in the
  browser, then uses `pyautogui` to click through the site's "click to generate link" /
  "download anyway" prompts by matching screenshots stored in `New folder/`.
- **`moviesverse_click.py`** — just the `pyautogui` screen-clicking loop from the script
  above, without the search/scrape part.
- **`mkvking.py`** — same idea as `movies_verse.py` but targets mkvking.me, with a
  hardcoded quality (`480`).
- **`gogo.py` / `gogoanime_2.0.py`** — searches for an anime title on gogoanime and tries
  to resolve a download/stream link. Contains an anime-name-spelling helper
  (`check_anime_spell`) that cross-checks against MyAnimeList.
- **`gogorename.py`** — a standalone utility that walks a directory (`D:\` by default) and
  strips a `gogoanime` prefix/tag out of downloaded file names.
- **`google_search/google_search.py`** — a small helper that scrapes Google's HTML search
  results page (no API) for result links; used by the other scripts.
- **`grab_the_beast/grab_the_beast.ipynb`** — notebook version of `google_search`, used to
  look a title up on gotytv.com. Also just runs `import this` for the Zen of Python.
- **`New folder/*.png`** — reference screenshots (buttons like "click to generate link",
  "download anyway", "not a robot", etc.) that `pyautogui` matches against the screen to
  find where to click.
- **`data.py`** — scratch notes/commented-out snippets, not runnable code.
- **`test.py`**, **`Untitled-1.txt.py`** — unrelated scratch files. `Untitled-1.txt.py`
  in particular does not run as-is (it has a syntax error on an incomplete assignment).
- **`1Automate Downloading.rar`** — an archived copy of (part of) this same folder.

## How it (theoretically) runs

These were written for a specific Windows machine and are not portable out of the box:

- Several scripts hardcode `C:\Users\saket\...` paths for locating the reference
  screenshots, and `gogorename.py` hardcodes `D:\\` as the folder to rename files in.
  You'll need to edit these paths for your own machine.
- Dependencies used across the scripts: `requests`, `beautifulsoup4`, `googlesearch-python`,
  `pyautogui`.

  ```
  pip install requests beautifulsoup4 googlesearch-python pyautogui
  ```

- The `pyautogui`-based scripts (`movies_verse_2.0.py`, `mkvking.py`,
  `moviesverse_click.py`) work by template-matching the PNGs in `New folder/` against
  whatever is currently on screen, so they need the target website already open in a
  visible browser window at the right screen resolution/zoom the screenshots were taken
  at.
- Run a script directly, e.g.:

  ```
  python "1Automate Downloading/movies_verse_2.0.py"
  ```

  and enter a movie name when prompted.

## Known limitations

- Scraping Google's search results HTML directly (`google_search.py`) is fragile and
  breaks whenever Google changes its markup or serves a captcha.
- Site-scraping logic (CSS class names, link patterns) is tied to the exact HTML structure
  of moviesverse/mkvking/gogoanime at the time this was written and will likely need
  updating if those sites have changed.
- Screen-click automation only works on the original author's screen setup (paths,
  resolution) and on Windows.
- `Untitled-1.txt.py` is broken (incomplete `space =` assignment) and `test.py` is unrelated
  scratch code — neither is part of the actual download-automation flow.
- No error handling for "not found" cases in most scripts beyond printing a message; a few
  paths will raise if a link/class isn't found on the page.
