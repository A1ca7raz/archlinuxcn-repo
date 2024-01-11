#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['poly000'])
    update_pkgrel()
    vcs_update()

def post_build():
    git_pkgbuild_commit()
