#!/bin/bash

# ================================================================
#                  [TeamDev](https://t.me/team_x_og)
#
#          Project Id     -> 30.
#          Project Name   -> TeamDev X Music
#          Project Age    -> 15D+ (Updated On 05/05/2026)
#          Idea By        -> @MR_ARMAN_08
#          Dev By         -> @MR_ARMAN_08
#          Powered By     -> @Team_X_Og ( On Telegram )
#          Updates        -> @TeamDevXBots ( On Telegram )
#
#          This Script Part Off https://t.me/Team_X_Og's Team.
#          Copyright (c) 2026 TeamDev | @Team_X_Og
# ================================================================

cred='\033[0;31m'
cgreen='\033[0;32m'
cyellow='\033[0;33m'
cblue='\033[0;34m'
cpurple='\033[0;35m'
ccyan='\033[0;36m'
cwhite='\033[0;37m'

pprint() {
    local color="${cpurple}"
    [ ! -z "$2" ] && eval "color=\$$2"
    printf "${color}$1${cwhite}"
}

yesnoprompt() {
    local old_stty_cfg=$(stty -g)
    stty raw -echo
    answer=$(head -c 1)
    stty $old_stty_cfg
    echo "$answer" | grep -iq "^y"
}

update_system() {
    pprint "\n╭────────────────────────────────────╮\n" "cblue"
    pprint "│   Updating Package List...         │\n" "cblue"
    pprint "╰────────────────────────────────────╯\n" "cblue"

    sudo apt update 2>&1 | grep "can be upgraded" &>/dev/null
    if [ $? -eq 0 ]; then
        pprint "✓ Updates Available\n" "cyellow"
        pprint "\nDo you want to upgrade? (y/n): " "cwhite"
        if yesnoprompt; then
            pprint "\n\nUpgrading packages... "
            sudo apt upgrade -y &>/dev/null && pprint "✓ Done\n\n" "cgreen" || { pprint "✗ Failed\n\n" "cred"; exit 1; }
        else
            pprint "\n\nSkipping upgrade...\n" "cyellow"
        fi
    else
        pprint "✓ Already Up to Date\n\n" "cgreen"
    fi
}

install_packages() {
    pprint "\n╭────────────────────────────────────╮\n" "cblue"
    pprint "│   Installing Required Packages     │\n" "cblue"
    pprint "╰────────────────────────────────────╯\n" "cblue"

    if ! command -v pip3 &>/dev/null; then
        pprint "\n→ Installing Python3-pip... "
        sudo apt install python3-pip -y 2>pypilog.txt 1>/dev/null && pprint "✓ Done\n" "cgreen" || { pprint "✗ Failed\n" "cred"; exit 1; }
    else
        pprint "\n✓ Python3-pip already installed\n" "cgreen"
    fi

    if ! command -v ffmpeg &>/dev/null; then
        pprint "→ Installing FFmpeg... "
        sudo apt install ffmpeg -y &>/dev/null && pprint "✓ Done\n" "cgreen" || { pprint "✗ Failed\n" "cred"; exit 1; }
    else
        pprint "✓ FFmpeg already installed\n" "cgreen"
    fi

    local fv=$(ffmpeg -version 2>/dev/null | grep -Po 'version (3.*?) ')
    [ ! -z "$fv" ] && pprint "\n⚠ Warning: FFmpeg $fv detected. Version 4+ required for live streams.\n" "cyellow"

    for pkg in git curl wget unzip build-essential libffi-dev libssl-dev; do
        if ! dpkg -s "$pkg" &>/dev/null; then
            pprint "→ Installing $pkg... "
            sudo apt install -y "$pkg" &>/dev/null && pprint "✓ Done\n" "cgreen" || pprint "✗ Failed\n" "cred"
        fi
    done
}

