#!/bin/sh

doppler run -- gunicorn -w 3 -b :$PORT server:app