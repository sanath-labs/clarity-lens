# 1. Introduction

## 1.1 Background

The volume of information people encounter daily - news articles, social
media posts, forwarded messages, advertisements - has grown far faster
than most people's tools for evaluating that information critically.
Existing solutions largely fall into two categories: fact-checking tools
that provide a binary true/false verdict with no visible reasoning, and
summarization tools that compress content without evaluating its logical
or evidential quality. Neither category helps the reader develop or apply
critical thinking skills themselves.

## 1.2 Problem Statement

Ordinary readers - students, parents, professionals - frequently lack an
accessible way to identify weak reasoning, loaded language, or unverified
claims in text they encounter, or in their own decision-making. This gap
leaves people vulnerable to misinformation and persuasive but poorly
evidenced arguments, and provides no structured way to examine their own
reasoning before making a decision.

## 1.3 Objectives

This project aims to:
1. Detect specific, well-documented reasoning weaknesses (absolute
   language, emotionally loaded language, unsourced claims) in a
   transparent, explainable way.
2. Generate a neutral summary and the strongest opposing viewpoint for
   any analyzed text, so users can weigh both sides.
3. Support personal decision-making through Socratic questioning rather
   than direct advice.
4. Persist analysis history so users can review their own patterns over time.

## 1.4 Scope

The system is a single-user, English-language, browser-based tool. It is
explicitly not a fact-checker, not a source of financial/legal/medical
advice, and not a replacement for human judgment - see
docs/methodology.md for the full design rationale.
