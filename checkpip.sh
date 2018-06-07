#!/usr/bin/env bash

req_file="./requirements/local.txt"
tmp_file="/root/requirements.txt.md5"


if [ ! -f $tmp_file ]; then
    md5sum $req_file >  $tmp_file
    pip3 install --upgrade -r $req_file
else
    md5sum -c $tmp_file
    if [ $? -ne 0 ]; then
        pip3 install --upgrade -r $req_file
    fi
fi