install_deno() {
    pprint "\n╭────────────────────────────────────╮\n" "cblue"
    pprint "│   Installing Deno Runtime          │\n" "cblue"
    pprint "╰────────────────────────────────────╯\n" "cblue"

    if command -v deno &>/dev/null; then
        pprint "\n✓ Deno already installed: $(deno --version | head -1)\n" "cgreen"
        return
    fi

    pprint "\n→ Downloading and installing Deno... "
    curl -fsSL https://deno.land/install.sh | sh &>denolog.txt

    export DENO_INSTALL="$HOME/.deno"
    export PATH="$DENO_INSTALL/bin:$PATH"

    SHELL_RC="$HOME/.bashrc"
    [[ -f "$HOME/.zshrc" ]] && SHELL_RC="$HOME/.zshrc"
    if ! grep -q "DENO_INSTALL" "$SHELL_RC" 2>/dev/null; then
        {
            echo ''
            echo '# Deno'
            echo 'export DENO_INSTALL="$HOME/.deno"'
            echo 'export PATH="$DENO_INSTALL/bin:$PATH"'
        } >> "$SHELL_RC"
    fi

    if command -v deno &>/dev/null; then
        pprint "✓ Done\n\n" "cgreen"
    else
        pprint "✗ Failed\n\n" "cred"
        pprint "⚠ Install Deno manually: https://deno.land\n" "cyellow"
    fi
}

install_ytdlp() {
    pprint "\n╭────────────────────────────────────╮\n" "cblue"
    pprint "│   Installing yt-dlp (Latest)       │\n" "cblue"
    pprint "╰────────────────────────────────────╯\n" "cblue"

    pprint "\n→ Downloading yt-dlp binary... "
    curl -fsSL "https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp" \
        -o /usr/local/bin/yt-dlp 2>ytdlplog.txt && chmod a+rx /usr/local/bin/yt-dlp

    if command -v yt-dlp &>/dev/null; then
        pprint "✓ Done → $(yt-dlp --version)\n\n" "cgreen"
    else
        pprint "✗ Binary failed, trying pip... "
        pip3 install -q "https://github.com/yt-dlp/yt-dlp/archive/master.zip" &>>ytdlplog.txt
        command -v yt-dlp &>/dev/null && pprint "✓ Done\n\n" "cgreen" || { pprint "✗ Failed\n\n" "cred"; exit 1; }
    fi
}

install_dependencies() {
    pprint "\n╭────────────────────────────────────╮\n" "cblue"
    pprint "│   Installing Python Dependencies   │\n" "cblue"
    pprint "╰────────────────────────────────────╯\n" "cblue"

    pprint "\n→ Upgrading pip... "
    pip3 install -U pip &>>pypilog.txt && pprint "✓ Done\n" "cgreen" || { pprint "✗ Failed\n" "cred"; exit 1; }

    pprint "→ Patching py-tgcalls to 2.1.0... "
    sed -i 's/py-tgcalls==.*/py-tgcalls==2.1.0/' requirements.txt
    sed -i '/yt-dlp/d' requirements.txt
    pprint "✓ Done\n" "cgreen"

    pprint "→ Installing requirements... "
    pip3 install --no-cache-dir -U -r requirements.txt &>>pypilog.txt && pprint "✓ Done\n" "cgreen" || { pprint "✗ Failed\n" "cred"; exit 1; }

    pprint "→ Pinning py-tgcalls==2.1.0... "
    pip3 install -q "py-tgcalls==2.1.0" &>>pypilog.txt && pprint "✓ Done\n\n" "cgreen" || { pprint "✗ Failed\n\n" "cred"; exit 1; }
}

get_input() {
    local prompt="$1"
    local value
    pprint "$prompt: " "ccyan"
    printf "${cwhite}"
    read value
    echo "$value"
}

