#!/usr/bin/env python
# -*- coding: utf-8 -*-
#可以扩展统计每个单词出现的频率
file_name = "/root/movie.txt"

line_counts = 0
word_counts = 0
character_counts = 0

with open(file_name, 'r') as f:
    for  line  in f:
        words = line.split()

        line_counts += 1
        word_counts += 1
        character_counts += len(line)

print "line_counts", line_counts
print "words_counts", word_counts
print "character_count", character_counts
