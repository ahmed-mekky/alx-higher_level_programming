#!/bin/bash
#i hate curl
curl -sI $1 | grep Status | cut -d " " -f 2-
