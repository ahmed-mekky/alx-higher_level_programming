#!/bin/bash
#i hate curl
curl -sI -w "%{http_code}" -o /dev/null $1
