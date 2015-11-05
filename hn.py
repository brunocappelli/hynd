#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
#this will get the top stories from HackerNews (news.ycombinator.com)

from hn import HN, Story

hn = HN()

# print the first 2 pages of newest stories
for story in hn.get_stories(story_type='newest', limit=60):
        print(story.rank, story.title)
