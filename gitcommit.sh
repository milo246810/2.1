#!/bin/bash

#cd/linuxopg
git add *
git config --global user.email "milo21@live.dk"
git config --global user.name "milo246810"
echo Navn til commiten?
read commit
git commit -m $commit
git push

