---
title: Alias Commands
layout: home
---

# Alias Commands

{% for section in site.data.aliases.sections %}

##  {{ section.section }}

{% for command in section.commands %}

### {{ command.alias }}

command: {{ command.name }}

usage: {{ command.usage }}

description: {{ command.description }}

{% endfor %}

{% endfor %}