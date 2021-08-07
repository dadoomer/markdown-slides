"""Export utilities."""
import subprocess
from pathlib import Path


SUPPORTED_BROWSERS = ["chromium"]


def pdf_chromium_export(index_html_path: Path, output_pdf_path: Path):
    """Use Chromium to export an HTML file to PDF. On failure raises
    `subprocess.CalledProcessError`."""
    command = [
        'chromium',
        '--headless',
        '--print-to-pdf={}'.format(output_pdf_path),
        index_html_path.resolve().as_uri()+'?print-pdf',
    ]
    subprocess.run(command, check=True)


def export(index_html_path: Path, output_pdf_path: Path):
    """Export an HTML file to PDF."""
    try:
        pdf_chromium_export(index_html_path, output_pdf_path)
    except subprocess.CalledProcessError as exception:
        print("PDF exporting failed")
        print(exception)
        print(
                "Make sure a supported browser is installed and in your path"
                f" {SUPPORTED_BROWSERS}"
            )
