VERSION 0.8

IMPORT ./gazebo AS gazebo


jetty:
    ARG registry='localhost/'
    ARG image_name='gazebo'
    BUILD --pass-args gazebo+jetty


ionic:
    ARG registry='localhost/'
    ARG image_name='gazebo'
    BUILD --pass-args gazebo+ionic


harmonic:
    ARG registry='localhost/'
    ARG image_name='gazebo'
    BUILD --pass-args gazebo+harmonic


fortress:
    ARG registry='localhost/'
    ARG image_name='gazebo'
    BUILD --pass-args gazebo+fortress


jetty-multiarch:
    ARG registry='localhost/'
    ARG image_name='gazebo'
    BUILD --pass-args --platform=linux/amd64 --platform=linux/arm64/v8 +jetty


ionic-multiarch:
    ARG registry='localhost/'
    ARG image_name='gazebo'
    BUILD --pass-args --platform=linux/amd64 --platform=linux/arm64/v8 +ionic


harmonic-multiarch:
    ARG registry='localhost/'
    ARG image_name='gazebo'
    BUILD --pass-args --platform=linux/amd64 --platform=linux/arm64/v8 +harmonic


fortress-multiarch:
    ARG registry='localhost/'
    ARG image_name='gazebo'
    BUILD --pass-args --platform=linux/amd64 --platform=linux/arm64/v8 +fortress
