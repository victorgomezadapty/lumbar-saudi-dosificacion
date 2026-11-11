"""Genera ../og.png (1200x630) a partir de og.html con Chrome o Edge en modo headless. Uso: cd src && python3 render_og.py"""
import shutil
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
CANDIDATES = [
    "/opt/google/chrome/chrome",
    shutil.which("chromium"), shutil.which("chromium-browser"), shutil.which("chrome"), shutil.which("msedge"),
    shutil.which("google-chrome"),
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
]

browser = next((c for c in CANDIDATES if c and Path(c).exists()), None)
if not browser:
    raise SystemExit("No se encontró Chrome ni Edge para generar la imagen")
out = HERE.parent / "og.png"
with tempfile.TemporaryDirectory() as profile:
    subprocess.run([browser, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
                    "--force-device-scale-factor=1", f"--user-data-dir={profile}",
                    "--window-size=1200,630", "--virtual-time-budget=8000", f"--screenshot={out}",
                    (HERE / "og.html").as_uri()], check=True, capture_output=True, timeout=30)
print(f"ok: {out.name} ({out.stat().st_size:,} bytes)")
