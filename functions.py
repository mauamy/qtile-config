import subprocess
import pywal

from variables import HOME


def get_pywal_colors(wallpaper):
    pywal_colors = pywal.colors.get(wallpaper)
    cols = pywal_colors["special"]
    cols.update(pywal_colors["colors"])
    return cols


def set_wallpaper(wallpaper):
    subprocess.call([HOME + '/.config/qtile/scripts/set-wallpaper.sh', wallpaper])