create_env() {
    pprint "\n╭────────────────────────────────────╮\n" "cblue"
    pprint "│   Bot Configuration Setup          │\n" "cblue"
    pprint "╰────────────────────────────────────╯\n\n" "cblue"

    pprint "ℹ Get API credentials from https://my.telegram.org\n\n" "cyellow"

    api_id=$(get_input       "API ID           ")
    api_hash=$(get_input     "API HASH         ")
    bot_token=$(get_input    "BOT TOKEN        ")
    owner_id=$(get_input     "OWNER ID         ")
    mongo_db=$(get_input     "MONGO DB URI     ")
    log_group=$(get_input    "LOG GROUP ID     ")
    string1=$(get_input      "STRING SESSION   ")
    string2=$(get_input      "STRING SESSION 2 (optional)")
    string3=$(get_input      "STRING SESSION 3 (optional)")
    git_token=$(get_input    "GIT TOKEN        (optional)")

    pprint "\n→ Saving configuration... " "cwhite"

    [ -f .env ] && rm .env

    cat > .env <<EOF
API_ID=$api_id
API_HASH=$api_hash
BOT_TOKEN=$bot_token
OWNER_ID=$owner_id
MONGO_DB_URI=$mongo_db
LOG_GROUP_ID=$log_group
MUSIC_BOT_NAME=TeamDevXMusic
STRING_SESSION=$string1
STRING_SESSION2=$string2
STRING_SESSION3=$string3
STRING_SESSION4=
STRING_SESSION5=
GIT_TOKEN=$git_token
UPSTREAM_REPO=https://github.com/justfortestingnothibghere/TeamDev-Music
UPSTREAM_BRANCH=fix-teamxog-replacement-and-pytgcalls-bug-494525827456582041
COOKIES=
EOF

    pprint "✓ Done\n" "cgreen"
}

main() {
    clear
    pprint "\n╔════════════════════════════════════╗\n" "cpurple"
    pprint "║                                    ║\n" "cpurple"
    pprint "║           Music  •  Setup       ║\n" "cpurple"
    pprint "║                                    ║\n" "cpurple"
    pprint "║    Dev    →  @Lord_Vasudev_Krishna          ║\n" "cpurple"
    pprint "║    Team   →  @Lord_Vasudev_Krishna            ║\n" "cpurple"
    pprint "║                                    ║\n" "cpurple"
    pprint "╚════════════════════════════════════╝\n\n" "cpurple"

    pprint "ℹ Error Logs:\n" "cblue"
    pprint "  • Python errors  → pypilog.txt\n" "cwhite"
    pprint "  • Deno errors    → denolog.txt\n" "cwhite"
    pprint "  • yt-dlp errors  → ytdlplog.txt\n\n" "cwhite"

    sleep 1

    pprint "⚠ This script requires sudo privileges.\n" "cyellow"
    sudo -v || exit 1

    update_system
    install_packages
    install_deno
    install_ytdlp
    install_dependencies

    pprint "\n╔════════════════════════════════════╗\n" "cgreen"
    pprint "║   Installation Completed! ✓        ║\n" "cgreen"
    pprint "╚════════════════════════════════════╝\n\n" "cgreen"

    sleep 1
    create_env

    clear
    pprint "\n╔════════════════════════════════════╗\n" "cgreen"
    pprint "║                                    ║\n" "cgreen"
    pprint "║   Setup Completed Successfully! ✓  ║\n" "cgreen"
    pprint "║                                    ║\n" "cgreen"
    pprint "╚════════════════════════════════════╝\n\n" "cgreen"

    pprint "✓ Configuration saved to .env\n" "cgreen"
    pprint "\nℹ To edit variables: " "cblue"
    pprint "vi .env\n" "cwhite"
    pprint "\n→ Start the bot: " "cyellow"
    pprint "python3 -m TeamDevXMusic\n" "cgreen"
    pprint "→ Run in background: " "cyellow"
    pprint "nohup python3 -m TeamDevXMusic &> teamdev.log &\n\n" "cgreen"
    pprint "  Need help?  →  https://t.me/Lord_Vasudev_Krishna\n" "ccyan"
    pprint "  Updates     →  https://t.me/SECRECT_BOT_UPDATES\n\n" "ccyan"
}

main
