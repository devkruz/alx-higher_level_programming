#!/bin/bash
# 3. cURL only methods
curl -Is "$1" | grep "Allow" | cut -d " " -f 2-
