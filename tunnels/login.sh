#!/usr/bin/env zsh
dest=$1
ssh -F ~/.ssh/tunnels.config -fN $dest-tunnel
ssh -F ~/.ssh/tunnels.config $dest
