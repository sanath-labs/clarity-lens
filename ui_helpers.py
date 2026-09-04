def format_sentence_with_flags(sentence, flags):
    """
    Returns an HTML string highlighting a sentence based on its detected flags.
    Red = absolute language, Orange = emotional language, Blue = missing source.
    """
    badges = []

    if flags.get("absolute_language"):
        words = ", ".join(flags["absolute_language"])
        badges.append("<span style='background-color:#ffcccc;padding:2px 6px;border-radius:4px;margin-right:6px;display:inline-block;margin-bottom:4px;'>Absolute: " + words + "</span>")

    if flags.get("emotional_language"):
        words = ", ".join(flags["emotional_language"])
        badges.append("<span style='background-color:#ffe4b3;padding:2px 6px;border-radius:4px;margin-right:6px;display:inline-block;margin-bottom:4px;'>Emotional: " + words + "</span>")

    if flags.get("missing_source"):
        badges.append("<span style='background-color:#cce5ff;padding:2px 6px;border-radius:4px;margin-right:6px;display:inline-block;margin-bottom:4px;'>Missing source</span>")

    if badges:
        badges_html = "".join(badges)
    else:
        badges_html = "<span style='color:gray;'>No flags detected</span>"

    return "<p>" + sentence + "</p><div>" + badges_html + "</div><hr>"

def render_flag_badges(counts: dict) -> str:
    """
    Renders styled HTML metric badges for flag totals.
    """
    total = counts.get("total_flags", 0)
    abs_count = counts.get("absolute_language", 0)
    emo_count = counts.get("emotional_language", 0)
    src_count = counts.get("missing_source", 0)

    html = f"""
    <div style='display: flex; gap: 10px; margin: 10px 0;'>
        <span style='background-color:#ffebee; color:#c62828; padding: 4px 8px; border-radius: 4px; font-weight: bold;'>Total Flags: {total}</span>
        <span style='background-color:#ffcccc; padding: 4px 8px; border-radius: 4px;'>Absolute: {abs_count}</span>
        <span style='background-color:#ffe4b3; padding: 4px 8px; border-radius: 4px;'>Emotional: {emo_count}</span>
        <span style='background-color:#cce5ff; padding: 4px 8px; border-radius: 4px;'>Missing Source: {src_count}</span>
    </div>
    """
    return html.strip()
