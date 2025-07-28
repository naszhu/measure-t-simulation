```bash
# Create an autostart entry so Obsidian launches on login
mkdir -p "$HOME/.config/autostart"
cat > "$HOME/.config/autostart/obsidian.desktop" <<'EOF'
[Desktop Entry]
Type=Application
Exec=/home/YOUR_USERNAME/bin/obsidian
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=Obsidian
EOF
```