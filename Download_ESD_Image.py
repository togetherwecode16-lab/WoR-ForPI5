import os
import sys
import urllib.request
from pathlib import Path

# URL of the ESD file
URL = "http://dl.delivery.mp.microsoft.com/filestreamingservice/files/826e5c00-e4bf-42b9-9419-3bc999053e41/26200.6899.251011-1532.25h2_ge_release_svc_refresh_CLIENTCONSUMER_RET_A64FRE_en-us.esd"

def download_file(url):
    # Determine Downloads folder cross-platform
    if sys.platform == "win32":
        downloads_path = Path(os.path.join(os.environ['USERPROFILE'], 'Downloads'))
    else:
        downloads_path = Path.home() / "Downloads"

    downloads_path.mkdir(parents=True, exist_ok=True)
    filename = url.split("/")[-1]
    file_path = downloads_path / filename

    # Resume support
    mode = 'wb'
    headers = {}
    downloaded = 0
    if file_path.exists():
        downloaded = file_path.stat().st_size
        headers['Range'] = f'bytes={downloaded}-'
        mode = 'ab'
        print(f"Resuming download from {downloaded} bytes...")

    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response, open(file_path, mode) as f:
        total_size = response.getheader('Content-Length')
        if total_size:
            total_size = int(total_size) + downloaded
        chunk_size = 1024 * 1024  # 1 MB
        while True:
            chunk = response.read(chunk_size)
            if not chunk:
                break
            f.write(chunk)
            downloaded += len(chunk)
            if total_size:
                done = int(50 * downloaded / total_size)
                print(f"\r[{'='*done}{' '*(50-done)}] {downloaded/1024/1024:.2f}/{total_size/1024/1024:.2f} MB", end="")
            else:
                print(f"\rDownloaded {downloaded/1024/1024:.2f} MB", end="")

    print(f"\nDownload completed: {file_path}")

if __name__ == "__main__":
    download_file(URL)
