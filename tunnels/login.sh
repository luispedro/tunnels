#!/usr/bin/env zsh
dest=$1
ssh -F ~/.ssh/tunnels.config -f $dest-tunnel sleep 10
ssh -F ~/.ssh/tunnels.config $dest
