#!/bin/bash
#i hate curl
curl -sI $1 | grep Allow | cut -d " " -f 2-
