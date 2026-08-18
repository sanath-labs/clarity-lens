def format_sentence_with_flags(sentence, flags):
    """
    Returns an HTML string highlighting a sentence based on its detected flags.
    Red = absolute language, Orange = emotional language, Blue = missing source.
    """
    badges = []

    if flags.get("absolute_language"):
        words = ", ".join(flags["absolute_language"])
        badges.append("<span style='background-color:#ffcccc;padding:2px 6px;border-radius:4px;margin-right:4px;'>Absolute: " + words + "</span>")

    if flags.get("emotional_language"):
        words = ", ".join(flags["emotional_language"])
        badges.append("<span style='background-color:#ffe4b3;padding:2px 6px;border-radius:4px;margin-right:4px;'>Emotional: " + words + "</span>")

    if flags.get("missing_source"):
        badges.append("<span style='background-color:#cce5ff;padding:2px 6px;border-radius:4px;margin-right:4px;'>Missing source</span>")

    if badges:
        badges_html = "".join(badges)
    else:
        badges_html = "<span style='color:gray;'>No flags detected</span>"

    return "<p>" + sentence + "</p><div>" + badges_html + "</div><hr>"
