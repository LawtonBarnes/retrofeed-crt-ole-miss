# RetroFeed Project Notes

## Environment
- Raspberry Pi 3B+, 64-bit Raspberry Pi OS, username `metalshop`, hostname `raspberrypi-02`
- CRT TV connected via composite/RCA
- Display: framebuffer_width=312, framebuffer_height=360 (26 cols x 15 rows)
- KMS driver (vc4-kms-v3d) is commented out — using legacy fbcon framebuffer driver
- Font: Uni2-TerminusBold24x12.psf.gz, applied via `sudo setfont` in ~/.bashrc on tty1
- Sudoers exception at /etc/sudoers.d/consolefont for passwordless setfont
- Python deps: beautifulsoup4, requests
- Screen width: 26 characters

## Testing workflow
- Don't reboot to test changes — use: `pkill -f retrofeed.py && python retrofeed.py`

## Code conventions
- display.py has a set_color() method for ANSI inline color switching
- Color scheme per segment: green=loading, red/blue=Ole Miss, magenta=AP Top 25, cyan=NYT
- pr_flag()-style pattern used for multi-color ASCII art rendering

## Segments implemented
Ole Miss football, SEC football, Pete Golding, CFB rankings, NYT News,
ESPN College Football, AP Top 25, Ole Miss schedule (ICS/Google Calendar),
Ole Miss ASCII art

## Gotchas
- VS Code Server requires 64-bit OS (32-bit armv7l is incompatible)