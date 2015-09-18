#!/usr/bin/perl -w -CAS
use utf8;

$_ = lc join('', <>);

s/[^\p{L}\s]//g;
s/[\s]+/ /g;

print;

