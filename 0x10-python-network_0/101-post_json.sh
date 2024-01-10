#!/bin/bash
#i hate curl
curl -sd "@$2" -H "Content-Type: application/json" $1
