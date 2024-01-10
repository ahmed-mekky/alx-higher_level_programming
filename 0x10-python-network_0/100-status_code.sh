#!/bin/bash
#i hate curl
curl -sI $1 | grep HTTP | cut -d " " -f2
