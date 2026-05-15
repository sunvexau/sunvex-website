#!/usr/bin/env python3
"""Convert BFS business card proof PDF to PNG for visual inspection."""
import subprocess, os

pdf = "/Users/sunvex/Desktop/Projects/support-internal/brand system/BFS/Brand pack/07_print-ready/business-card/business-card-proof.pdf"
out = "/Users/sunvex/Desktop/bfs-card-preview.png"

# Convert first page of PDF to PNG at 300 DPI
subprocess.run([
    "magick", "convert",
    "-density", "300",
    pdf + "[0]",
    "-resize", "1200x",
    out
], check=True)
print(f"Saved to {out}")
print(f"Size: {os.path.getsize(out)} bytes")
